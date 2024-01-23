from django.shortcuts import render, redirect
from .models import CryptoCurrency, News
from django.db.models import Count
from .forms import AddCryptocurrencyForm
from rest_framework import viewsets
from .serializers import NewsSerializer, CryproCurrencySerializer
from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection

def index(request):
    news_data = News.objects.values('currencies__name', 'currencies__id').annotate(news_count=Count('id'))
    # print(news_data)
    # print(connection.queries)
    return render(request, 'index.html', {'news_data': news_data})

def show_crypto_currency_news(request, currency_id):
    crypto_cyrrency_news = News.objects.select_related('channel').filter(currencies__id=currency_id)
    currency = CryptoCurrency.objects.get(id=currency_id)
    # print(crypto_cyrrency_news.query)
    # print(connection.queries)
    return render(request, 'currency_news.html', {'currency_news': crypto_cyrrency_news, 'currency': currency})

def add_cryptocurrency(request):
    if request.method == 'POST':
        form = AddCryptocurrencyForm(request.POST) #экзепляр класс формы
        if form.is_valid(): #валидация формы
            CryptoCurrency.objects.create(name=form.cleaned_data['name']) #устраняем посторонние символы
            return redirect('/')
        else:
            return render(request, 'add_cryptocurrency.html', {'form': form}) #если пользователь нарушил вводу, тогда покажем страницу с ошибками
    else:
        form = AddCryptocurrencyForm()
        return render(request, 'add_cryptocurrency.html', {'form': form})


class NewsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(detail=False)
    def process_old_news(self, request):
        print('Score old news')
        return Response({'Status': 'Ok'})


class CryptoCurrencyViewSet(viewsets.ModelViewSet):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryproCurrencySerializer

def show_test_api(request):
    return render(request, 'api_test.html')




from django.db import models
from django.core.exceptions import ValidationError

def check_currency_name(value):
    if not value.isalpha():
        raise ValidationError(f'Name of crypto currency must consist of letters:{value}')



class CryptoCurrency(models.Model):
    name = models.CharField(max_length=4, validators=[check_currency_name])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TelegramChannel(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class News(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(TelegramChannel, on_delete=models.CASCADE)
    currencies = models.ManyToManyField(CryptoCurrency)

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'News record'
        verbose_name_plural = 'News'




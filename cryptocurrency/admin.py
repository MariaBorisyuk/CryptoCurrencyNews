from django.contrib import admin
from .models import CryptoCurrency, News, TelegramChannel

admin.site.register(CryptoCurrency)
admin.site.register(News)
admin.site.register(TelegramChannel)


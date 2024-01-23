# CryptoCurrencyNews
## Описание:
Проект построен на базе django, Telethon, telebot.
Собирает новости из Телеграм-каналов, связанных с криптовалютами.
Анализирует упоминание в тексте новости какой-либо криптовалюты.
Демонстрирует пользователю статистику по выбранной криптовалюте в телеграмм-боте.

## Установка и настройка:
1. Создать файл .env в корне проекта
2. Получить ключи для доступа к [API телеграмм](https://my.telegram.org/auth?to=apps)
3. Создать в файле .env переменную API_ID и заполнить ее полученным значением
4. Создать в файле .env переменную API_HASH и заполнить ее полученным значением
5. Зарегистрировать телеграмм-бота в [BotFather](https://t.me/BotFather)
6. Создать в файле .env переменную API_BOT_HASH и заполнить ее полученным значением от BotFather
7. Выполнить миграции:
   'python manage.py makemigrations'
   'python manage.py migrate'
8. Создайте администратор системы:
   'python manage.py createsuperuser'
9. Запустите сервер системы:
   'python manage.py runserver'
10. Перейдите в браузере по адресу:
    'http://127.0.0.1:8000/admin/'
11. Перейдите в раздел "Crypto currencys" и добавте тикеры(абривиатуры) криптовалют для их поиска в новостях
12. Перейдите в раздел "Telegram channels" и добавте телеграмм-каналы с новостями о криптовалютах.
Для того чтобы узнать номер канала перешлите сообщение из этого канала в [IDBot](https://t.me/username_to_id_bot)
13. Запустите телеграмм-клиент, чтобы он начал собирать новости из телеграм-каналов:
    'python telegram_client.py'
14. Запустите телеграм-бота для отображение статистики по новостям:
    'python telegram_bot.py'

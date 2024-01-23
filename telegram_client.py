from telethon.sync import TelegramClient, events
import os
import sys
import django
from pathlib import Path
from dotenv import load_dotenv
from asgiref.sync import sync_to_async

load_dotenv()


BASE_DIR = str(Path(__file__).resolve().parent)

sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from cryptocurrency.models import News, TelegramChannel, CryptoCurrency

channels_ids = list(TelegramChannel.objects.all().values_list('number', flat=True))


api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']

client = TelegramClient('mariaborisyuk', api_id, api_hash, device_model='MacBook Pro', system_version='macOS Venture 13.4.1')


@client.on(events.NewMessage(chats=channels_ids))
async def handle_message(event):
    channel = await sync_to_async(TelegramChannel.objects.get)(number=int('100'+str(event.message.peer_id.channel_id)))
    news_object = await sync_to_async(News.objects.create)(text=event.message.message, channel=channel)
    found_crypto = []
    for currency in await sync_to_async(list)(CryptoCurrency.objects.all()):
        if currency.name.lower() in news_object.text.lower():
            found_crypto.append(currency)
    await sync_to_async(news_object.currencies.add)(*found_crypto)
    print(event.message)


if __name__ == '__main__':
    client.start()
    print('client started')
    client.run_until_disconnected()


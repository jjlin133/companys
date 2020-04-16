from django.shortcuts import render
from companysapp.models import company6666 as company
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from datetime import datetime
from flask import Flask
from flask import request
from flask import abort
from linebot.models import *
logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)
"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('1wvrzWVhcC3NtqQmCrim4ja4Jp0AhOq7l+XrdcAkVrAzQNassUG4agDdgMQQV66wQWRvwuxEJqS4AyNF+CrfKgO7QMhbylmeOWaeRKYT70OWTR3gdTPgxROUA/6xx/eUpPFEkcXuuaJsacCgrvg4wAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('e9d9f0bbe0dd52767bb719eccd45f652') #ehappyFunc5

line_bot_api.push_message('Uaa63a3f5feff2725536db7d81f09c929', TextSendMessage(text='可以開始連結Heroku'))

@csrf_exempt
@require_POST
def callback(request):
    signature = request.META['HTTP_X_Line_Signature']
    body = request.body.decode('utf-8')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = ( "Invalid signature. Please check your channel access token/channel secret.")
        HttpResponseForbidden()

    return HttpResponse('OK',status=200)


@handler.add(event=MessageEvent, message=TextMessage)
def handl_message(event: MessageEvent):
           line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=TextSendMessage(text=event.message.text),
        )

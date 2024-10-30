from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import datetime
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


# def WeeklyReportNotification() :
#     Monday == 0
#     today = datetime.datetime.today().weekday()
#     NowHour = datetime.now().hour
#     NowMinute = datetime.now().minute
#     if NowHour == 9 and NowMinute == 2 :
#         message = """
# 同學好，
# 請記得要在今天完成 Weekly Report 的填寫。

# SR
#     """
#         line_bot_api.reply_message(event.reply_token, message)
#         return True 
#     else :
#         return False
    # if today == 4 :
        

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    NowHour = datetime.now().hour
    NowMinute = datetime.now().minute
    message = """
同學好，
請記得要在今天完成 Weekly Report 的填寫。

SR
    """
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
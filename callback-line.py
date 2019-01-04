from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# YOUR_CHANNEL_ACCESS_TOKEN
line_bot_api = LineBotApi('tP3Do5wL7vL9FUMETeVzSWpbOA/Z6jbOplAmSATekEOPMYXb78yRZW4UveUGdjJqhK8tfKr1KKnksrqKY9Q/3OkCD8Blc7NkyyrPzpf1Z2R7uym1l2A4qRRtWg8avC9Apb/WfKpKZ+H0F40GFqykcQdB04t89/1O/w1cDnyilFU=')
# YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
from flask import Flask, request
import re
from src.errors import Error
from src.bot import Bot
app = Flask(__name__)

@app.route("/bot_call", methods=['POST'])
def get_channel_info():
    if request.method == 'POST':
        try:
            text = str(request.form['text']).lower()
            print text
            channel = request.form['channel_id']
            user_id = request.form['user_id']
            user = request.form['user_name']
            ratio = re.search("[0-9]+", text)
            ratio_group = int(ratio.group(0))/float(100)
        except:
            raise Error.ParameterError("Parameters are not correct")
        try:
            Bot(channel_id=channel, reply_user_id=user_id, reply_user_name=user).assign(text=text,ratio=ratio_group)
        except:
            raise Error.MessageError("Message is incorrect")
        return "200"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
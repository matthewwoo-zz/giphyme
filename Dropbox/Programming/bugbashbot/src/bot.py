import calendar
import json
import re
import time
import urllib2
import uuid

from datetime import datetime
import time

import requests
from slackclient import SlackClient
import src.constants as BotConstants

class Bot(object):
    def __init__(self, bot_token=BotConstants.TOKEN,
                 bot_username=BotConstants.BOTNAME,
                 channel_id=None,
                 reply_user_id=None,
                 reply_user_name=None):
        self.bot_token = bot_token
        self.username = bot_username
        self.channel_id = channel_id
        self.reply_user_id = reply_user_id
        self.reply_user_name = reply_user_name

    def success_message(self, num_articles):
        sc = SlackClient(self.bot_token)
        sc.api_call(
            "chat.postMessage", channel=self.channel_id,
            text="Hello <@{}|{}> just grabbed {} new articles for you :newspaper:!".format(self.reply_user_id, self.reply_user_name, num_articles),
            username=self.username, as_user="false", icon_emoji=':instapaper:'
        )
        return 200

    def fail_message(self):
        sc = SlackClient(self.bot_token)
        sc.api_call(
            "chat.postMessage", channel=self.channel_id,
            text="Sorry <@{}|{}> not sure if I can do that".format(self.reply_user_id, self.reply_user_name),
            username=self.username, as_user="false", icon_emoji=':instapaper:')
        return 200

    def get_messages(self, channel=None, start_time=None):
        channel = self.channel_id if channel is None else channel
        sc = SlackClient(self.bot_token)
        if start_time == None:
            json_data = sc.api_call("channels.history", channel=channel, count=10)
        else:
            json_data = sc.api_call("channels.history", channel=channel, oldest=start_time)
        message_dump = json.dumps(json_data)
        message_dict = json.loads(message_dump)
        num_articles = 0
        for msg in message_dict['messages']:
            if 'attachments' in msg:
                x = msg['attachments'][0]['from_url']
                Article().save_to_instapaper(url=x)
                print x
                num_articles += 1
        return self.success_message(num_articles=num_articles)


    def get_links(self):
        pass

    def json(self):
        return
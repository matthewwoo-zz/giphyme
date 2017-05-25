import json
import random
import math
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

    def assign(self, text, ratio):
        sc = SlackClient(self.bot_token)
        if 'zdco' in text:
            team = self.active_channel_users(sc=sc)
            text2 = self.zdco(team=team, ratio=ratio)
            self.msg(sc=sc, text=text2)
        elif 'sfco' in text:
            team = self.active_channel_users(sc=sc)
            text2 = self.sfdc(team=team, ratio=ratio)
            self.msg(sc=sc, text=text2)
        else:
            self.fail_message(sc=sc)
        return 200

    def active_channel_users(self, sc):
        x = sc.api_call("channels.info", channel=self.channel_id)
        dump_data = json.dumps(x)
        data = json.loads(dump_data)
        num_users = len(data['channel']['members'])
        members = []
        for i in range(0, num_users):
            cur_member = data['channel']['members'][i]
            if self.check_presence(sc=sc, user=cur_member) == 'active':
                members.append(cur_member)
                i += 1
        random_members = random.sample(members, len(members))
        return random_members

    @staticmethod
    def check_presence(user, sc):
        x = sc.api_call("users.getPresence", user=user)
        user_state = x['presence']
        return user_state

    def post_msg(self, member, sc):
        return sc.api_call("chat.postMessage", channel=self.channel_id, text="<@{}>".format(member), username=self.username)

    def zdco(self, team, ratio):
        num_team = len(team)
        num_agents = int(math.ceil(len(team)*ratio))
        if ratio == 0:
            num_agents = 1
        if num_agents == num_team:
            num_agents = num_agents - 1
        agents = "\n\n*Call Agents*\n"
        for i in range(0, num_agents):
            if i < num_team:
                agents += str("<@"+team[i]+">" + "\n")
                i += 1
        customers = "\n\n*Customers*\n"
        for i in range(num_agents, num_team):
            if i < num_team:
                customers += str("<@"+team[i]+">" + "\n")
                i += 1
        instructions = "\n\nTeam: When call gets transferred, new agent please mention:" \
                       + "\n- if you see verified " \
                       + "\n- how many photos you receive" \
                       +"\n- and what is the new queue the call got transferred to"
        text = "*ZDCO* " + agents + customers + instructions
        return text

    def sfdc(self, team, ratio):
        num_team = len(team)
        num_agents = int(math.ceil(len(team) * ratio))
        if ratio == 0:
            num_agents = 1
        if num_agents == num_team:
            num_agents = num_agents - 1
        agents = "\n\n*Call Agents*\n"
        for i in range(0, num_agents):
            if i < num_team:
                agents += str("<@" + team[i] + ">" + "\n")
                i += 1
        customers = "\n\n*Customers*\n"
        for i in range(num_agents, num_team):
            if i < num_team:
                customers += str("<@" + team[i] + ">" + "\n")
                i += 1
        instructions = "\n\nTeam: When call gets transferred, new agent please mention:" \
                       + "\n- if you see verified " \
                       + "\n- how many photos you receive" \
                       + "\n- and what is the new queue the call got transferred to"
        text = "*SFCO* " + agents + customers + instructions
        return text

    def msg(self, sc, text):
        sc.api_call(
            "chat.postMessage", channel=self.channel_id,text="{}".format(text),username=self.username)
        return 200


    def fail_message(self,sc):
        sc.api_call(
            "chat.postMessage", channel=self.channel_id,
            text="<@{}|{}> sorry I didn't get what envirionment you wanted please specify SFDC or ZDCO".format(
                self.reply_user_id, self.reply_user_name),
            username=self.username)
        return 200


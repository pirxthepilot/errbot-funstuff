from __future__ import absolute_import, division, print_function

from errbot import BotPlugin, botcmd, re_botcmd
import requests
import random
import re


class Funstuff(BotPlugin):
    """Random short fun things"""

    @botcmd
    def insult(self, msg, args):
        """ I fart in your general direction! """
        fired = requests.get('http://quandyfactory.com/insult/json')
        shot = fired.json()['insult'].lower()
        if args:
            return "%s, %s" % (args, shot)
        else:
            return shot.capitalize()

    @re_botcmd(pattern=r"^(who|what)('?s|.* is)", prefixed=False, flags=re.IGNORECASE)
    def whoisbot(self, msg, match):
        """ Bot, introduce thyself """
        if self.bot_config.CHATROOM_FN.lower() in msg.body.lower():
            try:
                room = str(msg.frm.room).split('@')[0]
            except AttributeError:
                room = 'nobody'
            responses = [
                "I am your friendly neighborhood chat bot.",
                "I am here to serve.",
                "Just call my name and I'll be there.",
                "Some bots just want to watch the world burn.",
                "I like green eggs and ham!",
                "I. am. a. robot. Beep boop beep.",
                "Are you talkin' to me?",
                "I'm the hero %s deserves." % room
            ]
            return random.choice(responses)

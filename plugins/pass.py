#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmpp

class Plugin(object):
    only_admin = False
    command = "pass"

    @classmethod
    def run(cls, bot, mess):
        user=str(mess.getFrom()).split('/')[0]

        text = mess.getBody()
        if text == 'pass '+bot.config['pass']:
            bot.config['user_no_pass'].append(user)
            text = 'password right'
            bot.send(xmpp.Message(mess.getFrom(),text))
        else:
            text = 'password wrong'
            bot.send(xmpp.Message(mess.getFrom(),text))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmpp

class Plugin(object):
    only_admin = False
    command = "help"

    @classmethod
    def run(cls, bot, mess):
        text = 'user: '+str(bot.plugins['public_commands'])

        user=str(mess.getFrom()).split('/')[0]

        if user in bot.config['user_no_pass']:
            text += '\nadmin: '+str(bot.plugins['commands'])

        bot.send(xmpp.Message(mess.getFrom(),text))

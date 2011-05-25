#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmpp

class Plugin(object):
    only_admin = True
    command = "off"

    @classmethod
    def run(cl, bot, mess):
        bot.online = 0
        bot.send(xmpp.Message(mess.getFrom(),'closing bot...'))

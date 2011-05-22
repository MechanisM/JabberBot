#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmpp

class Plugin(object):
    only_admin = False
    command = "echo"

    @classmethod
    def run(cl, bot, mess):
        bot.send(xmpp.Message(mess.getFrom(), mess.getBody()))

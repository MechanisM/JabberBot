#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import xmpp

class Plugin(object):
    only_admin = True
    command = "cmd"

    @classmethod
    def run(cls, bot, mess):
        cmd = mess.getBody()[4:]
        output = os.popen(cmd).read()

        if not isinstance(output, unicode):
            output = unicode(output,'utf-8','ignore')

        bot.send(xmpp.Message(mess.getFrom(),output))
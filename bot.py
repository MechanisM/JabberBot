#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
import xmpp

LOGIN = "testaccforbot@jabber.ru"
PASSWORD = "qwerty3"

PASS_FOR_ADMIN = "123"

def loadPlugins(bot):
    for file in glob.glob("plugins/*.py"):
        if "__init__.py" in file:
            continue
        pl_name = file.split("\\")[1].split(".")[0]
        pl = "plugins."+pl_name

        mod = getattr(__import__(pl), pl_name)
        cl = getattr(mod, "Plugin")
        bot.plugins['plugins'][pl_name] = cl
        if cl.only_admin:
            bot.plugins['commands'].append(pl_name)
        else:
            bot.plugins['public_commands'].append(pl_name)


def runPlugin(command, bot, mess):
    plugin = bot.plugins['plugins'][command]
    plugin.run(bot, mess)

def message(conn, mess):
    global bot
    text = mess.getBody()
    if not text:
        return

    command = text.split(' ')[0]
    if command in bot.plugins['public_commands']:
        runPlugin(command, bot, mess)
        return

    user = str(mess.getFrom()).split('/')[0]

    if user not in bot.config['user_no_pass']:
        text = "wrong command. try 'help'"
        bot.send(xmpp.Message(mess.getFrom(), text))
        return

    if command in bot.plugins['commands']:
        runPlugin(command, bot, mess)
    else:
        text = "wrong command. try 'help'"
        bot.send(xmpp.Message(mess.getFrom(), text))
    return

##########
jid = xmpp.JID(LOGIN)
bot = xmpp.Client(jid.getDomain(), debug=[])
bot.plugins = {
    "plugins": {},
    "public_commands": [],
    "commands": [],
}
bot.config = {
    'user_no_pass':[],
    'pass': PASS_FOR_ADMIN
}

loadPlugins(bot)

if "gmail" in LOGIN:
    conres = bot.connect( server=('talk.google.com', 5223) )
else:
    conres = bot.connect()

if not conres:
    print "Unable to connect to server!"
    sys.exit(1)
authres = bot.auth(jid.getNode(), PASSWORD)
if not authres:
    print "Unable to authorize - check login/password"
    sys.exit(1)

bot.RegisterHandler('message', message)

bot.sendInitPresence()
print "Bot started"
bot.online = 1
while bot.online:
    bot.Process(1)
bot.disconnect()
print "Bot stopped"

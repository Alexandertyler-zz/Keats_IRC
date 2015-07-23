def action(ircsock, chan, nick, msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")

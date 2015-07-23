import sys

def action(connection, msg):
    connection.send('kill')
    connection.close()
    sys.exit(1)

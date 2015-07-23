def action(connection, msg):
    connection.send('say:' + msg)

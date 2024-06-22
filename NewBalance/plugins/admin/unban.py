
from srca.configs import addCommand,Client
from db.mongo_client import MongoDB
from random import randrange


@addCommand('unban')
def bin(_,m):
    querY = MongoDB().query_user(int(m.from_user.id))
    if  querY == None: return m.reply('Usar el comando $register para el registro.')
    
    if MongoDB().admin(int(m.from_user.id)) == False: return ...
    
    data = m.text.split(' ')
    
    if len(data) < 2: return m.reply('ingrese datos correctos <code>$free id </code>')

    idw = int(data[1])

    MongoDB().unban(idw)

    texto= f'''<b>User comando UNBan

Name: {m.from_user.first_name}
id: {m.from_user.id}
Username: @{m.from_user.username}
━━━━━━━━
A desbaneado  a este id
• id: <code>{idw}</code>
━━━━━━━━━━
</b>'''
    Client.send_message(_,chat_id=-4286695568,text=texto)
    return m.reply('El usuario ahora esta desbaneado.')

from srca.configs import addCommand, Client
from db.mongo_client import MongoDB

@addCommand('register')
def start(_, m):
    try:
        user_id = int(m.from_user.id)
        querY = MongoDB().query_user(user_id)

        if querY is None:
            data = {
                'id': user_id,
                'plan': 'free',
                'role': 'user',
                'credits': 0,
                'antispam': 40,
                'since': None
            }
            MongoDB().insert_user(data)

            texto = f'''<b>New User 

Name: {m.from_user.first_name}
id: {user_id}
Username: @{m.from_user.username}</b>'''
            Client.send_message(_, chat_id=-4286695568, text=texto)

            return m.reply_text(f'Welcome {m.from_user.first_name}, you have just registered ✳️.')

        else:
            return m.reply('<b>You are already registered.</b>')

    except Exception as e:
        print(f"Error in registration: {str(e)}")
        return m.reply('<b>Registration failed. Please try again later.</b>')

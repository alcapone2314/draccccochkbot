from pyrogram import Client, filters
from paquetes.plantillas import atras

@Client.on_callback_query(filters.regex("gates"))
def gates_coman(client, message):
    message.edit_message_text('''<b>Gaterways comando
- Stripe Gate ( /ah )
- Braintree Avs ( /br )
- Shopify Normal ( /sh )
- Shopify Adyen ( /sa )
- Shopify Normal ( /se )
- Shopify Normal ( /st )
- Shopify Cyber ( /sy )
- Paypal 0.01$ ( /pp )
- Vbv Braintree ( /vbv )</b>''',reply_markup=atras(message.from_user.id))
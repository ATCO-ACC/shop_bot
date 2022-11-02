from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
import re
from functions import *


TOKEN = '5792806053:AAEQHQTNSN2GSlA9ZuFFzKmbi8UA4WUAyMI'
bot = Bot(token=TOKEN)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher



# TODO Create function to CHECK if item is in the items json file, ADD or DELETE items from json file
# TODO Create user 'account' with personal information and orders
# TODO Connect payment method
# TODO Add owners (admins) of the shop to get notifications, manage items and orders

# TODO Add a few commands to enhance bot's possibilities

with open('data/admins.json') as adn:
    admins = json.load(adn)


def new_hand(command):
    name = command.__name__+'_handler'
    print(name)
    locals()[name] = CommandHandler(command.__name__, command)
    dispatcher.add_handler(locals()[name])


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='Greetings Customer! Welcome to our shop!',
                             reply_markup=mmenu)
    context.bot.send_message(chat_id=chat_id, text='How can I help you?', reply_markup=test_menu)
new_hand(start)


commands = '''
/start - calls Main menu
/my_orders - shows your pending orders
/saved - shows your saved items
/manage - manage this shop (admins only)'''


def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=commands)
new_hand(help)


def manage(update: Update, context: CallbackContext):
    id = str(update.effective_chat.id)
    if id in admins.keys():
        context.bot.send_message(chat_id=id, text=f"Welcome, {admins[id]}", reply_markup=manage_m)
    else:
        context.bot.send_message(chat_id=id, text="You're not identified")
new_hand(manage)


def unid_msg(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text
    chat_id = str(message.chat.id)
    if text == 'Catalogue':
        bot.send_message(chat_id=chat_id, text="Let's have a look at our goodies!", reply_markup=catalogue)
    elif text == 'Basket':
        bot.send_message(chat_id=chat_id, text="Let's have a look at your basket!")
        show_basket(bot, chat_id)
    elif text == 'Contacts':
        bot.send_message(chat_id=chat_id, text='You can contact us via:')
        bot.send_message(chat_id=chat_id, text='📞Phone: +7 777 777 7777\n✈Telegram: @test_shop_bot\n🟢WhatsApp: +7 777 777 7778')
    else:
    #context.bot.send_message(chat_id=chat_id, text='Please, choose:', reply_markup=test_menu)
        update.message.reply_text('If require any help, please, use /help command')
unid_msg_hler = MessageHandler(Filters.text, unid_msg)
dispatcher.add_handler(unid_msg_hler)


print('Commands are successfully added, admiral!')


def menu_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = str(query.message.chat.id)
    data = query.data
    basket = readJson('data/basket.json')
    if data == 'saved':
        context.bot.send_message(chat_id=chat_id, text='Work in progress', reply_markup=mmenu)
    elif data == 'basket':
        show_basket(bot, chat_id)
        #context.bot.send_message(chat_id=update.effective_chat.id, text='Work in progress', reply_markup=mmenu)
    elif data == 'contacts':
        bot.send_message(chat_id=chat_id, text='You can contact us via:')
        bot.send_message(chat_id=chat_id,
                         text='📞Phone: +7 777 777 7777\n✈Telegram: @test_shop_bot\n🟢WhatsApp: +7 777 777 7778')
    elif data == 'catalogue':
        context.bot.send_message(chat_id=chat_id, text='Please, choose from following items', reply_markup=catalogue)
    elif data in items.keys():
        quantity = 0
        if chat_id in basket:
            if data in basket[chat_id]:
                quantity = basket[chat_id][data]['quantity']
        image = open(f'./images/{data}.jpg', 'rb')
        bot.send_photo(chat_id=chat_id, photo=image)
        context.bot.send_message(chat_id=chat_id, text=f"{items[data]['name']} In basket: {quantity}",
                                 reply_markup=item_btn)
    elif data == 'add':
        item = re.search(r'\w+', query.message.text).group()
        add(bot, item, chat_id)
    elif data == 'delete':
        item = item = re.search(r'\w+', query.message.text).group()
        delete(bot, item, chat_id)
    elif data == 'back_fc':
        context.bot.send_message(chat_id=chat_id, text="And we're back in the Main menu",
                                 reply_markup=mmenu)
    elif data == 'back_fi':
        context.bot.send_message(chat_id=chat_id, text='Catalogue',
                                 reply_markup=catalogue)
    if data == 'clear_basket':
        clear_bask(bot, chat_id)
    if data == 'place_order':
        place_ordr(bot, chat_id, query)
    if data == 'show_ordr':
        show_orders(bot, chat_id)
    query.answer()
    #query.edit_message_text(text=f"Selected option: {query.data}")
    #bot.answer_callback_query(update.callback_query.id, text='Saved items')
dispatcher.add_handler(CallbackQueryHandler(menu_buttons))


updater.start_polling()
print("We're up and running.")





# update.callback_query content --
#{'data': 'catalogue',
# 'message': {'channel_chat_created': False,
#             'date': 1665222968,
#             'text': 'Please, choose:',
#             'entities': [],
#             'supergroup_chat_created': False,
#             'message_id': 150,
#             'photo': [],
#             'reply_markup': {'inline_keyboard': [[{'text': 'Saved', 'callback_data': 'saved'},
#                                                   {'text': 'Basket', 'callback_data': 'basket'}],
#                                                  [{'text': 'Catalogue', 'callback_data': 'catalogue'}],
#                                                  [{'text': 'Contacts', 'callback_data': 'contacts'}]]},
#             'group_chat_created': False,
#             'new_chat_photo': [],
#             'delete_chat_photo': False,
#             'chat': {'type': 'private',
#                      'id': 772615904,
#                      'username': 'procrastinatorg',
#                      'first_name': 'Атом'},
#             'new_chat_members': [],
#             'caption_entities': [],
#             'from': {'id': 5792806053,
#                      'is_bot': True,
#                      'username': 'TestShop5Bot',
#                      'first_name': 'TestShopBot'}},
# 'id': '3318360042637370004',
# 'chat_instance': '-7937715285777962955',
# 'from': {'id': 772615904,
#          'language_code': 'ru',
#          'is_bot': False,
#          'username': 'procrastinatorg',
#          'first_name': 'Атом'}}



# update.effective_chat content -- {'first_name': 'Атом',
# 'type': 'private',
# 'id': 772615904,
# 'username': 'procrastinatorg'}


# update.effective_message content -- {'new_chat_members': [],
# 'new_chat_photo': [],
# 'chat': {'id': 772615904, 'type': 'private', 'first_name': 'Атом', 'username': 'procrastinatorg'},
# 'delete_chat_photo': False,
# 'date': 1664740915,
# 'entities': [{'type': 'bot_command', 'length': 6, 'offset': 0}],
# 'message_id': 13,
# 'caption_entities': [],
# 'supergroup_chat_created': False,
# 'group_chat_created': False,
# 'text': '/start',
# 'channel_chat_created': False,
# 'photo': [],
# 'from': {'first_name': 'Атом', 'id': 772615904, 'username': 'procrastinatorg', 'language_code': 'ru', 'is_bot': False}}


'''new_items = {
    'apples': {
        'price': 5.00,
        'measure': 'kg',
        'in_stock': 10
    },
    'books': {
        'price': 10.00,
        'measure': 'item',
        'in_stock': 500
    },
    'water': {
        'price': 2.00,
        'measure': 'litre',
        'in_stock': 200
    },
    'beer': {
        'price': 3.00,
        'measure': 'can',
        'in_stock': 1000
    },
    'wine': {
        'price': 7.00,
        'measure': 'bottle',
        'in_stock': 15},
}'''




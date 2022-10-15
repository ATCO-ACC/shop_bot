from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
import json


with open('data/items.json', encoding='utf-8') as f:
    items = json.load(f)


mmenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Saved', callback_data='saved'),
     InlineKeyboardButton('Basket', callback_data='basket')],
                                                 [InlineKeyboardButton('Catalogue', callback_data='catalogue')],
    [InlineKeyboardButton('Contacts', callback_data='contacts')]
])

# CREATING CATALOGUE FROM ITEMS DICTIONARY
cat_kb = []
count = 0
line = []

for k, v in items.items():
    if count < 2:
        new = InlineKeyboardButton(f"{v['name']}, {v['price']} per {v['measure']}", callback_data=k)
        line.append(new)
        count += 1
        if k == list(items)[-1]:
            cat_kb.append(line)
    else:
        cat_kb.append(line)
        line = []
        count = 0
        new = InlineKeyboardButton(f"{v['name']}, {v['price']} per {v['measure']}", callback_data=k)
        line.append(new)
        count += 1
        if k == list(items)[-1]:
            cat_kb.append(line)
cat_kb.append([InlineKeyboardButton('Back', callback_data='back_fc')])
catalogue = InlineKeyboardMarkup(inline_keyboard=cat_kb)


item_btn = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Add', callback_data='add'),
                                                 InlineKeyboardButton('Delete', callback_data='delete')],
                                                 [InlineKeyboardButton('Back', callback_data='back_fi')]])


manage_m = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Current admins', callback_data='curr_adm')],
                                               [InlineKeyboardButton('Add items', callback_data='add_itm')],
                                               [InlineKeyboardButton('Show pending orders', callback_data='show_ordr')],
                                               ])


basket_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('Clear', callback_data='clear_basket')],
                                                 [InlineKeyboardButton('Place order', callback_data='place_order')]])

# TODO Create ReplyKeyboardMarkup

test_menu = ReplyKeyboardMarkup([[KeyboardButton('Catalogue'), KeyboardButton('Basket')],
                                 [KeyboardButton('Contacts')]], resize_keyboard=True)

print("We've got menus in tact, captain!")

from menus import *


def readJson(file):
    with open(file, encoding='utf-8') as fl:
       name = json.load(fl)
    return name


basket = readJson('data/basket.json')
orders = readJson('data/orders.json')


def add(bot, item, chat_id):
    for k, v in items.items():
        if item == v['name']:
            item = k
    price = items[item]['price']
    name = items[item]['name']
    if chat_id not in basket.keys():
        basket.setdefault(chat_id, {})
    if item not in basket[chat_id]:
        basket[chat_id].setdefault(item, {'name': name, 'quantity': 1, 'price': price})
    else:
        basket[chat_id][item]['quantity'] += 1
    with open('data/basket.json', 'w') as bs:
        json.dump(basket, bs)
    image = open(f'./images/{item}.jpg', 'rb')
    bot.send_message(chat_id=chat_id, text='Done!')
    bot.send_photo(chat_id=chat_id, photo=image)
    bot.send_message(chat_id=chat_id, text=f"{name} In basket: {basket[chat_id][item]['quantity']}",
                     reply_markup=item_btn)


def delete(bot, item, chat_id):
    for k, v in items.items():
        if item == v['name']:
            item = k
    if chat_id not in basket:
        bot.send_message(chat_id=chat_id, text='Your basket is empty :(', reply_markup=catalogue)
    else:
        name = basket[chat_id][item]['name']
        if item in basket[chat_id]:
            basket[chat_id][item]['quantity'] -= 1
            image = open(f'./images/{item}.jpg', 'rb')
            bot.send_message(chat_id=chat_id, text='Done!')
            bot.send_photo(chat_id=chat_id, photo=image)
            bot.send_message(chat_id=chat_id, text=f"{name} In basket: {basket[chat_id][item]['quantity']}",
                             reply_markup=item_btn)
            if basket[chat_id][item]['quantity'] <= 0:
                del basket[chat_id][item]
        else:
            bot.send_message(chat_id=chat_id, text='No such item found', reply_markup=catalogue)
    if basket[chat_id] == {}:
        del basket[chat_id]
    with open('data/basket.json', 'w') as bs:
        json.dump(basket, bs)


def show_basket(bot, chat_id):
    if chat_id not in basket.keys():
        bot.send_message(chat_id=chat_id, text='Your basket is empty :(', reply_markup=mmenu)
    else:
        text = ''
        for k, v in basket[chat_id].items():
            text += f"Item: {v['name']} Quantity: {v['quantity']}\n"
        if text == '':
            bot.send_message(chat_id=chat_id, text='Your basket is empty :(', reply_markup=mmenu)
        else:
            total = 0
            for k, v in basket[chat_id].items():
                summ = v['quantity'] * v['price']
                total += summ
            text += f"Total: {total}"
            bot.send_message(chat_id=chat_id, text=text, reply_markup=basket_menu)


def clear_bask(bot, chat_id):
    if chat_id not in basket:
        bot.send_message(chat_id=chat_id, text='Your basket is empty :(')
    else:
        del basket[chat_id]
        bot.send_message(chat_id=chat_id, text='Done!', reply_markup=mmenu)
    with open('data/basket.json', 'w') as bs:
        json.dump(basket, bs)


# TODO Create new order for each place order action
def place_ordr(bot, chat_id, query):
    chat = query.message.chat
    orders.setdefault(chat_id, {})
    id = orders[chat_id]
    id.setdefault('username', chat.username)
    id.setdefault('first_name', chat.first_name)
    id.setdefault('order_num', 0)
    id['order_num'] += 1
    new = f"order_{id['order_num']}"
    id.setdefault(new, {})
    for k, v in basket[chat_id].items():
        id[new].setdefault(k, {'quantity': v['quantity'], 'price': v['price']})
    with open('data/orders.json', 'w') as ord:
        json.dump(orders, ord)
    clear_bask(bot, chat_id)
    bot.send_message(chat_id=chat_id, text='Order placed!')
    admins = readJson('data/admins.json')
    for i in admins.keys():
        bot.send_message(chat_id=i, text="You've got a new order!")


def show_orders(bot, chat_id):
    if orders != {}:
        for i in orders.values():
            text = f"User name: {i['username']} First name: {i['first_name']}\n"
            for k in i.keys():
                if k.rstrip('0123456789') == 'order_':
                    text += f"Order: {k}\n"
                    for n, m in i[k].items():
                        text += f"Item: {n} Quantity: {m['quantity']}\n"
            bot.send_message(chat_id=chat_id, text=text)
    else:
        bot.send_message(chat_id=chat_id, text='No orders yet')

print('Functions created, sir!')
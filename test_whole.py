from functions import add, delete, basket, items, show_basket, clear_bask, place_ordr, orders, show_orders
from random import choice
import json

class MockBot():
    def send_message(chat_id='testing', text='Nah', **kwargs):
        return text
    def send_photo(**kwargs):
        return kwargs


class MockQuery():
    class message():
        class chat():
            username = 'a'
            first_name = 'b'

chat_id = 'testing'

class TestFunctions():
    def test_add(self):
        item = choice(list(items.keys()))

        if chat_id in basket.keys():
            del basket[chat_id]

        add(MockBot, item, chat_id)
        assert  basket != {}


    def test_delete(self):
        item = choice(list(items.keys()))

        if chat_id in basket.keys():
            del basket[chat_id]

        add(MockBot, item, chat_id)

        delete(MockBot, item, chat_id)
        assert chat_id not in list(basket.keys())


    '''def test_show_basket(self):
        item = choice(list(items.keys()))

        if chat_id in basket.keys():
            del basket[chat_id]

        add(MockBot, item, chat_id)

        assert show_basket(MockBot, chat_id) != ('' or 'Your basket is empty :(')'''


    '''def test_show_empty_basket(self):
        if chat_id in basket.keys():
            del basket[chat_id]

        assert show_basket(MockBot, chat_id) == 'Your basket is empty :('''


    def test_clear_basket(self):
        item = choice(list(items.keys()))

        add(MockBot, item, chat_id)

        clear_bask(MockBot, chat_id)
        assert chat_id not in list(basket.keys())


    def test_place_ordr(self):
        item = choice(list(items.keys()))

        add(MockBot, item, chat_id)

        place_ordr(MockBot, chat_id, MockQuery)
        assert chat_id in orders


    def test_delete_testorders(self):
        del orders[chat_id]
        with open('data/orders.json', 'w') as ord:
            json.dump(orders, ord)
        assert 1 == 1


    '''def test_show_orders(self):
        text = show_orders(MockBot, chat_id)
        assert text == ('' and 'No orders yet')'''


    '''def test_MockBot(self):
        assert MockBot.send_message(chat_id) == 'Nah'''
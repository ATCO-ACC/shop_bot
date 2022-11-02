# shop_bot
Bot that runs your own Telegram shop.
Telegram token is missing for safety purposes. 
Token is to be removed from 'main.py' file later, so it is not easily accessible by other people.
Environment variables may be used to solve this issue.

What can it do?
- Create a catalogue from all your existing items
- Manage customers' basket and orders(not yet)
- Receive orders, shipping information(not yet) and payments(not yet)
- Let you to manage your shop from your own private administrator menu

What can users do with it?
- View items from shop catalogue with description and pictures
- Add or delete items from their baskets
- Empty their basket or place an order
- View their orders(not quite yet)
- View shop owner's contacts

What it consists of:
- 'data' directory, which comprises a few 'json' files, including 'basket' (existing caustomer baskets), 'items' (dictionary with your items), 
  'orders' (customers' orders), 'admins' (all administrators, who have rights to run your shop)
- 'images' directory, which contains photos for each item
- 'functions.py' contains functions, which are used in 'main.py'
- 'menus.py' includes inline keyboard markups for so-called menus in your shop
- 'requirements.txt' comprises requirements to be installed on start-up

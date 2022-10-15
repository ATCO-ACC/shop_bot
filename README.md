# shop_bot
Bot that runs your own Telegram shop.

What can it do?
- Create a catalogue from all your existing items
- Manage customers' basket and orders(not yet)
- Receive orders, shipping information(not yet) and payments(not yet)
- Let you to manage your shop from your own private administrator menu

What it consists of:
- 'data' directory, which comprises a few 'json' files, including 'basket' (existing caustomer baskets), 'items' (dictionary with your items), 
  'orders' (customers' orders), 'admins' (all administrators, who have rights to run your shop)
- 'images' directory, which contains photos for each item
- 'functions.py' contains functions, which are used in 'main.py'
- 'menus.py' includes inline keyboard markups for so-called menus in your shop
- 'requirements.txt' comprises requirements to be installed on start-up

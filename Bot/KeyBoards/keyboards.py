from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from Lexicon.lexicon import LEXICON_KEYBOARD

show_products = KeyboardButton(text=LEXICON_KEYBOARD['show_products'])
make_order= KeyboardButton(text=LEXICON_KEYBOARD['make_order'])
connect_with_seller = KeyboardButton(text=LEXICON_KEYBOARD['connect_with_seller'])

change_product = KeyboardButton(text=LEXICON_KEYBOARD['change_product'])
add_product = KeyboardButton(text=LEXICON_KEYBOARD['add_product'])
delete_product = KeyboardButton(text=LEXICON_KEYBOARD['delete_product'])
show_orders = KeyboardButton(text=LEXICON_KEYBOARD['show_orders'])
exit_button = KeyboardButton(text=LEXICON_KEYBOARD['exit'])

edit_name = KeyboardButton(text=LEXICON_KEYBOARD['edit_name'])
edit_description = KeyboardButton(text=LEXICON_KEYBOARD['edit_description'])
edit_price = KeyboardButton(text=LEXICON_KEYBOARD['edit_price'])


cancel = KeyboardButton(text=LEXICON_KEYBOARD['cancel'])
save = KeyboardButton(text=LEXICON_KEYBOARD['save'])

empty_keyboard = ReplyKeyboardRemove()

main_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            show_products, 
            make_order,
            connect_with_seller
        ]
    ],
    resize_keyboard=True
)

admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            show_products, 
            change_product,
            add_product,
            show_orders,
            exit_button
        ]
    ],
    resize_keyboard=True
)

edit_product_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            edit_name, 
            edit_description,
            edit_price,
            delete_product,
            cancel
        ]
    ],
    resize_keyboard=True
)

save_or_cancel_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            save,
            cancel
        ]
    ],
    resize_keyboard=True
)

cancel_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            cancel
        ]
    ],
    resize_keyboard=True
)



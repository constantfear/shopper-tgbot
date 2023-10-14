from aiogram.filters import StateFilter
from aiogram.filters.state import State, StatesGroup

class ShowProducts(StatesGroup):
    choose_course = State()
    fill_course = State()
    fill_price_item = State()
    fill_amount_item = State()
    choose_mode =  State()

class SellerConnection(StatesGroup):
    get_phone =  State()

class Admin(StatesGroup):
    main_menu = State()
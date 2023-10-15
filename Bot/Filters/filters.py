from aiogram.filters import StateFilter
from aiogram.filters.state import State, StatesGroup

class ShowProducts(StatesGroup):
    enter_type = State()

class SellerConnection(StatesGroup):
    get_phone =  State()

class Admin(StatesGroup):
    main_menu = State()
    enter_type = State()

class AddProduct(StatesGroup):
    enter_type = State()
    enter_name = State()
    enter_description = State()
    enter_price = State()
    save_product = State()
    

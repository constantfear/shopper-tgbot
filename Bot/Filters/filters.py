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

class ChangeProduct(StatesGroup):
    enter_product_id = State()
    enter_setting = State()
    enter_new_name = State()
    enter_new_description = State()
    enter_new_price = State()
    delete_product = State()
    save_changes = State()

class MakeOrder(StatesGroup):
    make_order_panel = State()
    enter_product_id = State()
    enter_product_amount = State()
    save_order = State() 
    enter_phone = State()
    enter_address = State()

class ShowOrder(StatesGroup):
    show_orders = State()
    enter_order_id = State()
    change_order_status = State()
    show_order_products = State()

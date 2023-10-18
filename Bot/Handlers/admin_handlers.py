from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import admin_panel, main_panel, empty_keyboard, show_orders_panel, cancel_panel, change_order_status_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import Admin, AddProduct, ChangeProduct, ShowOrder
import Functions.functions as func
from Database.products import get_types, get_products_by_type
from Database.orders import get_orders, get_order_list, change_status

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['show_products'], StateFilter(Admin.main_menu))
async def show_products(message: Message, state: FSMContext):
    product_types = get_types()
    msg = LEXICON_MESSAGE['add_product_type']+''.join([str(row[0])+'. '+row[1]+'\n' for row in product_types])
    await message.answer(text = msg, parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(Admin.enter_type)

@router.message(StateFilter(Admin.enter_type))
async def proc_start_command(message: Message, state: FSMContext):
    product_type = int(message.text)
    products = get_products_by_type(product_type)
    msg = ''.join([str(row) for row in products])
    if msg != '':
        await message.answer(text = msg, parse_mode='HTML', reply_markup=admin_panel)
    else:
        await message.answer(text = LEXICON_MESSAGE['empty_products'], parse_mode='HTML', reply_markup=admin_panel)
    await state.set_state(Admin.main_menu)
    



@router.message(F.text == LEXICON_KEYBOARD['change_product'], StateFilter(Admin.main_menu))
async def change_product(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['change_product'], parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(ChangeProduct.enter_product_id)

@router.message(F.text == LEXICON_KEYBOARD['add_product'], StateFilter(Admin.main_menu))
async def add_product(message: Message, state: FSMContext):
    product_types = get_types()
    msg = LEXICON_MESSAGE['add_product_type']+''.join([str(row)+'\n' for row in product_types])
    await message.answer(text = msg, parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(AddProduct.enter_type)

@router.message(F.text == LEXICON_KEYBOARD['show_orders'], StateFilter(Admin.main_menu))
async def show_orders(message: Message, state: FSMContext):
    orders = get_orders()
    msg = LEXICON_MESSAGE['add_product_type']+'\n'.join([str(row)+'\n' for row in orders])
    await message.answer(text = msg, parse_mode='HTML', reply_markup=show_orders_panel)
    await state.set_state(ShowOrder.show_orders)



@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(ShowOrder.show_orders))
async def show_orders(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['cancel'], parse_mode='HTML', reply_markup=admin_panel)
    await state.clear()
    await state.set_state(Admin.main_menu)

@router.message(F.text == LEXICON_KEYBOARD['show_order_list'], StateFilter(ShowOrder.show_orders))
async def show_orders(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['add_product_type'], parse_mode='HTML', reply_markup=cancel_panel)
    await state.set_state(ShowOrder.enter_order_id)



@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(ShowOrder.enter_order_id))
async def show_orders(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_MESSAGE['cancel'], reply_markup=show_orders_panel)
    await state.clear()
    await state.set_state(ShowOrder.show_orders)
    
@router.message(StateFilter(ShowOrder.enter_order_id))
async def proc_start_command(message: Message, state: FSMContext):
    order_id = int(message.text)
    order_list = get_order_list(order_id)
    await state.update_data(order_id = order_id)
    p = '\n'.join([str(row)+'\n' for row in order_list])
    if p:
        msg = LEXICON_MESSAGE['found_product']+p
        await message.answer(text = msg, parse_mode='HTML', reply_markup=change_order_status_panel)
        await state.set_state(ShowOrder.change_order_status)
    else:
        await message.answer(text=LEXICON_MESSAGE['error'], reply_markup=show_orders_panel)
        await state.set_state(ShowOrder.show_orders)

@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(ShowOrder.change_order_status))
async def show_orders(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['cancel'], parse_mode='HTML', reply_markup=admin_panel)
    await state.clear()
    await state.set_state(Admin.main_menu)

@router.message(F.text == LEXICON_KEYBOARD['change_order_status'], StateFilter(ShowOrder.change_order_status))
async def show_orders(message: Message, state: FSMContext):
    try: 
        order = await state.get_data()
        change_status(order['order_id'])
        await message.answer(text = 'changed', parse_mode='HTML', reply_markup=admin_panel)
    except:
        await message.answer(text=LEXICON_MESSAGE['error'], reply_markup=admin_panel)
    await state.clear()
    await state.set_state(Admin.main_menu)



@router.message(F.text == LEXICON_KEYBOARD['exit'], StateFilter(Admin.main_menu))
async def exit_admin(message: Message, state: FSMContext):
    await message.answer(text = 'exit', parse_mode='HTML', reply_markup=main_panel)
    await state.clear()


    

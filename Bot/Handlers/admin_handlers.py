from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import admin_panel, main_panel, empty_keyboard
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import Admin, AddProduct, ChangeProduct
import Functions.functions as func
from Database.products import get_types, get_products_by_type
from Database.connection_to_database import engine

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['show_products'], StateFilter(Admin.main_menu))
async def show_products(message: Message, state: FSMContext):
    product_types = get_types(engine)
    msg = LEXICON_MESSAGE['add_product_type']+''.join([str(row[0])+'. '+row[1]+'\n' for row in product_types])
    await message.answer(text = msg, parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(Admin.enter_type)

@router.message(StateFilter(Admin.enter_type))
async def proc_start_command(message: Message, state: FSMContext):
    product_type = int(message.text)
    products = get_products_by_type(engine, product_type)
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
    product_types = get_types(engine)
    msg = LEXICON_MESSAGE['add_product_type']+''.join([str(row[0])+'. '+row[1]+'\n' for row in product_types])
    await message.answer(text = msg, parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(AddProduct.enter_type)

@router.message(F.text == LEXICON_KEYBOARD['show_orders'], StateFilter(Admin.main_menu))
async def show_orders(message: Message):
    await message.answer(text = 'show_orders', parse_mode='HTML', reply_markup=admin_panel)

@router.message(F.text == LEXICON_KEYBOARD['exit'], StateFilter(Admin.main_menu))
async def exit_admin(message: Message, state: FSMContext):
    await message.answer(text = 'exit', parse_mode='HTML', reply_markup=main_panel)
    await state.clear()


    

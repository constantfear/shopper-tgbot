from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import main_panel, empty_keyboard, cancel_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
import Functions.functions as func
from Filters.filters import ShowProducts
from Database.connection_to_database import engine
from Database.products import get_types, get_products_by_type

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['show_products'], StateFilter(default_state))
async def proc_start_command(message: Message, state: FSMContext):
    product_types = get_types(engine)
    msg = LEXICON_MESSAGE['add_product_type']+''.join([str(row[0])+'. '+row[1]+'\n' for row in product_types])
    await message.answer(text = msg, parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(ShowProducts.enter_type)

@router.message(StateFilter(ShowProducts.enter_type))
async def proc_start_command(message: Message, state: FSMContext):
    product_type = int(message.text)
    products = get_products_by_type(engine, product_type)
    msg = ''.join([str(row) for row in products])
    if msg != '':
        await message.answer(text = msg, parse_mode='HTML', reply_markup=main_panel)
    else:
        await message.answer(text = LEXICON_MESSAGE['empty_products'], parse_mode='HTML', reply_markup=main_panel)
    await state.clear()
    




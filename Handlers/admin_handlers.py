from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import admin_panel, main_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import Admin
import Functions.functions as func

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['show_products'], StateFilter(Admin.main_menu))
async def proc_start_command(message: Message):
    await message.answer(text = 'admin_show_product', parse_mode='HTML', reply_markup=admin_panel)
    
@router.message(F.text == LEXICON_KEYBOARD['change_product'], StateFilter(Admin.main_menu))
async def proc_start_command(message: Message):
    await message.answer(text = 'change_product', parse_mode='HTML', reply_markup=admin_panel)
    
@router.message(F.text == LEXICON_KEYBOARD['delete_product'], StateFilter(Admin.main_menu))
async def proc_start_command(message: Message):
    await message.answer(text = 'delete_product', parse_mode='HTML', reply_markup=admin_panel)

@router.message(F.text == LEXICON_KEYBOARD['show_orders'], StateFilter(Admin.main_menu))
async def proc_start_command(message: Message):
    await message.answer(text = 'show_orders', parse_mode='HTML', reply_markup=admin_panel)

@router.message(F.text == LEXICON_KEYBOARD['exit'], StateFilter(Admin.main_menu))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = 'exit', parse_mode='HTML', reply_markup=main_panel)
    await state.clear()


    

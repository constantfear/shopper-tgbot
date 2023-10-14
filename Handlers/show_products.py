from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import main_panel, empty_keyboard, cancel_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
import Functions.functions as func

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['show_products'], StateFilter(default_state))
async def proc_start_command(message: Message):
    await message.answer(text = LEXICON_MESSAGE['show_products'], parse_mode='HTML', reply_markup=main_panel)




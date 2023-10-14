from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import main_panel, admin_panel
from Lexicon.lexicon import LEXICON_MESSAGE
from Filters.filters import Admin

config = make_config()

router = Router()


@router.message(F.text == '/start', StateFilter(default_state))
async def start_command(message: Message):
    await message.answer(text = LEXICON_MESSAGE['start'], parse_mode='HTML', reply_markup=main_panel)

@router.message(F.text == '/help', StateFilter(default_state))
async def help_command(message: Message):
    await message.answer(text = LEXICON_MESSAGE['help'], parse_mode='HTML', reply_markup=main_panel)

@router.message(((F.text == '/admin_panel') & (F.from_user.id==config.tg_bot.admin_id)), StateFilter(default_state))
async def admin_command(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['admin_panel'], parse_mode='HTML', reply_markup=admin_panel)
    await state.set_state(Admin.main_menu)


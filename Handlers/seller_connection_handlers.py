from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import main_panel, cancel_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import SellerConnection
import Functions.functions as func

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['connect_with_seller'], StateFilter(default_state))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['connect_with_seller_phone'], parse_mode='HTML', reply_markup=cancel_panel)
    await state.set_state(SellerConnection.get_phone)


@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(SellerConnection.get_phone))
async def proc_start_command(message: Message, bot: Bot, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['cancel'], parse_mode='HTML', reply_markup=main_panel)
    await state.clear()


@router.message(StateFilter(SellerConnection.get_phone))
async def proc_start_command(message: Message, bot: Bot, state: FSMContext):
    if func.is_valid_phone_number(message.text):
        await bot.send_message(config.tg_bot.seller_id, text=f"Пользователь {message.from_user.first_name} {message.from_user.last_name} хочет связаться с вами.\nНомер телефона для связи: {message.text}")
        await message.answer(text = LEXICON_MESSAGE['connect_with_seller'], parse_mode='HTML', reply_markup=main_panel)
        await state.clear()
    else:
        await message.answer(text = LEXICON_MESSAGE['error_try_again'], parse_mode='HTML', reply_markup=cancel_panel)
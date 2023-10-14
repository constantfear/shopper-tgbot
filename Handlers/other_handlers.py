from aiogram import Router
from aiogram.types import Message

from Lexicon.lexicon import LEXICON_MESSAGE

router = Router()


@router.message()
async def proc_start_command(message: Message):
    await message.answer(text = LEXICON_MESSAGE['other'], parse_mode='HTML')

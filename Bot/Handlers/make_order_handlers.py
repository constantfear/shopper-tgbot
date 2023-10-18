from aiogram import F, Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import main_panel, empty_keyboard, cancel_panel, make_order, save_or_cancel_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import MakeOrder
import Functions.functions as func
import Database.products as prod
import Database.orders as ord 

config = make_config()

router = Router()


@router.message(F.text == LEXICON_KEYBOARD['make_order'], StateFilter(default_state))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['make_order'], parse_mode='HTML', reply_markup=make_order)
    await state.update_data(order = dict())
    await state.set_state(MakeOrder.make_order_panel)

@router.message(F.text == LEXICON_KEYBOARD['add_product_to_order'], StateFilter(MakeOrder.make_order_panel))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = 'add_product_to_order', parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(MakeOrder.enter_product_id)

@router.message(StateFilter(MakeOrder.enter_product_id))
async def proc_start_command(message: Message, state: FSMContext):
    product_id = int(message.text)
    product = prod.get_product_by_id(product_id)
    await state.update_data(product_id = product_id)
    p = ''.join([str(row[0])+'. '+row[1]+'\n' for row in product])
    if p:
        msg = LEXICON_MESSAGE['found_product']+p+'\nВведите кол-во'
        await message.answer(text = msg, parse_mode='HTML', reply_markup=cancel_panel)
        await state.set_state(MakeOrder.enter_product_amount)
    else:
        await message.answer(text=LEXICON_MESSAGE['error'], reply_markup=make_order)
        await state.set_state(MakeOrder.make_order_panel)


@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(MakeOrder.enter_product_amount))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = 'cancel', parse_mode='HTML', reply_markup=make_order)
    await state.set_state(MakeOrder.make_order_panel)

@router.message(StateFilter(MakeOrder.enter_product_amount))
async def proc_start_command(message: Message, state: FSMContext):
    try:
        product_amount = int(message.text)
        data = await state.get_data()
        data['order'][data['product_id']] = product_amount
        msg = 'added'
        print(data['order'])
        await message.answer(text = msg, parse_mode='HTML', reply_markup=make_order)
        await state.set_state(MakeOrder.make_order_panel)
    except:
        await message.answer(text=LEXICON_MESSAGE['error'], reply_markup=make_order)
        await state.set_state(MakeOrder.make_order_panel)


@router.message(F.text == LEXICON_KEYBOARD['save_order'], StateFilter(MakeOrder.make_order_panel))
async def proc_start_command(message: Message, state: FSMContext):
    product_data = await state.get_data()
    if len(product_data['order']) > 0:
        await message.answer(text = 'save_order', parse_mode='HTML', reply_markup=cancel_panel)
        await state.set_state(MakeOrder.enter_phone)
    else:
        await message.answer(text = 'not enough', parse_mode='HTML', reply_markup=make_order)

@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(MakeOrder.enter_phone))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = 'cancel', parse_mode='HTML', reply_markup=make_order)
    await state.set_state(MakeOrder.make_order_panel)

@router.message(StateFilter(MakeOrder.enter_phone))
async def proc_start_command(message: Message, state: FSMContext):
    if func.is_valid_phone_number(message.text):
        await state.update_data(phone = message.text)
        await message.answer(text = 'enter addres', parse_mode='HTML', reply_markup=cancel_panel)
        await state.set_state(MakeOrder.enter_address)
    else:
        await message.answer(text = LEXICON_MESSAGE['error_try_again'], parse_mode='HTML', reply_markup=cancel_panel)


@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(MakeOrder.enter_address))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = 'cancel', parse_mode='HTML', reply_markup=make_order)
    await state.set_state(MakeOrder.make_order_panel)

@router.message(StateFilter(MakeOrder.enter_address))
async def proc_start_command(message: Message, state: FSMContext):
    await state.update_data(addres = message.text)
    await message.answer(text = 'save?', parse_mode='HTML', reply_markup=save_or_cancel_panel)
    await state.set_state(MakeOrder.save_order)


@router.message(F.text == LEXICON_KEYBOARD['save'], StateFilter(MakeOrder.save_order))
async def save_product(message: Message, state: FSMContext, bot: Bot):
    product_data = await state.get_data()
    try:
        ord.insert_order(message.from_user.id, product_data['order'], product_data['phone'], product_data['addres'])
        await bot.send_message(config.tg_bot.seller_id, text='New Order!')
        await message.answer(text = LEXICON_MESSAGE['added'], parse_mode='HTML', reply_markup=main_panel)

        await state.clear()
    except Exception as ex:
        print(ex)
        await message.answer(text = LEXICON_MESSAGE['error'], parse_mode='HTML', reply_markup=make_order)
        await state.set_state(MakeOrder.make_order_panel)


@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(MakeOrder.save_order))
async def save_product(message: Message, state: FSMContext):
    await message.answer(text = 'cancel', parse_mode='HTML', reply_markup=make_order)
    await state.set_state(MakeOrder.make_order_panel)


@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(MakeOrder.make_order_panel))
async def proc_start_command(message: Message, state: FSMContext):
    await message.answer(text = 'cancel', parse_mode='HTML', reply_markup=main_panel)
    await state.clear()


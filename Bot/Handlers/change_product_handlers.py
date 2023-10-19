from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import admin_panel, empty_keyboard, edit_product_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import Admin, ChangeProduct
import Functions.functions as func
import Database.products as prod



router = Router()


@router.message(StateFilter(ChangeProduct.enter_product_id))
async def show_products(message: Message, state: FSMContext):
    product_id = int(message.text)
    await state.update_data(product_id=product_id)
    product = prod.get_product_by_id(product_id)
    p = ''.join([str(row[0])+'. '+row[1]+'\n' for row in product])
    if p:
        msg = LEXICON_MESSAGE['found_product']+p
        await message.answer(text = msg, parse_mode='HTML', reply_markup=edit_product_panel)
        await state.set_state(ChangeProduct.enter_setting)
    else:
        await message.answer(text=LEXICON_MESSAGE['error'], reply_markup=admin_panel)
        await state.set_state(Admin.main_menu)


@router.message(F.text == LEXICON_KEYBOARD['edit_name'], StateFilter(ChangeProduct.enter_setting))
async def change_product(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['change_product_name'], parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(ChangeProduct.enter_new_name)

@router.message(StateFilter(ChangeProduct.enter_new_name))
async def show_products(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        prod.update_product_name(data['product_id'], message.text)
        await message.answer(text = LEXICON_MESSAGE['changed'], parse_mode='HTML', reply_markup=admin_panel)
    except:
        await message.answer(text=LEXICON_MESSAGE['error'])
    await state.clear()
    await state.set_state(Admin.main_menu)

@router.message(F.text == LEXICON_KEYBOARD['edit_description'], StateFilter(ChangeProduct.enter_setting))
async def change_product(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['change_product_description'], parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(ChangeProduct.enter_new_description)

@router.message(StateFilter(ChangeProduct.enter_new_description))
async def show_products(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        prod.update_product_description(data['product_id'], message.text)
        await message.answer(text = LEXICON_MESSAGE['changed'], parse_mode='HTML', reply_markup=admin_panel)
    except Exception as ex:
        await message.answer(text=LEXICON_MESSAGE['error'], parse_mode='HTML', reply_markup=admin_panel)
        # await message.answer(text=str(ex))
    await state.clear()
    await state.set_state(Admin.main_menu)

@router.message(F.text == LEXICON_KEYBOARD['edit_price'], StateFilter(ChangeProduct.enter_setting))
async def change_product(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['change_product_price'], parse_mode='HTML', reply_markup=empty_keyboard)
    await state.set_state(ChangeProduct.enter_new_price)

@router.message(StateFilter(ChangeProduct.enter_new_price))
async def show_products(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        prod.update_product_price(data['product_id'], int(message.text))
        await message.answer(text = LEXICON_MESSAGE['changed'], parse_mode='HTML', reply_markup=admin_panel)
    except:
        await message.answer(text=LEXICON_MESSAGE['error'])
    await state.clear()
    await state.set_state(Admin.main_menu)

@router.message(F.text == LEXICON_KEYBOARD['delete_product'], StateFilter(ChangeProduct.enter_setting))
async def change_product(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        prod.delete_product(data['product_id'])
        await message.answer(text = LEXICON_MESSAGE['delete_product'], parse_mode='HTML', reply_markup=admin_panel)
    except:
        await message.answer(text=LEXICON_MESSAGE['error'])
    await state.clear()
    await state.set_state(Admin.main_menu)
    

@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(ChangeProduct.enter_setting))
async def change_product(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['cancel'], parse_mode='HTML', reply_markup=admin_panel)
    await state.set_state(Admin.main_menu)



    

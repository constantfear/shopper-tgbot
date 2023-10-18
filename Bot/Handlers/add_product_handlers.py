from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from Configs.config import make_config
from KeyBoards.keyboards import admin_panel, save_or_cancel_panel
from Lexicon.lexicon import LEXICON_MESSAGE, LEXICON_KEYBOARD
from Filters.filters import Admin, AddProduct
import Functions.functions as func
from Database.products import add_products

config = make_config()

router = Router()


@router.message(StateFilter(AddProduct.enter_type))
async def enter_Type(message: Message, state: FSMContext):
    await state.update_data(product_type = int(message.text))
    await message.answer(text = LEXICON_MESSAGE['add_product_name'], parse_mode='HTML')
    await state.set_state(AddProduct.enter_name)

@router.message(StateFilter(AddProduct.enter_name))
async def enter_Name(message: Message, state: FSMContext):
    await state.update_data(product_name = message.text)
    await message.answer(text = LEXICON_MESSAGE['add_product_description'], parse_mode='HTML')
    await state.set_state(AddProduct.enter_description)

@router.message(StateFilter(AddProduct.enter_description))
async def enter_Description(message: Message, state: FSMContext):
    await state.update_data(product_description = message.text)
    await message.answer(text = LEXICON_MESSAGE['add_product_price'], parse_mode='HTML')
    await state.set_state(AddProduct.enter_price)

@router.message(StateFilter(AddProduct.enter_price))
async def enter_Price(message: Message, state: FSMContext):
    await state.update_data(product_price = int(message.text))
    product_data = await state.get_data()
    msg = f"""Проверьте верность:
    Тип: {product_data['product_type']}
    Название: {product_data['product_name']}
    Описание: {product_data['product_description']}
    Цена за единицу товара: {product_data['product_price']}"""
    await message.answer(text = msg, parse_mode='HTML', reply_markup=save_or_cancel_panel)
    await state.set_state(AddProduct.save_product)


@router.message(F.text == LEXICON_KEYBOARD['save'], StateFilter(AddProduct.save_product))
async def save_product(message: Message, state: FSMContext):
    product_data = await state.get_data()
    try:
        add_products(product_data['product_name'], product_data['product_description'], product_data['product_price'], product_data['product_type'])
        await message.answer(text = LEXICON_MESSAGE['added'], parse_mode='HTML', reply_markup=admin_panel)
    except:
        await message.answer(text = LEXICON_MESSAGE['error'], parse_mode='HTML', reply_markup=admin_panel)
    await state.clear()
    await state.set_state(Admin.main_menu)

@router.message(F.text == LEXICON_KEYBOARD['cancel'], StateFilter(AddProduct.save_product))
async def save_product(message: Message, state: FSMContext):
    await message.answer(text = LEXICON_MESSAGE['cancel'], parse_mode='HTML', reply_markup=admin_panel)
    await state.clear()
    await state.set_state(Admin.main_menu)



    

LEXICON_MESSAGE: dict[str, str] = {
    'start': 'Пример бота для небольшого магазина\nВведите /help, чтобы узнать что он может',
    'help': 'Этот бот может: \n -Вывод товаров\n -Оформлять заказ\n -Связаться с продавцом',

    'show_products': 'Вывод товаров',
    'connect_with_seller_phone': 'Введите ваш номер, чтобы продавец мог связаться с вами',
    'connect_with_seller': 'Продавцу отправлено уведомление, что вы хотели с ним связаться',
    'make_order':'Оформление заказа',

    'admin_panel': 'Переходим в панель администрирования',

    'add_product_type': 'Выберите номер типа продукта:\n',
    'add_product_name': 'Введите название продукта',
    'add_product_description': 'Напишите небольшое описание для продукта',
    'add_product_price': 'Введите цену за единицу товара',
    'added': 'Товар добавлен',

    'change_product': 'Введите id товара',
    'change_product_name': 'Введите новое название товара',
    'change_product_description': 'Введите новое описание товара',
    'change_product_price': 'Введите новую цену товара',
    'delete_product': 'Товар удален',
    'changed': 'Изменения сохранены',
    'found_product': 'Найден продукт',


    'add_product_to_order': 'Введите id товара, который вы хотите добавить к заказу',
    'save_order_phone': 'Введите ваш номер ',
    'save_order_addres': 'Введите ваш адрес для доставки',
    'save_order': 'Все верно?',
    'get_order_id': 'Введите id заказа',
    'new_order': 'Заказ сохранен',
    'order_empty': 'Заказ пуст!',
    'added_to_order': 'Товар добавлен к заказу',
    'new_order_for_seller': 'Новый заказ!',
    'found_product': 'Найден продукт',
    'changed_order_status': 'Статус заказа изменен на "Доставлено"',

    'error_try_again': 'Произошла ошибка! попробуйте еще раз',
    'exit': 'Выходим',    
    'cancel': 'Возвращаемся назад',
    'other': "Неизвестная команда",
    'error': 'Произошла ошибка',
    'empty_products': 'Товаров данного типа нет'
}


LEXICON_KEYBOARD: dict[str, str] = {
    'show_products': 'Показать товары',
    'make_order': 'Сделать заказ',    
    'connect_with_seller': 'Связаться с продавцом',
    'show_my_orders': 'Посмотреть список моих заказов',
    'cancel': 'Отмена',
    'change_product' : 'Редактировать товар',
    'add_product': 'Добавить продукт',
    'delete_product': 'Удалить товар',
    'show_orders': 'Посмотреть список заказов',
    'exit': 'Выйти из панели управления',
    'save': 'Сохранить',

    'edit_name': 'Редактировать название',
    'edit_description': 'Редактировать описание',
    'edit_price': 'Редактировать цену',

    'add_product_to_order': 'Добавить товар',
    'save_order': 'Сохранить заказ',

    'show_order_list': 'Вывести товары в заказе',
    'change_order_status': 'Изменить статус заказа',

}

PRODUCT_HEADER = ['Id', 'Название', 'Описание', 'Цена', 'Тип товара']

ORDER_HEADER = ['Id', 'User td Id', 'Дата заказа', 'Телефон', 'Адрес', 'Статус']

ORDER_LIST_HEADER = ['Название товара', 'Кол-во', 'Стоимость']


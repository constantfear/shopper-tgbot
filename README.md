# Shopper-TGbot

Welcome to Shopper-TGbot, your Telegram assistant. Our bot is designed so that you can make your store more modern and convenient for users!

## Key Features

- **Customer Interaction**: Our bot is equipped with functions to ensure customer interaction with the store.

- **Customers and seller**: After reviewing the goods, the customer can place an order and the seller will receive a message about it. Also, if you have any questions, you can leave a request to the seller, and later he will contact the client

- **Easy Integration**: Seamless integration with your Telegram app means you can use our bot without any hassle.


## Table of Contents

- [Running the Bot](#running-the-bot)
- [Project Structure](#project-structure)
- [Used Libraries](#used-libraries)
- [License](#license)

## Running the Bot

### Requirements

Before starting the bot, make sure that the following components are installed on your computer:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Bot Configuration
1. Register your bot with Telegram and obtain an API token.
2. Get your Id and Seller Id
3. In the **'Bot/example.env'** file, replace **'Your Token'**, **'ADMIN_ID'**, **'SELLER_ID'** with your data 

### Starting the Bot
Start the bot by running:
```bash 
docker-compose up --build
```
Your bot is now active and ready for use!

## Project Structure

```arduino
shopper-tgbot/
    ├── Bot/
    │   ├── bot.py
    │   ├── Configs/
    │   │   └── config.py
    │   ├── Database/
    │   │   ├── connection_to_database.py
    │   │   ├── orders.py
    │   │   └── products.py
    │   ├── Dockerfile
    │   ├── .env    
    │   ├── Filters/
    │   │   └── filters.py
    │   ├── Functions/
    │   │   └── functions.py
    │   ├── Handlers/
    │   │   ├── add_product_handlers.py
    │   │   ├── admin_handlers.py
    │   │   ├── change_product_handlers.py
    │   │   ├── comand_handlers.py
    │   │   ├── __init__.py
    │   │   ├── make_order_handlers.py
    │   │   ├── other_handlers.py
    │   │   ├── seller_connection_handlers.py
    │   │   └── show_products.py
    │   ├── KeyBoards/
    │   │   └── keyboards.py
    │   ├── Lexicon/
    │   │   └── lexicon.py
    │   └── requirements.txt
    ├── db-create/
    │   └── create_tables.sql
    └── docker-compose.yaml
```

## Used Libraries
- [Aiogram](https://docs.aiogram.dev/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## License
This project is licensed under the MIT License.
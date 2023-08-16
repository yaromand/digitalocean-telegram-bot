from os import environ

from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot

bot_name = environ.get('bot_name', 'RozetkaMarket')


def start(d: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(
            text='Добавить аккаунт',
            callback_data='add_account'
        ),
        InlineKeyboardButton(
            text='Управлять аккаунтами',
            callback_data='manage_accounts'
        ),
        InlineKeyboardButton(
            text='Создать каплю',
            callback_data='create_droplet'
        ),
        InlineKeyboardButton(
            text='Управлять каплями',
            callback_data='manage_droplets'
        ),
    )
    t = f'Добро пожаловать <b>{bot_name}</b>\n\n' \
        'Тут вы можете управлять учетными записями DigitalOcean \n\n'

    bot.send_message(
        text=t,
        chat_id=d.from_user.id,
        parse_mode='HTML',
        reply_markup=markup
    )

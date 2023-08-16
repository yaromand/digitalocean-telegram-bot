from telebot.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

import digitalocean
from digitalocean import DataReadError

from _bot import bot
from utils.db import AccountsDB


def account_detail(call: CallbackQuery, data: dict):
    doc_id = data['doc_id'][0]
    t = '<b>Информация о аккаунте:</b>\n\n'

    account = AccountsDB().get(doc_id=doc_id)

    msg = bot.send_message(
        text=f'{t}'
             f'Почта： <code>{account["email"]}</code>\n\n'
             f'Загружаю информацию...',
        chat_id=call.from_user.id,
        parse_mode='HTML'
    )

    t += f'Почта： <code>{account["email"]}</code>\n' \
         f'Примечание： <code>{account["remarks"]}</code>\n' \
         f'Добавлен： <code>{account["date"]}</code>\n' \
         f'Token： <code>{account["token"]}</code>\n\n'
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text='Удалить',
            callback_data=f'delete_account?doc_id={account.doc_id}'
        )
    )

    try:
        account_balance = digitalocean.Balance().get_object(api_token=account['token'])
        droplet_limi = digitalocean.Account().get_object(api_token=account['token'])
        droplets = digitalocean.Manager(token=account['token']).get_all_droplets()
        t += f'Баланс： <code>{account_balance.account_balance}</code>\n' \
             f'Использовано： <code>{account_balance.month_to_date_usage}</code>\n' \
             f'Лимит： <code>{len(droplets)} из {droplet_limi.droplet_limit}</code>\n' \
             f'Дата выставление： <code>{account_balance.generated_at.split("T")[0]}</code>'

    except DataReadError as e:
        t += f'Отчет об ошибке： <code>{e}</code>'

    bot.edit_message_text(
        text=t,
        chat_id=call.from_user.id,
        message_id=msg.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )

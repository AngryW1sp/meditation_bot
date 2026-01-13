from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_choise():
    kb = InlineKeyboardBuilder()
    kb.button(text="Медитации", callback_data="admin_meditaion")
    kb.button(text="Аффирмации", callback_data="admin_affer")
    kb.button(text="Советы", callback_data="admin_recommend")
    kb.button(text="Добавить +", callback_data="admin_add")
    kb.adjust(1)
    return kb.as_markup()


def 
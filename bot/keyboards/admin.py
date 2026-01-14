from aiogram.utils.keyboard import InlineKeyboardBuilder



def admin_choise():
    kb = InlineKeyboardBuilder()
    kb.button(text="Медитации", callback_data="admin:meditations")
    kb.button(text="Аффирмации", callback_data="admin:affirmations")
    kb.button(text="Советы", callback_data="admin:tips")
    kb.adjust(1)
    return kb.as_markup()

def admin_section_kb(section: str):
    kb = InlineKeyboardBuilder()
    kb.button(text="Список", callback_data=f"admin:{section}:list")
    kb.button(text="Добавить", callback_data=f"admin:{section}:add")
    kb.button(text="Назад", callback_data="admin:back")
    kb.adjust(1)
    return kb.as_markup()



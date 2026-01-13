from aiogram.fsm.state import State, StatesGroup

class AdminStates(StatesGroup):
    add_med_time = State()
    add_med_link = State()
    add_med_desc = State()

    add_text = State()

    edit_med_time = State()
    edit_med_link = State()
    edit_med_desc = State()

    edit_text = State()
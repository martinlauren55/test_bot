from aiogram import types


def get_keyboard():
    # Генерация клавиатуры для timezone
    buttons = [
        types.InlineKeyboardButton(text="±00:00", callback_data="tz_+00:00"),
        types.InlineKeyboardButton(text="+01:00", callback_data="tz_+01:00"),
        types.InlineKeyboardButton(text="+02:00", callback_data="tz_+02:00"),
        types.InlineKeyboardButton(text="+03:00", callback_data="tz_+03:00"),
        types.InlineKeyboardButton(text="+03:30", callback_data="tz_+03:30"),
        types.InlineKeyboardButton(text="+04:00", callback_data="tz_+04:00"),
        types.InlineKeyboardButton(text="+04:30", callback_data="tz_+04:30"),
        types.InlineKeyboardButton(text="+05:00", callback_data="tz_+05:00"),
        types.InlineKeyboardButton(text="+05:30", callback_data="tz_+05:30"),
        types.InlineKeyboardButton(text="+05:45", callback_data="tz_+05:45"),
        types.InlineKeyboardButton(text="+06:00", callback_data="tz_+06:00"),
        types.InlineKeyboardButton(text="+06:30", callback_data="tz_+06:30"),
        types.InlineKeyboardButton(text="+08:00", callback_data="tz_+08:00"),
        types.InlineKeyboardButton(text="+08:45", callback_data="tz_+08:45"),
        types.InlineKeyboardButton(text="+09:00", callback_data="tz_+09:00"),
        types.InlineKeyboardButton(text="+09:30", callback_data="tz_+09:30"),
        types.InlineKeyboardButton(text="+10:00", callback_data="tz_+10:00"),
        types.InlineKeyboardButton(text="+10:30", callback_data="tz_+10:30"),
        types.InlineKeyboardButton(text="+11:00", callback_data="tz_+11:00"),
        types.InlineKeyboardButton(text="+12:00", callback_data="tz_+12:00"),
        types.InlineKeyboardButton(text="+13:00", callback_data="tz_+13:00"),
        types.InlineKeyboardButton(text="+13:45", callback_data="tz_+13:45"),
        types.InlineKeyboardButton(text="+14:00", callback_data="tz_+14:00"),
        types.InlineKeyboardButton(text="-01:00", callback_data="tz_-01:00"),
        types.InlineKeyboardButton(text="-02:00", callback_data="tz_-02:00"),
        types.InlineKeyboardButton(text="-02:30", callback_data="tz_-02:30"),
        types.InlineKeyboardButton(text="-03:00", callback_data="tz_-03:00"),
        types.InlineKeyboardButton(text="-04:00", callback_data="tz_-04:00"),
        types.InlineKeyboardButton(text="-05:00", callback_data="tz_-05:00"),
        types.InlineKeyboardButton(text="-06:00", callback_data="tz_-06:00"),
        types.InlineKeyboardButton(text="-07:00", callback_data="tz_-07:00"),
        types.InlineKeyboardButton(text="-08:00", callback_data="tz_-08:00"),
        types.InlineKeyboardButton(text="-09:00", callback_data="tz_-09:00"),
        types.InlineKeyboardButton(text="-09:30", callback_data="tz_-09:30"),
        types.InlineKeyboardButton(text="-10:00", callback_data="tz_-10:00"),
        types.InlineKeyboardButton(text="-11:00", callback_data="tz_-11:00"),
        types.InlineKeyboardButton(text="-12:00", callback_data="tz_-12:00"),
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    return keyboard


def get_remind_keyboard():
    # buttons = [
    #     types.InlineKeyboardButton(text="15 Минут", callback_data="remind_15_min"),
    #     types.InlineKeyboardButton(text="30 Минут", callback_data="remind_30_min"),
    #     types.InlineKeyboardButton(text="1 Час", callback_data="remind_60_min"),
    #     types.InlineKeyboardButton(text="Завтра", callback_data="remind_1440_min"),
    # ]
    buttons = [
        types.InlineKeyboardButton(text="+1", callback_data="num_incr1"),
        types.InlineKeyboardButton(text="+5", callback_data="num_incr5"),
        types.InlineKeyboardButton(text="+10", callback_data="num_incr10"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    return keyboard

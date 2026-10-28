from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL, SITE_URL, FORM_URL, VK_URL

# --- ПРОВЕРКА ПОДПИСКИ ---
subscribe_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📢 Открыть канал", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="✅ Я подписан", callback_data="check_sub")]
])

# --- ГЛАВНОЕ МЕНЮ ---
main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤸‍♀️ Об учреждении", callback_data="about")],
    [InlineKeyboardButton(text="📍 Адрес учреждения", callback_data="addresses")],
    [InlineKeyboardButton(text="🏐 Чемпионат России по гандболу (суперлига) 2026/2027", callback_data="champ_menu")],
    [InlineKeyboardButton(text="🏐 Первенство России по гандболу (молодёжка U22) 2026/2027", callback_data="youth_menu")],
    [InlineKeyboardButton(text="💳 Платные услуги", url="http://www.zarya-kaspiya.ru/wp-content/uploads/2026/02/prejskurant-czen-na-okazanie-platnyh-uslug-v-sportivnom-sooruzhenii-dvorecz-sporta-dejstvuet-s-01.01.2026-g-1.pdf")],
    [InlineKeyboardButton(text="🟦 Мы есть в ВКОНТАКТЕ", url=VK_URL)],
    [InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="support_menu")],
    [InlineKeyboardButton(text="📞 Контактная информация", callback_data="contacts")],
    [InlineKeyboardButton(text="💬 Остались вопросы? Напишите нам", url="https://pos.gosuslugi.ru/landing/")],
])

# --- ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ ---
support_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❓ Запись в группу", callback_data="question_1")],
])

# --- КНОПКА "НАЗАД" ДЛЯ ПОДМЕНЮ FAQ ---
back_to_support_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к часто задаваемым вопросам", callback_data="support_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- ЧЕМПИОНАТ РОССИИ (суперлига): МЕСЯЦЫ ---
championship_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Сентябрь 2026",  callback_data="champ_2026_09")],
    [InlineKeyboardButton(text="📅 Октябрь 2026",  callback_data="champ_2026_10")],
    [InlineKeyboardButton(text="📅 Ноябрь 2026",   callback_data="champ_2026_11")],
    [InlineKeyboardButton(text="📅 Декабрь 2026",  callback_data="champ_2026_12")],
    [InlineKeyboardButton(text="📅 Январь 2027",   callback_data="champ_2027_01")],
    [InlineKeyboardButton(text="📅 Февраль 2027",  callback_data="champ_2027_02")],
    [InlineKeyboardButton(text="📅 Март 2027",     callback_data="champ_2027_03")],
    [InlineKeyboardButton(text="⬅️ Назад",         callback_data="back_to_menu")],
])

# --- ПЕРВЕНСТВО РОССИИ (U22): МЕСЯЦЫ ---
youth_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Сентябрь 2026",  callback_data="youth_2026_09")],
    [InlineKeyboardButton(text="📅 Октябрь 2026",  callback_data="youth_2026_10")],
    [InlineKeyboardButton(text="📅 Ноябрь 2026",   callback_data="youth_2026_11")],
    [InlineKeyboardButton(text="📅 Декабрь 2026",  callback_data="youth_2026_12")],
    [InlineKeyboardButton(text="📅 Январь 2027",   callback_data="youth_2027_01")],
    [InlineKeyboardButton(text="📅 Февраль 2027",  callback_data="youth_2027_02")],
    [InlineKeyboardButton(text="📅 Март 2027",     callback_data="youth_2027_03")],
    [InlineKeyboardButton(text="📅 Апрель 2027",   callback_data="youth_2027_04")],
    [InlineKeyboardButton(text="⬅️ Назад",         callback_data="back_to_menu")],
])

# --- КНОПКИ "НАЗАД" ИЗ РАСПИСАНИЯ МЕСЯЦА ---
back_to_champ_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к месяцам", callback_data="champ_menu")],
    [InlineKeyboardButton(text="🏠 На главную",      callback_data="back_to_menu")],
])

back_to_youth_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к месяцам", callback_data="youth_menu")],
    [InlineKeyboardButton(text="🏠 На главную",      callback_data="back_to_menu")],
])

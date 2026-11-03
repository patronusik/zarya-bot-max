from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    CHANNEL_URL, SITE_URL, VK_URL, PRICE_URL, FEEDBACK_URL
)

# --- ПРОВЕРКА ПОДПИСКИ ---
subscribe_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📢 Открыть канал", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="✅ Я подписан", callback_data="check_sub")]
])

# --- ГЛАВНОЕ МЕНЮ ---
main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤾🏻‍♂️ Об учреждении", callback_data="history")],
    [InlineKeyboardButton(text="📍 Адреса учреждения", callback_data="addresses")],
    [InlineKeyboardButton(text="🏆 Чемпионат России (суперлига)", callback_data="champ_menu")],
    [InlineKeyboardButton(text="🏆 Первенство России (молодёжка U22)", callback_data="youth_menu")],
    [InlineKeyboardButton(text="💳 Платные услуги", callback_data="paid_services")],
    [InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="faq_menu")],
    [InlineKeyboardButton(text="📞 Контактная информация", callback_data="contacts")],
    [InlineKeyboardButton(text="🌐 Официальный сайт", url=SITE_URL)],
    [InlineKeyboardButton(text="🟦 Мы есть в ВКонтакте", url=VK_URL)],
    [InlineKeyboardButton(text="💬 Остались вопросы? Напишите нам", url=FEEDBACK_URL)],
])

back_to_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- FAQ ---
faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Запись детей 5–8 лет на гандбол", callback_data="faq_kids")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к вопросам", callback_data="faq_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- ПЛАТНЫЕ УСЛУГИ ---
paid_services_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📄 Открыть прейскурант (PDF)", url=PRICE_URL)],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

# --- ЧЕМПИОНАТ РОССИИ: МЕСЯЦЫ ---
championship_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Сентябрь 2026",  callback_data="champ_2026_09")],
    [InlineKeyboardButton(text="📅 Октябрь 2026",  callback_data="champ_2026_10")],
    [InlineKeyboardButton(text="📅 Ноябрь 2026",   callback_data="champ_2026_11")],
    [InlineKeyboardButton(text="📅 Декабрь 2026",  callback_data="champ_2026_12")],
    [InlineKeyboardButton(text="📅 Январь 2027",   callback_data="champ_2027_01")],
    [InlineKeyboardButton(text="📅 Февраль 2027",  callback_data="champ_2027_02")],
    [InlineKeyboardButton(text="📅 Март 2027",     callback_data="champ_2027_03")],
    [InlineKeyboardButton(text="🏠 На главную",    callback_data="back_to_menu")],
])

back_to_champ_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к месяцам", callback_data="champ_menu")],
    [InlineKeyboardButton(text="🏠 На главную",      callback_data="back_to_menu")],
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
    [InlineKeyboardButton(text="🏠 На главную",    callback_data="back_to_menu")],
])

back_to_youth_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к месяцам", callback_data="youth_menu")],
    [InlineKeyboardButton(text="🏠 На главную",      callback_data="back_to_menu")],
])

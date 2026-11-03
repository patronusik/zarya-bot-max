from config import (
    TEXT_WELCOME, TEXT_NOT_SUBSCRIBED,
    TEXT_HISTORY, TEXT_ADDRESSES, TEXT_PAID_SERVICES,
    TEXT_FAQ_MENU, TEXT_FAQ_KIDS, TEXT_CONTACTS,
    TEXT_CHAMP_MENU, CHAMP_SCHEDULE,
    TEXT_YOUTH_MENU, YOUTH_SCHEDULE,
)
from keyboards import (
    main_menu_kb, back_to_menu_kb, subscribe_kb,
    faq_kb, back_to_faq_kb,
    paid_services_kb,
    championship_menu_kb, back_to_champ_kb,
    youth_menu_kb, back_to_youth_kb,
)
from handlers.start import is_user_subscribed


def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        print(f"CALLBACK: payload={cb.payload} user={getattr(cb, 'user', None)}")

        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (
                cb.user.get("user_id") if isinstance(cb.user, dict) else None
            )
        if user_id is None:
            user_id = getattr(cb, "user_id", None)

        print(f"CALLBACK: resolved user_id={user_id}")

        payload = cb.payload

        # --- ПОДПИСКА ---
        if payload == "check_sub":
            subscribed = await is_user_subscribed(user_id)
            if subscribed:
                await bot.send_message(
                    user_id=user_id,
                    text=TEXT_WELCOME,
                    reply_markup=main_menu_kb,
                    format="markdown"
                )
            else:
                await bot.send_message(
                    user_id=user_id,
                    text=TEXT_NOT_SUBSCRIBED,
                    reply_markup=subscribe_kb
                )
            return

        # --- НА ГЛАВНУЮ (без проверки подписки) ---
        if payload == "back_to_menu":
            await bot.send_message(user_id=user_id, text=TEXT_WELCOME,
                                   reply_markup=main_menu_kb, format="markdown")
            return

        # --- ДЛЯ ВСЕХ ОСТАЛЬНЫХ ДЕЙСТВИЙ — ПРОВЕРКА ПОДПИСКИ ---
        subscribed = await is_user_subscribed(user_id)
        if not subscribed:
            await bot.send_message(
                user_id=user_id,
                text=TEXT_NOT_SUBSCRIBED,
                reply_markup=subscribe_kb
            )
            return

        # --- ИСТОРИЯ КЛУБА ---
        if payload == "history":
            await bot.send_message(user_id=user_id, text=TEXT_HISTORY,
                                   reply_markup=back_to_menu_kb, format="markdown")

        # --- АДРЕСА ---
        elif payload == "addresses":
            await bot.send_message(user_id=user_id, text=TEXT_ADDRESSES,
                                   reply_markup=back_to_menu_kb, format="markdown")

        # --- ПЛАТНЫЕ УСЛУГИ ---
        elif payload == "paid_services":
            await bot.send_message(user_id=user_id, text=TEXT_PAID_SERVICES,
                                   reply_markup=paid_services_kb, format="markdown")

        # --- FAQ ---
        elif payload == "faq_menu":
            await bot.send_message(user_id=user_id, text=TEXT_FAQ_MENU,
                                   reply_markup=faq_kb, format="markdown")

        elif payload == "faq_kids":
            await bot.send_message(user_id=user_id, text=TEXT_FAQ_KIDS,
                                   reply_markup=back_to_faq_kb, format="markdown")

        # --- СПРАВОЧНАЯ ИНФОРМАЦИЯ ---
        elif payload == "contacts":
            await bot.send_message(user_id=user_id, text=TEXT_CONTACTS,
                                   reply_markup=back_to_menu_kb, format="markdown")

        # --- ЧЕМПИОНАТ РОССИИ (суперлига) ---
        elif payload == "champ_menu":
            await bot.send_message(user_id=user_id, text=TEXT_CHAMP_MENU,
                                   reply_markup=championship_menu_kb, format="markdown")

        elif payload in CHAMP_SCHEDULE:
            await bot.send_message(user_id=user_id, text=CHAMP_SCHEDULE[payload],
                                   reply_markup=back_to_champ_kb, format="markdown")

        # --- ПЕРВЕНСТВО РОССИИ (U22) ---
        elif payload == "youth_menu":
            await bot.send_message(user_id=user_id, text=TEXT_YOUTH_MENU,
                                   reply_markup=youth_menu_kb, format="markdown")

        elif payload in YOUTH_SCHEDULE:
            await bot.send_message(user_id=user_id, text=YOUTH_SCHEDULE[payload],
                                   reply_markup=back_to_youth_kb, format="markdown")

        else:
            print(f"UNHANDLED PAYLOAD: {payload}")

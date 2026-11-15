
# BOT: SATO - Marketing
# Забони точики
# Кутубхона: aiogram 3.x
# Насб кардан: pip install aiogram

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# ===== ТАНЗИМОТ =====
BOT_TOKEN = "TOKEN-И-ТУРО-ИНЧО-ГУЗОР"  # Аз @BotFather мегири
ADMIN_ID = 123456789  # ID-и ту (аз @userinfobot мегири)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ===== КЛАВИАТУРАИ АСОСИ =====
def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📢 Хизматрасониҳо"), KeyboardButton(text="💰 Нархҳо")],
            [KeyboardButton(text="💼 Портфолио"), KeyboardButton(text="ℹ️ Дар бораи SATO")],
            [KeyboardButton(text="📝 Фармоиш додан"), KeyboardButton(text="📞 Тамос")],
        ],
        resize_keyboard=True
    )

# ===== START =====
@dp.message(CommandStart())
async def start(message: types.Message):
    text = (
        "Салом! 👋\n\n"
        "Ман <b>SATO</b> — боти расмии <b>SATO Marketing</b> ҳастам.\n\n"
        "Мо бизнеси туро дар Интернет машҳур мекунем:\n"
        "🔥 SMM • 🎯 Таргет • 🎨 Брендинг • 📹 Reels\n\n"
        "Барои оғоз яке аз тугмаҳои поёнро интихоб кун 👇"
    )
    await message.answer(text, reply_markup=main_kb(), parse_mode="HTML")

# ===== ХИЗМАТРАСОНИҲО =====
@dp.message(F.text == "📢 Хизматрасониҳо")
async def services(message: types.Message):
    text = (
        "<b>📢 Хизматрасониҳои SATO Marketing:</b>\n\n"
        "1️⃣ <b>SMM - Идораи Instagram / Telegram</b>\n"
        "Пост, сторис, reels, план ва контент.\n\n"
        "2️⃣ <b>Таргет - Рекламаи пулакӣ</b>\n"
        "Реклама дар Instagram, Facebook, TikTok. Мизоҷи аниқ.\n\n"
        "3️⃣ <b>Брендинг ва Логотип</b>\n"
        "Ном, лого, ранги фирмавӣ, услуби ягона.\n\n"
        "4️⃣ <b>Видео ва Монтаж</b>\n"
        "Reels, рекламаи видеоӣ, TikTok.\n\n"
        "5️⃣ <b>Сайти фурӯшанда / Лендинг</b>\n"
        "Сайт, ки мизоҷ меорад.\n\n"
        "Барои фармоиш тугмаи «📝 Фармоиш додан»-ро пахш кун."
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "💰 Нархҳо")
async def prices(message: types.Message):
    text = (
        "<b>💰 Нархҳои мо:</b>\n\n"
        "📱 <b>SMM - Аз 800 сомонӣ / моҳ</b>\n"
        "🎯 <b>Таргет - Аз 500 сомонӣ + буҷети реклама</b>\n"
        "🎨 <b>Логотип - Аз 300 сомонӣ</b>\n"
        "📹 <b>Монтаж Reels - Аз 50 сомонӣ / 1 видео</b>\n"
        "🌐 <b>Лендинг - Аз 1500 сомонӣ</b>\n\n"
        "❗ Нархи аниқ аз ҳаҷми кор вобаста аст.\n"
        "Барои ҳисоби ройгон фармоиш бидеҳ 👇"
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "💼 Портфолио")
async def portfolio(message: types.Message):
    text = (
        "<b>💼 Портфолиои SATO:</b>\n\n"
        "✅ +50 лоиҳаи анҷомдода\n"
        "✅ +120 000 обуначӣ ҷалбшуда барои мизоҷон\n"
        "✅ Кафе, дӯкон, салон, курсҳо, сохтмон\n\n"
        "Намунаи корҳоро дар Instagram-и мо бубин:\n"
        "👉 @sato.marketing\n\n"
        "Хоҳӣ, ки бизнеси ту ҳам ҳамин хел машҳур шавад?"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝 Фармоиш додан", callback_data="order")]
    ])
    await message.answer(text, parse_mode="HTML", reply_markup=kb)

@dp.message(F.text == "ℹ️ Дар бораи SATO")
async def about(message: types.Message):
    text = (
        "<b>SATO Marketing — Агентии маркетинги рақамӣ</b>\n\n"
        "Мо на танҳо пост мекунем, мо мизоҷ меорем.\n\n"
        "🎯 Ҳадафи мо: Фурӯши ту зиёд шавад.\n"
        "⚡ Усули мо: Зуд, сифатнок, бе об.\n"
        "📍 Ҷойгиршавӣ: Душанбе, Тоҷикистон\n"
        "🕐 Кор мекунем: Ҳар рӯз 09:00 - 21:00"
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "📞 Тамос")
async def contact(message: types.Message):
    text = (
        "<b>📞 Тамос бо мо:</b>\n\n"
        "📱 Telegram: @sato_admin\n"
        "📸 Instagram: @sato.marketing\n"
        "📞 Телефон: +992 00 000 00 00\n\n"
        "Паёмак навис — дар 15 дақиқа ҷавоб медиҳем!"
    )
    await message.answer(text, parse_mode="HTML")

# ===== ФАРМОИШ =====
class Order(StatesGroup):
    name = State()
    business = State()
    service = State()
    phone = State()

@dp.message(F.text == "📝 Фармоиш додан")
@dp.callback_query(F.data == "order")
async def order_start(event: types.Message | types.CallbackQuery, state: FSMContext):
    msg = event if isinstance(event, types.Message) else event.message
    await state.set_state(Order.name)
    await msg.answer("Зӯр! Биё фармоишро оғоз кунем. 😊\n\n<b>Номи ту чист?</b>", parse_mode="HTML")
    if isinstance(event, types.CallbackQuery):
        await event.answer()

@dp.message(Order.name)
async def order_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Order.business)
    await message.answer("Бизнеси ту чист? Масалан: Кафе, Дӯкони либос, Салон...")

@dp.message(Order.business)
async def order_business(message: types.Message, state: FSMContext):
    await state.update_data(business=message.text)
    await state.set_state(Order.service)
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="SMM"), KeyboardButton(text="Таргет")],
        [KeyboardButton(text="Логотип"), KeyboardButton(text="Reels / Видео")],
        [KeyboardButton(text="Сайт / Лендинг")],
    ], resize_keyboard=True, one_time_keyboard=True)
    await message.answer("Кадом хизмат лозим аст?", reply_markup=kb)

@dp.message(Order.service)
async def order_service(message: types.Message, state: FSMContext):
    await state.update_data(service=message.text)
    await state.set_state(Order.phone)
    await message.answer("Рақами телефони туро навиc? Масалан: +992 90 123 45 67", reply_markup=types.ReplyKeyboardRemove())

@dp.message(Order.phone)
async def order_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    business = data.get("business")
    service = data.get("service")
    phone = message.text
    username = f"@{message.from_user.username}" if message.from_user.username else "йўқ"

    await message.answer(
        f"Раҳмат, {name}! ✅\n\n"
        f"Фармоиши ту қабул шуд:\n"
        f"🏢 Бизнес: {business}\n"
        f"📢 Хизмат: {service}\n"
        f"📞 Телефон: {phone}\n\n"
        f"Менеҷери мо ба зудӣ бо ту тамос мегирад!",
        reply_markup=main_kb()
    )
    # Паём ба админ
    try:
        await bot.send_message(
            ADMIN_ID,
            f"🆕 <b>Фармоиши нав! SATO</b>\n\n"
            f"👤 Ном: {name}\n"
            f"🏢 Бизнес: {business}\n"
            f"📢 Хизмат: {service}\n"
            f"📞 Телефон: {phone}\n"
            f"✉️ Telegram: {username}\n"
            f"🆔 ID: {message.from_user.id}",
            parse_mode="HTML"
        )
    except Exception as e:
        logging.error(f"Админга паём нарафт: {e}")

    await state.clear()

# ===== RUN =====
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  

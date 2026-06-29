# Telegram Lead Bot Template

**EN:** A reusable Telegram bot template for capturing leads (name, phone, email) with SQLite storage and instant admin notifications. Deploy in minutes &mdash; no marketplace-specific logic, just a clean FSM-based collection flow you can adapt to any business.

**Stack:** Python, aiogram 3, SQLite.

## Run locally
```
pip install -r requirements.txt
cp .env.example .env
python bot.py
```

## Deploy for free
Works out of the box on [Railway](https://railway.app) (free tier) or [Amvera](https://amvera.ru) &mdash; just set the env vars from `.env.example` and point the start command to `python bot.py`.

---

Телеграм-бот-шаблон для сбора заявок (имя, телефон, email) с базой SQLite и мгновенными уведомлениями админу. Универсальная FSM-логика, легко адаптировать под любой бизнес.

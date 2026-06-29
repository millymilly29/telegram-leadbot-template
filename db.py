import sqlite3

  DB_PATH = "leads.db"


  def init_db():
    conn = sqlite3.connect(DB_PATH)
          conn.execute(
              """CREATE TABLE IF NOT EXISTS leads (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  phone TEXT,
                  email TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              )"""
          )
          conn.commit()
          conn.close()

def save_lead(name: str, phone: str, email: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO leads (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email),
    )
    conn.commit()
    conn.close()

from sqlalchemy import create_engine

db = {
    "host": "db.sueofabfyrjepvhgumqa.supabase.co",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "Tushar@12"
}

url = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
engine = create_engine(url)

try:
    with engine.connect() as conn:
        print("✅ Connected to Supabase PostgreSQL successfully!")
except Exception as e:
    print("❌ Connection failed:", e)

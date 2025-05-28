# db_utils.py or wherever you want

from sqlalchemy import create_engine
from config import SUPABASE_DB

def connect_supabase():
    db = SUPABASE_DB
    url = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    engine = create_engine(url)
    return engine


def save_to_supabase(df, table_name="sales_data", if_exists="replace"):
    engine = connect_supabase()
    with engine.begin() as conn:
        df.to_sql(table_name, con=conn, if_exists=if_exists, index=False)

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="dream_db",
        user="dream_user",
        password="dream_pass",
        host="localhost"
    )

def insert_dream(title, date, mood, description, image_path, keywords, sentiment):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO dreams (title, dream_date, mood, description, image_path, keywords, sentiment)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (title, date, mood, description, image_path, keywords, sentiment))
    conn.commit()
    cur.close()
    conn.close()

def fetch_all_dreams():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM dreams")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

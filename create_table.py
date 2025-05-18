from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tutorial (
                Video_id INT PRIMARY KEY,
                Video_name VARCHAR(100) NOT NULL,
                Video_views INT,
                Watchtime FLOAT
            )
        """)
        db_connection.commit()
        print("Table 'tutorial' created (if not exists).")
    except Exception as e:
        db_connection.rollback()
        print("Table creation failed:", e)
    cur.close()
    db_connection.close()

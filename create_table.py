from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS medicines (
                drug_id INT PRIMARY KEY,
                drug_name VARCHAR(100) NOT NULL,
                price FLOAT,
                expiry DATE NOT NULL
            )
        """)
        db_connection.commit()
        print("Table created (if not exists).")
    except Exception as e:
        db_connection.rollback()
        print("Table creation failed:", e)
    cur.close()
    db_connection.close()

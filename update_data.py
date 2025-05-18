from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    sql = "UPDATE tutorial SET Video_name = 'mysql tutorial' WHERE Video_id = 104"
    try:
        cur.execute(sql)
        db_connection.commit()
        print(f"{cur.rowcount} rows updated")
    except Exception as e:
        db_connection.rollback()
        print("Update failed:", e)
    cur.close()
    db_connection.close()

from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    sql = "DELETE FROM tutorial WHERE Video_id = 105"
    try:
        cur.execute(sql)
        db_connection.commit()
        print(f"{cur.rowcount} rows deleted")
    except Exception as e:
        db_connection.rollback()
        print("Delete failed:", e)
    cur.close()
    db_connection.close()

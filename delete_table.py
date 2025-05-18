from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    table_name = input("Enter the table name to be deleted:")
    sql = f"DROP TABLE {table_name}"
    try:
        cur.execute(sql)
        db_connection.commit()
        print(f"{table_name} deleted")
    except Exception as e:
        db_connection.rollback()
        print("Delete failed:", e)
    cur.close()
    db_connection.close()

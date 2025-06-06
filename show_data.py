from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        table_name = input("Enter table name:")
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        if rows:
            print(f"Data in {table_name} table:", len(rows))
            for row in rows:
                print(row)
        else:
            print("No data found in 'tutorial' table.")
    except Exception as e:
        print("Failed to fetch data:", e)
    cur.close()
    db_connection.close()

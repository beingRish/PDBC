from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        cur.execute("SHOW DATABASES")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row[0])
        else:
            print("No Database found")
    except Exception as e:
        print("Failed to fetch database:", e)
    cur.close()
    db_connection.close()

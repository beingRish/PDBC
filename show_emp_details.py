from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        cur.execute("SELECT * FROM emp_details")
        rows = cur.fetchall()
        if rows:
            print("Employee Count:", len(rows))
            for row in rows:
                print(row)
        else:
            print("No data found in 'emp_details' table.")
    except Exception as e:
        print("Failed to fetch data:", e)
    cur.close()
    db_connection.close()

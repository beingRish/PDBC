from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        cur.execute("SELECT * FROM tutorial")

        n = int(input("Enter the number of rows: "))
        row = cur.fetchmany(n)
        print(row)

        while cur.fetchone():
            pass


    except Exception as e:
        print("Error fetching data:", e)
    finally:
        cur.close()
        db_connection.close()

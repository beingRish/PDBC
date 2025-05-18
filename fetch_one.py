from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        cur.execute("SELECT * FROM tutorial")
        n = int(input("Enter the number of rows: "))
        
        for i in range(n):
            row = cur.fetchone()
            if row is None:
                break
            if row:
                print(f"{i} row:", row)
            else:
                print("No more data available.")
                break

        # Discard any unread results to avoid error on close
        while cur.fetchone():
            pass

    except Exception as e:
        print("Error fetching data:", e)
    finally:
        cur.close()
        db_connection.close()

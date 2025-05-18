from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor(prepared=True)
    try:
        sql = """INSERT INTO medicines
            (drug_id, drug_name, price, expiry)
            VALUES (%s, %s, %s, %s)
        """

        n = int(input("Enter number of medicines:"))
        for i in range(n):
            drug_id = int(input("Enter drug id:"))
            drug_name = input("Enter drug name:")
            price = float(input("Enter price:"))
            expiry_date = input("Enter expiry date(2025-07-09):")

            cur.execute(sql,(drug_id, drug_name, price, expiry_date))
            db_connection.commit()
            print(f"{cur.rowcount} row(s) inserted")
    except Exception as e:
        db_connection.rollback()
        print("Insert failed:", e)
    finally:
        cur.close()
        db_connection.close()

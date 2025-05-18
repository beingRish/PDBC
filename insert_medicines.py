from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        sql = """INSERT INTO medicines
            (drug_id, drug_name, price, expiry)
            VALUES (%(drug_id)s, %(drug_name)s, %(price)s, %(expiry_date)s)
        """

        while True:
            drug_id = int(input("Enter drug id:"))
            drug_name = input("Enter drug name:")
            price = float(input("Enter price:"))
            expiry_date = input("Enter expiry date(YYYY-MM-DD):")

            cur.execute(
                sql,
                {
                    'drug_id': drug_id,
                    'drug_name': drug_name,
                    'price': price,
                    'expiry_date': expiry_date
                }
            )
            db_connection.commit()
            ans = input("Do you have more medicines:(y/n):").lower()
            if ans!='y':
                break
            print(f"{cur.rowcount} row(s) inserted")
            print("-"*50)
        
    except Exception as e:
        db_connection.rollback()
        print("Insert failed:", e)
    finally:
        cur.close()
        db_connection.close()

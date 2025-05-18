from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    try:
        empid = input("Enter employee ID to update: ")
        new_salary = input("Enter new salary: ")

        sql = "UPDATE emp_details SET salary = %s WHERE emp_id = %s"
        cur.execute(sql, (new_salary, empid))
        db_connection.commit()

        print(f"{cur.rowcount} row(s) updated")
    except Exception as e:
        db_connection.rollback()
        print("Update failed:", e)
    finally:
        cur.close()
        db_connection.close()

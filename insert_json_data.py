import json
from db_connect import get_connection

db_connection = get_connection()

with open('employee.json', 'r') as f:
    employees = json.load(f)

if db_connection:
    cur = db_connection.cursor()
    try:
        for employee in employees:
            val = (employee['id'],employee['name'],employee['age'],employee['salary'])
            sql = """INSERT INTO emp_details
                (id, name, age, salary)
                VALUES (%s, %s, %s, %s)
            """
            cur.execute(sql,val)
            db_connection.commit()
            print(cur.rowcount, "rows got inserted")
        
    except Exception as e:
        db_connection.rollback()
        print("Insert failed:", e)
    finally:
        cur.close()
        db_connection.close()
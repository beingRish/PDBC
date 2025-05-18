from db_connect import get_connection

db_connection = get_connection()
if db_connection:
    cur = db_connection.cursor()
    sql = """
    INSERT INTO tutorial (Video_id, Video_name, Video_views, Watchtime) VALUES
    (106, 'python basics', 25000, 20.0),
    (107, 'exception basics', 12000, 30.4);
    """
    try:
        cur.execute(sql)
        db_connection.commit()
        print(f"{cur.rowcount} rows inserted")
    except Exception as e:
        db_connection.rollback()
        print("Insert failed:", e)
    cur.close()
    db_connection.close()

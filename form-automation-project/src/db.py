import psycopg2

def connect():
    conn_string = (
        "host=localhost "
        "dbname=form_automation "
        "user=postgres "
        "password=992254 "
        "client_encoding=utf8"
    )

    return psycopg2.connect(conn_string)

def mark_processed(form_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE forms SET processado = TRUE WHERE id = %s",
        (form_id,)
    )

    conn.commit()
    cur.close()
    conn.close()

def save_log(total, status):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO logs (total_processed, status)
        VALUES (%s, %s);
    """, (total, status))

    conn.commit()
    cur.close()
    conn.close()

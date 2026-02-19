from db import connect

def get_pending_forms():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, nome, email, idade
        FROM forms
        WHERE processado = FALSE
    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data
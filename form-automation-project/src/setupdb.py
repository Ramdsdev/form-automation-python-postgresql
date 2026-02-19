# -*- coding: utf-8 -*-

from db import connect

def reset_forms():
    conn = connect()
    cur = conn.cursor()

    # limpa tabela
    cur.execute("DELETE FROM forms;")

    # insere dados de exemplo
    cur.execute("""
        INSERT INTO forms (nome, email, idade, processado)
        VALUES
        ('Maria Souza', 'maria@email.com', 31, false),
        ('Carlos Lima', 'carlos@email.com', 22, false),
        ('João Silva', 'joao@email.com', 25, false);
                """)

    conn.commit()
    cur.close()
    conn.close()

    print("Banco preparado para testes!")

if __name__ == "__main__":
    reset_forms()
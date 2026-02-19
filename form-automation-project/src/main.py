from read_forms import get_pending_forms
from automation import fill_form
from db import mark_processed
from browser import open_form
from db import save_log


forms = get_pending_forms()

open_form()
for form in forms[:1]:
    form_id, nome, email, idade = form

    fill_form(nome, email, idade)
    mark_processed(form_id)

input("Pressione ENTER para continuar...")
print("FORMULÁRIO ENVIADO") 

forms = get_pending_forms()
total = 0

try:
    for form in forms:
        form_id, nome, email, idade = form

        fill_form(nome, email, idade)
        mark_processed(form_id)

        total += 1

    save_log(total, "SUCCESS")
    print(f"{total} formulários processados!")

except Exception as e:
    save_log(total, "ERROR")
    print("Erro:", e)
    




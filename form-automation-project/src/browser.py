import webbrowser
import time

def open_form():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfa4Q7Qi6g5XL5bvaNn84H4zzOztZNEp6LbyHuCsGtVDyl4Rg/viewform"

    print("Abrindo navegador...")
    webbrowser.open(url)

    print("Aguardando carregamento...")
    time.sleep(8)  # tempo para página abrir

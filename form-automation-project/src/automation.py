import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8

def fill_form(nome, email, idade):

    print("Começando em 10 segundos...")
    time.sleep(10)

    # NOME
    pyautogui.write(nome)
    time.sleep(1.2)
    pyautogui.press("tab")

    # EMAIL
    time.sleep(1.2)
    pyautogui.write(email)
    time.sleep(1.2)
    pyautogui.press("tab")

    # IDADE
    time.sleep(1.2)
    pyautogui.write(str(idade))
    time.sleep(1.2)

    pyautogui.press("enter")

    

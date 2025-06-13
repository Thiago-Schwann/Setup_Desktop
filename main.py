import os
import pyautogui
from time import sleep
from dotenv import load_dotenv

from busca_imagens import clica_imagem

load_dotenv()
pyautogui.FailSafeException

SENHA_GOOGLE = os.getenv("SENHA_GOOGLE")

#Abrir o OperaGX
clica_imagem('icone_operagx')
sleep(1)
pyautogui.hotkey("ctrl", "shift", "n")
sleep(1)
pyautogui.hotkey("ctrl", "l")
sleep(1)
pyautogui.write("Google", interval=0.15)
sleep(0.25)
pyautogui.press("Enter")
sleep(1)

#Abrir um site de notícias
pyautogui.hotkey("ctrl", "t")
sleep(0.5)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://thenews.waffle.com.br/newsletter", interval=0.01)
pyautogui.press("Enter")
sleep(1)

#Acessar o email
pyautogui.hotkey("ctrl", "t")
sleep(0.5)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://workspace.google.com/intl/pt-BR/gmail/", interval=0.01)
pyautogui.press("Enter")
sleep(3)
clica_imagem('login_gmail')
sleep(2)
pyautogui.write('thiag.carve@gmail.com')
pyautogui.press("Enter")
sleep(4)
pyautogui.write(SENHA_GOOGLE)
pyautogui.press("Enter")




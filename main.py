import os
import pyautogui
from time import sleep
from dotenv import load_dotenv

from busca_imagens import clica_imagem

load_dotenv()
pyautogui.FailSafeException

SENHA_GOOGLE = os.getenv("SENHA_GOOGLE")

#Abrir o Google no OperaGX
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

#Acessar o Gmail
pyautogui.hotkey("ctrl", "t")
sleep(0.5)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://workspace.google.com/intl/pt-BR/gmail/", interval=0.01)
pyautogui.press("Enter")
sleep(3)
clica_imagem('login_gmail')
sleep(3)
pyautogui.write('thiago092527@gmail.com')
pyautogui.press("Enter")
sleep(4)
pyautogui.write(SENHA_GOOGLE)
pyautogui.press("Enter")
sleep(2)

#Abrir o Spotify
clica_imagem('icone_spotify')
sleep(10)
clica_imagem('playlist_lofi')
sleep(2)
clica_imagem('playlist_lofi_play_button')

#Abrir Discord
clica_imagem('icone_discord')




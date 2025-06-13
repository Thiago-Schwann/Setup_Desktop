import pyautogui

#Usamos isso para verificar a posição do mouse na tela, podendo pegar cordenada dos elementos da tela em tempo real. 

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
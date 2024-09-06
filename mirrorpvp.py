import pyautogui as pag
from time import sleep
import keyboard
import pygetwindow as gw


#define uma função que para o codigo quando a tecla "Q" for pressionada
def parar_Script():
    print('Parando a execução...')
    global executando 
    executando = False

executando = True
keyboard.add_hotkey('q', parar_Script)

def trocar_janela():
    try:
        vscode_window = gw.getWindowsWithTitle('Visual Studio Code')[0]
        vscode_window.minimize()
    except:
        print('Nao foi encontrado o vscode')

    try:
        emulator_window = gw.getWindowsWithTitle('Emulador GTarcade')[0]
        emulator_window.activate()
        print(f"Focado na janela do emulador: {'Emulador GTarcade'}.")
    except IndexError:
        print(f"Janela do emulador '{'Emulador GTarcade'}' não encontrada.")

trocar_janela()

 #clica no iniciar
while executando == True:
    pag.click(878, 962)
    sleep(20)

    #aperta para selecionar personagem
    pag.click(949, 838)
    sleep(10)
    pag.click(949, 838)
    sleep(3)
    pag.click(949, 838)
    sleep(1)

    #desistir e confirmar a desistencia
    pag.click(89, 225)
    sleep(0.5)
    pag.click(1129, 648)
    sleep(5)
    pag.click(1011, 598)
    sleep(10)

print('Fim do script.')
import pyautogui
import keyboard
from time import sleep
import pygetwindow as gw

print('O que quer comprar?')
print('1 - Pedra da Vontade Estelar')
print('2 - Poeira de Oricalco comum')
print('3 -  Gema limitada')
print('4 - Frag de Livro Azul')
print('5 - Frag do Arayashiki')
print('6 - Caixa de Flor')
print('7 - Ouro')
print('8 - XP')

def achar_janela():
    try:
        emulator_window = gw.getWindowsWithTitle('Emulador GTarcade')[0]
        emulator_window.activate()
        print(f"Focado na janela do emulador: {'Emulador GTarcade'}.")
    except IndexError:
        print(f"Janela do emulador '{'Emulador GTarcade'}' não encontrada.")

escolha = input('Escolha o Item: ')
int_escolha = int(escolha)
quantidade = input('Quantas vezes deseja comprar? ')
int_quant = int(quantidade)


if escolha.isdigit() == False:
    print('Digite um valor válido')
else:
    achar_janela()
    if int_escolha == 1:
        for i in range(1, int_quant + 1):
            pyautogui.click(493, 373) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 2:
        for i in range(1, int_quant + 1):
            pyautogui.click(797, 379) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 3:
        for i in range(1, int_quant + 1):
            pyautogui.click(1096, 378) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 4:
        for i in range(1, int_quant + 1):
            pyautogui.click(1384, 371) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 5:
        for i in range(1, int_quant + 1):
            pyautogui.click(497, 718) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 6:
        for i in range(1, int_quant + 1):
            pyautogui.click(789, 710) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 7:
        for i in range(1, int_quant + 1):
            pyautogui.click(1090, 727) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    elif int_escolha == 8:
        for i in range(1, int_quant + 1):
            pyautogui.click(1375, 709) 
            sleep(1)
            pyautogui.click(931, 815)
            sleep(1)
    
    

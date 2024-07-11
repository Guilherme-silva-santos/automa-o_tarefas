import pyautogui 
import time
import pandas 
# configura que a cada comando do pyautogui tera uma pausa de 0.5 segundos
pyautogui.PAUSE = 0.5

# abrindo o navegador e entrando no sistema da empresa

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrando no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# após esta tela abrir, preciso de um tempo para a tela carregar
time.sleep(3)

# Fazer login

pyautogui.click(x=1111, y=376)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

# code
pyautogui.click(x=860, y=258)
pyautogui.write("Cod")
pyautogui.press("tab")

#marca
pyautogui.write("marca")
pyautogui.press("tab")

#tipo
pyautogui.write("tipo")
pyautogui.press("tab")

# categoria
pyautogui.write("categoria")
pyautogui.press("tab")

# preco
pyautogui.write("preço")
pyautogui.press("tab")

# custo
pyautogui.write("custo")
pyautogui.press("tab")

# obs
pyautogui.write("obs")
pyautogui.press("tab")
pyautogui.press("enter")

# apos cadastrar tudo eu preciso dar um scroll pra cima para que seja cadastrado um novo
pyautogui.scroll(5000)

# fazer um loop para todos os produtos para todas as linhas da tabela, então a cada linha da tabela deve ser feito o cadastro
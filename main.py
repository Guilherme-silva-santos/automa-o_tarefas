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

# fazer um loop para todos os produtos para todas as linhas da tabela, para cada linha da tabela executa 
# para cada item dentro de uma lista de itens 
for linha in tabela.index:
    pyautogui.click(x=860, y=258)
    # transforma para string o dado retornado 
    # pega a linha e coluna que devem ser exibidos
    # usa a var linha pois sempre que o for for executado, a linha vai mudando 
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    #obs diferente então preenche   
    
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

# apos cadastrar tudo eu preciso dar um scroll pra cima para que seja cadastrado um novo
pyautogui.scroll(5000)


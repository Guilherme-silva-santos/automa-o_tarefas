import pyautogui 

# configura que a cada comando do pyautogui tera uma pausa de 0.5 segundos
pyautogui.PAUSE = 0.5

# abrindo o navegador e entrando no sistema da empresa

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrando no link
#entrando no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
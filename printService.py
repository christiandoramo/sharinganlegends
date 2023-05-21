import pyautogui
import os

def printScreen():
    screenshot = pyautogui.screenshot()
    
    # Verifica se o arquivo 'screenshot.png' já existe
    if os.path.exists('screenshot.png'):
        # Incrementa um número no nome do arquivo até encontrar um nome disponível
        count = 1
        while os.path.exists(f'screenshot_{count}.png'):
            count += 1
        filename = f'screenshot_{count}.png'
    else:
        filename = 'screenshot.png'
    
    # Salva a imagem com o nome gerado
    screenshot.save(filename)
    print(f"Imagem salva como: {filename}")
    
    
def printRemove(caminho_arquivo):
    try:
        os.remove(caminho_arquivo)
        print(f"Arquivo {caminho_arquivo} removido com sucesso.")
    except OSError as e:
        print(f"Erro ao remover o arquivo {caminho_arquivo}: {e}")

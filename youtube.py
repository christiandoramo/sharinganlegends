import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# IMPORTANDO A KEY DA API DO YOUTUBE

# Obtém o caminho absoluto para a pasta myenv
myenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'myenv'))
# Define o caminho completo para o arquivo .env dentro da pasta .myenv
dotenv_path = os.path.join(myenv_path, '.env')
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path)

# PEGANDO MINHAS NOTIFICAÇÕES PELA API DO YOUTUBE

# Configurações da API
API_KEY = os.getenv('API_KEY')
print(API_KEY)
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
def get_notifications():

    response = youtube.activities().list(part='snippet', mine=True).execute()
    notifications = response['items']
    for notification in notifications:
        print(notification['snippet']['title'])


# Chama a função para obter as notificações
get_notifications()

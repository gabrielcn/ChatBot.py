# Passo 1: Baixar e importar as bibliotecas
# Agora que as bibliotecas estão devidamente instaladas, vamos importa-las

import pywhatkit
import keyboard
import time
from datetime import datetime

# Passo 2: Definir a lista de contatos que queremos enviar a mesagem automática

lista_contatos = ['+5512923497452', '+5511978923074', '+5533987634578'] #números fictícios por questão de privacidade

# Passo 3: Definir o intervalo de envio

for i in range(0, len(lista_contatos)):
    # Enviar a mensagem automática
    pywhatkit.sendwhatmsg(lista_contatos[i], 'Esta mensagem é automática (não responda)!\nVamos automatizar o mundo!', datetime.now().hour, datetime.now().minute + 1)
    time.sleep(15)
    keyboard.press_and_release('ctrl + w')

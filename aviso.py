#Vamos a comprobar el nivel de tintas, si alguna es menor a 10 o igual avisamos 
# En teoria usando Teams y Webhook podemos mandar un mensaje a un canal de Teams
# pero odio a Microsoft y no quiero usarlo, asi que vamos a usar un bot de 
# Telegram para mandar el mensaje, que es mas facil y rapido de hacer.



def comprobar(tintas):
    for nombre,tinta in tintas.items():
        if tinta <= 10:
            print(f"Esto ya se va a acabar {tinta} ")
            #TODO
            #Hcemos una funcion que mande un mensaje a un bot de telegram con el nombre de la impresora y yo creo que todos las tintas
        else:
            print(f"Arre LuLu {nombre}")
            
            
def bot_telegram(mensaje):
    import requests

    # Reemplaza 'TU_TOKEN' con el token de tu bot de Telegram
    token = 'TU_TOKEN'
    
    # Reemplaza 'TU_CHAT_ID' con el ID del chat o canal donde quieres enviar el mensaje
    chat_id = 'TU_CHAT_ID'
    
    # URL de la API de Telegram para enviar mensajes
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    
    # Datos del mensaje
    data = {
        'chat_id': chat_id,
        'text': mensaje
    }
    
    # Enviar el mensaje
    response = requests.post(url, data=data)
    return response
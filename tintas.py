import estado
from estado import obtener_estado_impresora
from aviso import comprobar


def nivelTintas(nombre,direccion):
    
    '''
    Esta función obtiene el nivel de tintas de una impresora específica.
    Parámetros:
    - nombre: El nombre de la impresora.
    - direccion: La dirección IP de la impresora.
    Retorna:
    - Un diccionario con los niveles de tinta de la impresora.'''
    
    
    
    # La URL de la impresora para obtener el estado de los consumibles
    #/webglue/rawcontent?timedRefresh=1&c=Status&lang=es
    # Esta se obtiene de la dirección IP de la impresora y el endpoint específico para obtener el estado de los consumibles.
    # Ve a inspeccionar la página de estado de la impresora y busca la URL que contiene "rawcontent" para obtener el JSON con los niveles de tinta.
    # inspect --> network --> filtra por XHT --> refresh --> Busca cual es la URL que contiene "rawcontent" y copia esa URL para usarla en tu script.
    
    url_objetivo = f"http://{direccion}/webglue/rawcontent?timedRefresh=1&c=Status&lang=es"



    print(f"Consultando estado de la impresora: {url_objetivo}...\n")
    datos_json = obtener_estado_impresora(url_objetivo)
    if datos_json:
            try:
                # Hay que asegurarse de que la estructura del JSON es la esperada antes de intentar acceder a ella.
                # Busca la parte del toner que necesites, y filtrala, porque hay muchos datos en el JSON que no son necesarios para este caso.
                # Pero quizas para tu caso si, como sea.
                
                # yo lo que hago es imprimir el JSON completo para ver la estructura y luego navegar por él para obtener los datos que necesito.
                #print(datos_json)
                
                # lo que me interesa es la parte de "nodes" -> "supplies" -> "Black Toner" / "Black Imaging Kit" / "Maintenance Kit"

                supplies = datos_json.get("nodes", {}).get("supplies", {})
    
                if supplies:
                    print(f"--- ESTADO DE CONSUMIBLES DE LA IMPRESORA {nombre} {direccion}---")
                    
                    # Puedes extraer elementos específicos de forma segura con .get()
                    #black_toner = supplies.get("Black Toner", "No disponible")
                    #black_imaging = supplies.get("Black Imaging Kit", "No disponible")
                    #maintenance_kit = supplies.get("Maintenance Kit", "No disponible")
    
                    # Forma segura de extraerlos por si alguno no viene en la respuesta:
                    black_toner = (supplies.get("Black Toner") or {}).get("curlevel", "N/A")
                    black_imaging = (supplies.get("Black Imaging Kit") or {}).get("curlevel", "N/A")
                    maintenance_kit = (supplies.get("Maintenance Kit") or {}).get("curlevel", "N/A")
    
                    print(f"- Cartucho Negro (Black Toner): {black_toner}")
                    print(f"- Unidad de Imagen (Black Imaging Kit): {black_imaging}")
                    print(f"- Kit de Mantenimiento (Maintenance Kit): {maintenance_kit}")

                    tintas = {
                        "Black Toner":black_toner,
                        "Black Imaging Kit":black_imaging,
                        "Maintenance Kit":maintenance_kit
                    }

                    return tintas

                    
                    # Si quieres ver todos los consumibles que lleguen de golpe de forma dinámica:
                    #print("\n--- Listado completo de suministros ---")
                    #for k, v in supplies.items():
                    #    print(f"  * {k}: {v}")
                else:
                    print("No se encontró la sección 'supplies' en el JSON recibido.")
                    # Útil para depurar si la estructura cambia un poco:
                    # print(datos_json)
    
            except Exception as e:
                print(f"Error al procesar la estructura del JSON: {e}")


# Aquí puedes definir las direcciones IP de tus impresoras y sus nombres para luego consultar su estado de consumibles.
ips = {
    "dsdf":"10.x.x.x",
    "hgrjfg":"10.x.x.x",
    "Atjfbf":"10.x.x.x",
    "hetrw":"10.x.x.x"
}




#for nombre,direccion in ips.items():
#    resultado  = nivelTintas(nombre,direccion)
#    comprobar(resultado)
    
actualOperaciones = nivelTintas("Operaciones","10.x.x.x")
print(actualOperaciones)


comprobar(actualOperaciones)
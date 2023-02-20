def clasificador(ip:str):

    """ Clasifica el rango al que pertenece una IP. Distingue entre 
        ip publica y privada y sus clases.

    Args:
        ip (string): es la ip en formato 000.000.000.000

    return:
        json con el tipo y la clase.
    """

    # Procesamiento de IP
    ip_numbers = ip.split('.')

    try:
        ip_numbers = [eval(i) for i in ip_numbers]

    except: 
        return {"Error":"La ip no es válida"}


    # Verificacion de ip válida 
    if (len(ip_numbers) != 4): 
        return {"Error":"La ip no es válida"}

    if (ip_numbers[0] >= 0 and ip_numbers[0] <= 255): 
        pass 
    else: 
        return {"Error":"El primer numero no es octano"}

    if (ip_numbers[1] >= 0 and ip_numbers[1] <= 255): 
        pass 
    else: 
        return {"Error":"El segundo numero no es octano"}
    
    if (ip_numbers[2] >= 0 and ip_numbers[2] <= 255): 
        pass 
    else: 
        return {"Error":"El tercero numero no es octano"}

    if (ip_numbers[3] >= 0 and ip_numbers[3] <= 255): 
        pass 
    else: 
        return {"Error":"El cuarto numero no es octano"}
    

    # CLASIFICACION 
    # privada
    if(ip_numbers[0] == 10):
        return {"tipo":"Privada", "clase":"A"}

    if((ip_numbers[0] == 172) and (ip_numbers[1] >= 16) and (ip_numbers[1] <= 31)):
        return {"tipo":"Privada", "clase":"B"}

    if((ip_numbers[0] == 192) and (ip_numbers[1] == 168)):
        return {"tipo":"Privada", "clase":"C"}


    # publica
    if(ip_numbers[0] >= 0 and  ip_numbers[0] <= 126):
        return {"tipo":"Publica", "clase":"A"}

    if(ip_numbers[0] >= 128 and  ip_numbers[0] <= 191):
        return {"tipo":"Publica", "clase":"B"}

    if(ip_numbers[0] >= 192 and  ip_numbers[0] <= 223):
        return {"tipo":"Publica", "clase":"C"}

    if(ip_numbers[0] >= 224 and  ip_numbers[0] <= 239):
        return {"tipo":"Publica", "clase":"D"}

    if(ip_numbers[0] >= 240 and  ip_numbers[0] <= 254):
        return {"tipo":"Publica", "clase":"E"}
    


    return {"Error":"La ip no es válida"}




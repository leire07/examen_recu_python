import csv
from unicodedata import name
from pprint import pprint

dic = {
    '1020': {'description': 'PSEG ALAMEDA 14 (DAVANT JARDÍ VIA CENTRAL) - VALÈNCIA',
             'id': '1020',
             'lat': '4372694.493',
             'lon': '726668.229',
             'name': 'Albereda'},
    '1021': {'description': 'PSEG ALAMEDA 1(DAVANT JARDÍ VIA CENTRAL) - VALÈNCIA',
             'id': '1021',
             'lat': '4372960.453',
             'lon': '726489.285',
             'name': 'Pla del Reial'},
    '1026': {'description': 'CAMI RIBAS DAVANT  ADOR - CASTELLAR-OLIVERAL',
             'id': '1026',
             'lat': '4368090.933',
             'lon': '727158.752',
             'name': 'Ribàs (imparell) - Ador'},
    '1027': {'description': 'C  18 - VALÈNCIA',
             'id': '1027',
             'lat': '4368085.738',
             'lon': '726986.867',
             'name': 'Principal - El Caroig'},
    '1028': {'description': 'PL VIRGEN DE LEPANTO 7 - CASTELLAR-OLIVERAL',
             'id': '1028',
             'lat': '4367757.724',
             'lon': '726913.853',
             'name': 'Mare de Déu de Lepant (imparell) - Esc. F. Siurana'},
    '1029': {'description': 'C VICENTE PUCHOL 72 - CASTELLAR-OLIVERAL',
             'id': '1029',
             'lat': '4367435.072',
             'lon': '726877.702',
             'name': 'Vicent Puchol - Font de Bonet'},
    '1030': {'description': 'C CRISTO DEL REFUGIO 60 - CASTELLAR-OLIVERAL',
             'id': '1030',
             'lat': '4367200.126',
             'lon': '726906.174',
             'name': 'Crist del Refugi - Davant Sant Agustí'},
    '1032': {'description': 'C TIRIG 4 - VALÈNCIA',
             'id': '1032',
             'lat': '4373621.9',
             'lon': '727134.007',
             'name': 'Tírig - Guàrdia Civil'},
    '1035': {'description': 'AV ARAGÓN 22 (DAVANT INSTITUT) - VALÈNCIA',
             'id': '1035',
             'lat': '4372357.349',
             'lon': '727211.626',
             'name': 'Aragó - Finlàndia'},
    '1036': {'description': 'C URUGUAY 38 - VALÈNCIA',
             'id': '1036',
             'lat': '4370588.712',
             'lon': '724814.13',
             'name': 'Uruguai - Veneçuela'},
    '1038': {'description': 'C ARCHIDUQUE CARLOS 63 - VALÈNCIA',
             'id': '1038',
             'lat': '4371443.232',
             'lon': '723984.759',
             'name': 'Arxiduc Carles (imparell) - Tres Forques'},
    '1039': {'description': 'C ERNESTO FERRER 1 - VALÈNCIA',
             'id': '1039',
             'lat': '4372531.034',
             'lon': '727350.354',
             'name': 'Ernest Ferrer - Aragó'},
    '1041': {'description': 'GV RAMON Y CAJAL 25 - VALÈNCIA',
             'id': '1041',
             'lat': '4371764.019',
             'lon': '725195.021',
             'name': "Plaça d'Espanya"},
    '1042': {'description': 'AV REGNE DE VALENCIA 73 - VALÈNCIA',
             'id': '1042',
             'lat': '4371461.031',
             'lon': '726851.35',
             'name': 'Regne de València - Ciscar'},
    '1044': {'description': 'AV VICENTE ANDRES ESTELLES POLIESPORTIU - BURJASSOT',
             'id': '1044',
             'lat': '4376308.866',
             'lon': '722135.007',
             'name': 'Poliesportiu de Burjassot'},
    '1050': {'description': 'C MEDITERRANEO 4 - VALÈNCIA',
             'id': '1050',
             'lat': '4372087.375',
             'lon': '729539.815',
             'name': 'Mediterránia - Vicent Brull'},
    '1052': {'description': 'C EUGENIA VIÑES 109 (DAVANT BALNEARI) - VALÈNCIA',
             'id': '1052',
             'lat': '4372004.909',
             'lon': '730090.35',
             'name': 'Eugènia Viñes - Mare de Déu del Sufragi'},
    '1054': {'description': 'AV ARAGÓN 4 - VALÈNCIA',
             'id': '1054',
             'lat': '4372112.402',
             'lon': '727104.081',
             'name': 'Aragó - Saragossa'},
    '1055': {'description': 'AV ARAGÓN 34 - VALÈNCIA',
             'id': '1055',
             'lat': '4372582.617',
             'lon': '727355.834',
             'name': 'Aragó - Ernest Ferrer'},
    '1057': {'description': 'AV ARAGÓN 42 (ACCÉS) - VALÈNCIA',
             'id': '1057',
             'lat': '4372834.922',
             'lon': '727444.367',
             'name': 'Estadi de Mestalla'},
    '1060': {'description': 'C PEDRO CABANES 10 - VALÈNCIA',
             'id': '1060',
             'lat': '4375052.103',
             'lon': '725915.428',
             'name': 'Pere Cabanes - Mont Carmel'},
    '1061': {'description': 'C PEDRO CABANES 58 - VALÈNCIA',
             'id': '1061',
             'lat': '4374997.078',
             'lon': '725698.115',
             'name': 'Pere Cabanes - Sant Doménec Savio'},
    '1062': {'description': 'C PEDRO CABANES 88 - VALÈNCIA',
             'id': '1062',
             'lat': '4374905.938',
             'lon': '725403.439',
             'name': 'Pere Cabanes - Bisbe Laguarda'},
    '1067': {'description': 'AV ECUADOR  EL 93 (DAVANT) - VALÈNCIA',
             'id': '1067',
             'lat': '4375074.905',
             'lon': '724193.889',
             'name': 'Equador - Pintor Matarana'},
    '1080': {'description': 'C SAN VICENTE DE PAUL 15 - VALÈNCIA',
             'id': '1080',
             'lat': '4374553.414',
             'lon': '726119.689',
             'name': 'Sant Vicent de Paül - Peníscola'},
    '1083': {'description': 'AV ARAGÓN 25 - VALÈNCIA',
             'id': '1083',
             'lat': '4372578.4',
             'lon': '727276.222',
             'name': 'Aragó'},
    '1085': {'description': 'AV ARAGÓN 16 - VALÈNCIA',
             'id': '1085',
             'lat': '4372285.722',
             'lon': '727244.328',
             'name': 'Aragó - Xile'},
    '1087': {'description': 'AV SAN ANTONIO 140 (DAVANT) - MISLATA',
             'id': '1087',
             'lat': '4372858.716',
             'lon': '721698.011',
             'name': 'Sant Antoni - Pizarro'},
    '1091': {'description': 'CTRA MALILLA 60 - VALÈNCIA',
             'id': '1091',
             'lat': '4370047.781',
             'lon': '725499.184',
             'name': 'Malilla (parell) - Bernat Descoll'},
    '1096': {'description': 'C RAMON LLULL 31 (DAVANT) - VALÈNCIA',
             'id': '1096',
             'lat': '4373073.313',
             'lon': '728257.03',
             'name': 'Ramon Llull - Bernat Fenollar'}
}

#no me coge los archivos
def read_data(texto1, texto2):
    lista1= []
    lista2 = []

    with open(texto1, 'r') as archivo1:
        reader = csv.reader(archivo1)
        for fila in reader:
            lista1.append(archivo1)

            
    print(lista1)

    with open(texto2, 'r') as archivo2:
        reader2 = csv.reader(archivo2)
        for fila2 in reader2:
            lista2.append(fila2)
    
    print(lista2)

def get_name_description(clave, diccionario):
    lista = []
    if(len(clave)==4):
        for k, v in diccionario.items():
            if clave in k:
                for i in v.values():
                    lista.append(i)
                description = lista[0]
                nombre = lista[4]
                print("Para la clave: " + clave)
                print("La descripcion es: " + description)
                print("El nombre es: " + nombre)
        if (len(lista) == 0):
            raise ValueError ("No existe esa clave")
    else:
        raise ValueError ("No existe esa clave")
    
def search_by_lon(longitud, diccionario):
    #Devuelve la clave que tenga ese valor de longitud es su campo lon
    lista = []
    resultado=[]
    if(type(longitud)==float):
        for clave in diccionario.values():
            print(clave["lon"])

def get_min(clave, diccionario):
    lista = []
    description = []
    nombre = []
    contador = 0
    if(len(clave)<1020):
        for k, v in diccionario.items():
            if(k<clave):
                for i in v.values():
                    lista.append(i)
                    print(lista)
                description[contador] = lista[0]
                nombre[contador] = lista[4]
                print("Para el valor: " + clave)
                print("La descripcion es: " + description)
                print("El nombre es: " + nombre)
                contador = contador + 1
        if (len(description) == 0):
            raise ValueError ("No hay elementos")
    else:
        raise ValueError ("Ha saltado el error")



#get_name_description('1080', dic)
#get_name_description('2000', dic)
#search_by_lon(728257.03, dic)
get_min('2000', dic)


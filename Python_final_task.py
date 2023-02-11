from csv import DictReader

atlg_suma = 0
atlg_kiekis = 0

listas = []
with open('./2018.csv', encoding='utf8') as file:  
    csv_reader = DictReader(file)
    for row in csv_reader:      
        if row['Atlyginimas'] in '0':
        # if row['Atlyginimas'] not in '':
            row['Atlyginimas'] = 0
            listas.append(row)      
        else: 
            row['Atlyginimas'] = int(row['Atlyginimas'])
            listas.append(row)
            # print(row['Atlyginimas'])
            atlg_suma += row['Atlyginimas']           
            atlg_kiekis += 1
           

# print(listas)
            


vidurkis = round((atlg_suma/atlg_kiekis),2)




for eil in listas:
    if eil['Miestas'] in 'Vinius' or eil['Miestas'] in 'Vilniuje' or eil['Miestas'] in 'Vilnius ' or eil['Miestas'] in 'VIlnius':
        eil['Miestas'] = 'Vilnius'
    elif eil['Miestas'] in 'Kaunas ':
        eil['Miestas'] = 'Kaunas'
    elif eil['Miestas'] in '' or eil['Miestas'] in 'Kita' or eil['Miestas'] in 'Užsienis':
        eil['Miestas'] = 'Neirasyta'

# print(listas)
setas_miestu = set()
listas_miestu = []
for eil in listas:
    setas_miestu.add(eil['Miestas'])
setas_miestu.remove('Neirasyta')



for eil in listas:
    if eil['Šaltinis'] in '' or eil['Šaltinis'] in 'Other':
        eil['Šaltinis'] = 'Nepasirinkta'

setas_kalbu = set()
for eil in listas:
    setas_kalbu.add(eil['Šaltinis'])
setas_kalbu.remove('Nepasirinkta')




atlgmax = listas[1]['Atlyginimas']
for every in listas:
    if every['Atlyginimas'] > atlgmax:
        atlgmax = every['Atlyginimas']


atlgmin = listas[1]['Atlyginimas']
for every in listas:
    if every['Atlyginimas'] < atlgmin:
        if every['Atlyginimas'] != 0:
            atlgmin = every['Atlyginimas']




atlg_suma1 = 0
atlg_kiekis1 = 0
atlg_suma2 = 0
atlg_kiekis2 = 0
atlg_suma3 = 0
atlg_kiekis3 = 0

for every in listas:
    if every['lygis'] in '1':
        atlg_suma1 += every['Atlyginimas']
        atlg_kiekis1 += 1
    elif every['lygis'] in '2':
        atlg_suma2 += every['Atlyginimas']
        atlg_kiekis2 += 1
    elif every['lygis'] in '3':
        atlg_suma3 += every['Atlyginimas']
        atlg_kiekis3 +=1

vidurkis1 = round((atlg_suma1/atlg_kiekis1),2)
vidurkis2 = round((atlg_suma2/atlg_kiekis2),2)
vidurkis3 = round((atlg_suma3/atlg_kiekis3),2)

# print(f'Apklaustuju gyvenami miestai:',setas_miestu)
# print(f'Vartojamos kalbos:',setas_kalbu)
# print(f'Didziausias atlyginmas:',atlgmax)
# print(f'Maziausias atlyginmas:',atlgmin)
# print(f'Alyginimu vidurkis yra:',vidurkis)
# print(f'Pirmo lygio specialtstu atlyginimu vidurkis:',vidurkis1)
# print(f'Antro lygio specialtstu atlyginimu vidurkis:',vidurkis2)
# print(f'Trecio lygio specialtstu atlyginimu vidurkis:',vidurkis3)

stringmiestu = ', '.join(setas_miestu)
stringkalbu = ', '.join(setas_kalbu)

with open('./uzd.txt','w', encoding="utf-8") as failas:
    failas.write('Miestai: ' + stringmiestu + '\n')
    failas.write('Programavimo kalbos: '+ stringkalbu + '\n')
    failas.write('Didziausias atlyginmas: '+ str(atlgmax) + '\n')
    failas.write('Maziausias atlyginmas: '+ str(atlgmin) + '\n')
    failas.write('Alyginimu vidurkis yra: '+ str(vidurkis) + '\n')
    failas.write('Pirmo lygio specialtstu atlyginimu vidurkis: '+ str(vidurkis1) + '\n')
    failas.write('Antro lygio specialtstu atlyginimu vidurkis: '+ str(vidurkis2) + '\n')
    failas.write('Trecio lygio specialtstu atlyginimu vidurkis: '+ str(vidurkis3) + '\n')
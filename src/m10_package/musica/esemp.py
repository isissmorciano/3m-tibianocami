# dict={}
# for i in range (5):

#     print(i)

#     dict['anno']= i

# print (dict)



# studenti = [
#     {"nome": "Alice", "voto": 8},
#     {"nome": "Bob", "voto": 7},
#     {"nome": "Carlo", "voto": 9}
# ]
    
# for i in studenti :
#     print (i['nome'])
#     i['voto'] = 90
    




# dizionario = {}

# dati = [{"Mario": 10}, {"Mario": 10}]


# for nome in dati:
#     dizionario['nome'] = nome['nome']

# print(dizionario)

lista = [
    {"nome": "Mario", "valore": 10},
    {"nome": "Luca", "valore": 20}
]

dizionario = {}

for elemento in lista:
    dizionario[elemento["nome"]] = elemento["valore"]

print(dizionario)
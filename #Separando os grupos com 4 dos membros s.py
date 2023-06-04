#Separando os grupos com 4 dos membros separados aleatoriamente

Membros = {
    "nome": [
        "Adriel Faustino de Oliveira",
        "Amanda Emi Yamasaki",
        "Ana Werneck de Souza Dias",
        "André Menniti Pennini",
        "Felipe de Souza Lourenço",
        "Fernanda Mayumi Sakamoto Iizuka",
        "Fernanda Mees Antunes",
        "Gabriel Grub Vidal da Silva",
        "Guilherme Vinicius Afonso Dias de Freitas",
        "Henrique Nogueira Pedro Lindoso",
        "Kim Ju Hyang",
        "Leticia Amy Siramidu",
        "Marcelo Tamay Honda",
        "Maria Dulce Navarro de Britto Matos",
        "Mateus Pamio Forcione de Oliveira e Souza",
        "Milena da Silva Ramos",
        "Paulo Sergio Almeida de Oliveira",
        "Theo Borten Radesca Migliano",
        "Vitor Tatiama Gouveia"
    ],
    "restricao": [
        "não",
        "não",
        "não",
        "sim",
        "não",
        "não",
        "sim",
        "sim",
        "não",
        "sim",
        "não",
        "não",
        "não",
        "não",
        "não",
        "não",
        "não",
        "não",
        "não"
    ]
}

restritos = []
naorestritos = []

for nome, restricao in zip(Membros["nome"], Membros["restricao"]):
    if restricao == "sim":
        restritos.append(nome)
    else:
        naorestritos.append(nome)

print(restritos)

print(naorestritos)



import random


cabeca1= random.choice(restritos)
print(cabeca1)

restritos.remove(cabeca1)
print(restritos)

cabeca2= random.choice(restritos)
print(cabeca2)

restritos.remove(cabeca2)
print(restritos)

cabeca3=random.choice(restritos)
print(cabeca3)


restritos.remove(cabeca3)
print(restritos)

cabeca4= restritos
print(cabeca4)

resto1 = random.sample(naorestritos, 3)
print(resto1)
grupo1 = [[cabeca1], resto1]
print(grupo1)

for nome in resto1:
    naorestritos.remove(nome)
print(naorestritos)

resto2 = random.sample(naorestritos, 4)
print(resto2)
grupo2 = [[cabeca2], resto2]
print(grupo2)

for nome in resto2:
    naorestritos.remove(nome)
print(naorestritos)

resto3 = random.sample(naorestritos, 4)
print(resto3)
grupo3 = [[cabeca3], resto3]
print(grupo3)

for nome in resto3:
    naorestritos.remove(nome)
print(naorestritos)

grupo4 = [[cabeca4], naorestritos]
print(grupo4)

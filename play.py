import random

# o 'r' no comeco significa tratar a string como "raw", ignorar special characters tipo \n
arquivo = open(r"Instrumental Ambient etc.txt", "r")
conteudo = arquivo.readlines()

# for x in conteudo:  # pra cada x em conteudo (x = 'artista\n')
# x = x[:-2]  # remove os 2 ultimos caracteres (o '\n)

conteudoFormatado = []

for x in conteudo[:-1]:  # não vamos mexer na útlima string porque ela vem sem '\n'

    # x[:-1] é a string x sem o ultimo elemento (o '\n', q apesar da notação é um elemento só)
    conteudoFormatado.append(x[:-1])
    # foi necessário porque x[:2] aparentemente só retorna uma cópia da string x


sorteado = random.choice(conteudoFormatado)
print('sorteado:', sorteado)

arquivo.close()

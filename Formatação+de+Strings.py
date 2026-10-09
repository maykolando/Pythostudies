nome = "Cintia Alves Moreira de Souza"

print(nome)
print("Total de caracteres: " + str(len(nome)))

print(nome[0])
print(nome[0:6])
print(nome[7:12])
print(nome[13:20])
print(nome[7:])

#----------------------------------

frase = "CUrSo de LóGica DE PROGramaçÃO PYthOn"

#upper retorna todas as letras em maiúscula
print(frase.upper())

#lower retorna todas as letras em minusculas
print(frase.lower())

#---------------------------------------

notaProva = "Tirei nota cinco na prova"

print(notaProva.replace("cinco", "DOZE"))

#---------------------------------------

cpf = "123.456.789-10"

cptPartes = cpf.split(".")

print(cptPartes)
print(cptPartes[0])
print(cptPartes[1])

cptPartes2 = cptPartes[2].split("-")
print(cptPartes2[0])
print(cptPartes2[1])

print("CPF: " + cptPartes[0] + cptPartes[1] + cptPartes2[0] + cptPartes2[1])
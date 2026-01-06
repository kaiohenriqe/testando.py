# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra usando manipulação de string
invertida = palavra[::-1]  
# 👍 Aqui usamos o recurso de fatiamento [::-1] que pega a string de trás pra frente.

# Compara a palavra original com a invertida
if palavra == invertida:
    print("A palavra é um palíndromo!")
    # ✅ Se forem iguais, significa que a palavra lida de trás pra frente é igual à original.
else:
    print("A palavra não é um palíndromo.")
    # ❌ Se forem diferentes, não é palíndromo.
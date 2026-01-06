string = input("Digite uma string: ")
# 👍 Solicita ao usuário uma string (texto). 
# Pode ser qualquer coisa: palavra, frase, até um caractere.

numero = int(input("Digite um número inteiro:"))
# 👍 Solicita um número inteiro. 
# Esse número será usado para definir quantas vezes a string será repetida.

repeticao = string * numero
# 👍 Multiplicar uma string por um número inteiro em Python repete a string várias vezes.
# Exemplo: "oi" * 3 → "oioioi"
# 💡 Se quiser deixar mais legível, pode adicionar espaço: (string + " ") * numero

print(repeticao)
# 👍 Exibe o resultado na tela.
# 💡 Se o número for grande, a saída pode ficar muito longa.
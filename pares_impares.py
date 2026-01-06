mao = int(input("Digite um número: "))  
# 👍 Aqui você está pedindo um número ao usuário e convertendo para inteiro.
# 💡 Dica: se quiser aceitar decimais, poderia usar float, mas para par/ímpar o int é ideal.

if mao % 2 == 0:  
    # 👍 O operador % calcula o resto da divisão por 2.
    # Se o resto for 0, significa que o número é par.
    print("O numero informado é Par")  
    # 💡 Pode melhorar a mensagem incluindo o próprio número: 
    # Exemplo: f"O número {mao} é Par"

else:  
    # 👍 Caso contrário (resto diferente de 0), o número é ímpar.
    print("O número informado é impar")  
    # 💡 Atenção: "impar" → o correto é "ímpar" com acento.
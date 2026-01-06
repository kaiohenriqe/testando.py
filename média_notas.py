nota = int(input("Digite a sua primeira nota do semestre: "))
# 👍 Solicita a primeira nota e converte para inteiro.
# 💡 Dica: se quiser aceitar notas com casas decimais (ex.: 7.5), use float em vez de int.

nota2 = int(input("Digite a sua segunda nota do semestre: "))
# 👍 Segunda nota, mesma lógica.

nota3 = int(input("Digite a sua terceira nota do semestre: "))
# 👍 Terceira nota, mesma lógica.

Total = (nota + nota2 + nota3) / 3
# ✅ Correto: soma todas as notas e divide por 3 para calcular a média.
# 💡 Sempre use parênteses para garantir que a soma seja feita antes da divisão.

print("Nota final:", Total)
# 👍 Exibe o resultado da média.
# 💡 Pode formatar para mostrar apenas duas casas decimais: por exemplo, 7.33 em vez de 7.333333...
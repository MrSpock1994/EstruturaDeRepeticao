"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""

print("******************CAIXA REGISTRADORA******************")
precos = []
n = 1
while True:
    precos.append(float(input(f"Digite o preço do {n}° produto: \n")))
    print("Deseja inserir outro produto?")
    print("Digite S para sim e N para não.")
    c = str(input("")).upper()
    if c == "N":
        break
    n += 1

total = sum(precos)
print(f"O valor total da compra foi de R$ {total}")
dinheiro = float(input("Digite o valor pago pelo cliente: \n"))
print(f"Troco:R$ {dinheiro - total}")

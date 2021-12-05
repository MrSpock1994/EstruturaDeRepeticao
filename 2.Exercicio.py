"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""
print('Informações do usúario, gentileza notar que a senha não pode ser igual ao usuario!!')
print()
user = input('Digite seu nome de usuario sem espaços e tudo minusculo: ').lower().strip()
senha = input('Digite sua senha sem espaços e tudo minusculo: ').lower().strip()
if user != senha:
    print("Dados validos!")

while user == senha:
    print('Você digitou a senha igual ao usuario, gentileza informar usuario e senha novamente!')
    user = input('Digite seu nome de usuario sem espaços e tudo minusculo. ').lower().strip()
    senha = input('Digite sua senha sem espaços e tudo minusculo: ').lower().strip
    if user != senha:
        print("Dados validos!")
        break

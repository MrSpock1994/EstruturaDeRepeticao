"""
Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

"""

A_habitantes = float(input('Digite o população do primeiro pais: '))
A_realtaxa = float(input('Digite a taxa de crescimento do primeiro pais em %: '))
A_taxa = A_realtaxa / 100

B_habitantes = float(input('Digite o população do segundo pais: '))
B_realtaxa = float(input('Digite a taxa de crescimento do segundo pais em %: '))
B_taxa = B_realtaxa / 100
anos = 0
A_crescimento = A_habitantes + (A_habitantes * A_taxa)
B_crescimento = B_habitantes + (B_habitantes * B_taxa)

if A_habitantes < B_habitantes and A_taxa > B_taxa:
    while A_crescimento < B_crescimento:
        A_crescimento = A_habitantes + (A_habitantes * A_taxa)
        B_crescimento = B_habitantes + (B_habitantes * B_taxa)
        A_habitantes = A_crescimento
        B_habitantes = B_crescimento
        anos = anos + 1
    print(anos)

if A_habitantes < B_habitantes and A_taxa <= B_taxa:
    print('De acordo com os dados inseridos, a população do primeiro pais \nnunca ultrapassa a do segundo ')


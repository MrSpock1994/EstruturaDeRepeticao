"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de  anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.

"""

A_habitantes = 80000
A_taxa = 0.03
B_habitantes = 200000
B_taxa = 0.015
anos = 0
A_crescimento = A_habitantes + (A_habitantes * A_taxa)
B_crescimento = B_habitantes + (B_habitantes * B_taxa)

while A_crescimento < B_crescimento:
    A_crescimento = A_habitantes + (A_habitantes * A_taxa)
    B_crescimento = B_habitantes + (B_habitantes * B_taxa)
    A_habitantes = A_crescimento
    B_habitantes = B_crescimento
    anos = anos + 1

print(anos)
linha1 = str(input())
linha2 = str(input())

vetor1 = linha1.split(' ', 2)
vetor2 = linha2.split(' ', 2)

valor = (float(vetor1[1])*float(vetor1[2])) + (float(vetor2[1])*float(vetor2[2]))
print('VALOR A PAGAR: R$ {:.2f}'.format((valor)))
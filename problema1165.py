def primo(i):
    j = 0
    div = 0
    while (j <= i):
        j = j + 1
        if (i % j == 0):
            div = div + 1

    if (div == 2):
        return True
    return False
  

cont = int(input())
vetor = []
contador = 0

while(contador < cont):
    num1 = int(input())
    vetor.append(num1)
    contador = contador + 1

for i in vetor:
    if(primo(i) == True):
        print(str(i) + " eh primo")
    else:
        print(str(i) + " nao eh primo")

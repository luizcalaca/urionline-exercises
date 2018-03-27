idade = int(input())

ano = int(idade) / int(365)
mes = (int(idade) - (int(ano)*int(365))) / int(30)
dias = (int(idade) - (int(ano)*int(365))) % int(30)

print("{:d} ano(s)".format(int(ano)))
print("{:d} mes(es)".format(int(mes)))
print("{:d} dia(s)".format(int(dias)))



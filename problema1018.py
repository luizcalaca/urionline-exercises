cedula = int(input())

nota100 = int(cedula) / int(100)
nota50 = int(cedula) % int(100) / 50
nota20 = ((int(cedula) % int(100)) % 50) / 20
nota10 = ((((int(cedula) % int(100)) % 50)) % 20) / 10
nota5 = (((((int(cedula) % int(100)) % 50)) % 20) % 10) / 5
nota2 = (((((((int(cedula) % int(100)) % 50)) % 20) % 10)) % 5) / 2
nota1 = (((((((int(cedula) % int(100)) % 50)) % 20) % 10)) % 5) % 2

print(int(cedula))  
print("{:d} nota(s) de R$ 100,00".format(int(nota100)))
print("{:d} nota(s) de R$ 50,00".format(int(nota50)))
print("{:d} nota(s) de R$ 20,00".format(int(nota20)))
print("{:d} nota(s) de R$ 10,00".format(int(nota10)))
print("{:d} nota(s) de R$ 5,00".format(int(nota5)))
print("{:d} nota(s) de R$ 2,00".format(int(nota2)))
print("{:d} nota(s) de R$ 1,00".format(int(nota1)))
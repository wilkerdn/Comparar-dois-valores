x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))
if(x>y):
	print("O maior valor é ",x)
elif(y>x):
	print("O maior valor é ", y)
else:
	print("Os dois possuem valores iguais, portanto o maior valor é %d", y)
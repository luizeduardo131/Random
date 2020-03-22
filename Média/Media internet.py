down = []
up = []
lat = []
b = 0
quant = int(input('Digite a quantidade de testes para ser realizados: \n'))
for i in range(0, quant):
	b += 1
	print("Teste número ", b)
	down.append(float(input("Digite o valor de download: \n")))
	up.append(float(input("Digite o valor de upload: \n")))
	lat.append(int(input("Digite a latência: \n")))
	print('\n')
	print('\n')
print('Os valores insideridos foram:\n')
for i in range(0, quant):
	print('Download: ', down[i], end = ' ')
	print('Upload: ', up[i], end = ' ')
	print('Latência: ', lat[i], end = ' ')
	#i =+1
	print('\n')

mediadown = sum(down)/len(down)
print("A média de download foi ", mediadown, "Mbps\n")
mediaup = sum(up)/len(up)
print("A média de upload foi ", mediaup, "Mbps\n")
medialat = sum(lat)/len(lat)
print("A média da latência foi ", medialat, "ms\n")

x = input('digite qualquer tecla para continuar...')
def getnum():
	nums = "234567890"
	letras = "abcdefghijklmnopqrstuvwxyz"
	tecladoConNumeros = [] 
	contador = 2
	contadorletras = 0 
	for i in range(len(letras)):
		if contadorletras == 3 and contador != 9 and  contador != 7 :
			contadorletras = 0
			contador += 1 
		elif contadorletras == 4 and (contador == 9 or  contador == 7): 
			contadorletras = 0
			contador += 1 
		tecladoConNumeros.append(str(contador)*(contadorletras+2))			
		contadorletras +=1
	return tecladoConNumeros
def palabranum(palabra):
	nums = getnum()
	print(nums)
	letras = "abcdefghijklmnopqrstuvwxyz"
	palbraenc = ""
	for ii in palabra:
		try:
			palbraenc += str(int(ii))
			palbraenc+=","
		except:
			pass
		for i in range(len(nums)):
			if ii == letras[i]:
				palbraenc += nums[i]
				palbraenc+=","
		if ii == " ":
			palbraenc += "00"
			palbraenc+=","
	return palbraenc
	
def main():
	print(palabranum("hola vas por buen camino el premio es una ... aprender esta codificacion ;-) "))
main()

#c0 = cantidadpalabras
#c-1%cantidad
palabra = list(input("palabra a invertir doble\n"))
cantidad = len(palabra)
c = cantidad-1
#nuevaPalabra = [""]*cantidad
nuevaPalabra = []
for i in range(c+1):
	c = (c-1)%cantidad
	print(c,palabra[c],cantidad)
	#nuevaPalabra[c] = palabra[i]
	nuevaPalabra.append(palabra[c])
print(*nuevaPalabra)
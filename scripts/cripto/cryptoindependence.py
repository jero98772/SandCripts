from random import randint # not is needed , you can replace with pserandom.py 
chars2 = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNÑOPQRSTUVWXYZ[\\]^_`abcdefghijklmnñopqrstuvwxyz{|}~"
letras = "abcdefghijklmnopqrstuvwxyz"
nums = "234567890"
numcode = ['22', '222', '2222', '33', '333', '3333', '44', '444', '4444', '55', '555', '5555', '66', '666', '6666', '77', '777', '7777', '77777', '88', '888', '8888', '99', '999', '9999', '99999']
mcm = lambda num1, num2:num1 * num2/ mcd(num1, num2)
def mcd(num1, num2):
    resto = 0
    while(num2 > 0):
        resto = num2
        num2 = num1 % num2
        num1 = resto
    return num1
def mayor(num1,num2):
	if num1>num2:
		return num1
	else:
		return num2
def menor(num1,num2):
	if num1<num2:
		return num1
	else:
		return num2
def isPrime(inputnum):
	if inputnum < 2:
		return False
	for i in range(2,inputnum-1):
		if inputnum % i== 0 :
			return False
			break
	else :
	    return True
def getrndPrime(limit):
	#un buen primo es aquel que de 20191231 en un dataset
	modnum = int(str(limit)[-4:])
	num1 = randint(0,limit) % modnum
	num2 = (num1 +limit) % modnum
	numMayor = mayor(num1, num2)
	numMenor = menor(num1, num2)
	for i in range(numMenor, numMayor):
		if isPrime(i):
			return i
			break
def rndkey():
	return  randint(0,2**20)
def unpad(s):
	return s[:-ord(s[len(s) - 1:])]
def pad(s):
	size = 16
	s = str(s)
	return s + (size - len(s) % size) * chr(size - len(s) % size)
def cifrarcesar(text,key = rndkey, chars=chars2):
    cifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char) + key
            mod = int(num) % len(chars)
            cifrar = cifrar + (chars[mod])
    return  str(cifrar) 
def descifrarcesar(text,key = rndkey,chars=chars2):
    descifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char ) - key
            mod = int(num) % len(chars)
            descifrar = descifrar + str(chars[mod])
    return str(descifrar)
def publicKeyE(fi):
	e = 0
	for i in range(2,fi):
		if  mcd(fi,i) == 1 :
			e = i
			break
	return e
def privateKeyD(e,fi):
	i = 2
	while True:
		formula = (1+fi*i)%e
		d = int((1+fi*i)/e)
		if (formula == 0 and d != e):
			return d
		i += 1
def genprimes(limit):
    prime1 = getrndPrime(limit)
    prime2 = getrndPrime(limit)
    return prime1, prime2
def genKey(key1,key2):
	n = key1 * key2
	fi = (key1 - 1 ) * (key2 - 1 )
	base = key1 * key2 - key1 - key2 + 1 
	publica = publicKeyE(fi)
	privada = privateKeyD(publica , fi)
	return n , publica , privada
def encryptRsa(msg,e,n):
	cifrate = []
	for i in msg:	
		value = int(chars2.index(i))
		enchar = (value**int(e))%int(n)
		cifrate.append(enchar)
	return cifrate
def decryptRsa(cifrate,d,n):
	msg = ""
	d = int(d)
	n = int(n)
	cifrate = eval(str(cifrate))
	for value in cifrate:
		dechar = int((int(value)**d)%n)
		msg += chars2[dechar]
	return msg
def getnum():
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
def encpalabranum(palabra):
	palabraenc = ""
	for i in palabra:
		try:
			palabraenc += str(int(i))
			palabraenc+=","
		except:
			pass
		for ii in range(len(numcode)):
			if i == letras[ii]:
				palabraenc += numcode[ii]
				palabraenc+=","
		if i == " ":
			palabraenc += "00"
			palabraenc+=","
	return ","+palabraenc
def decpalabranum(palbraenc):
	palabra = ""
	caracter = ""
	for i in palbraenc:
		if i ==  ",":
			if caracter == "00":
				palabra += " "
			else:
				try:
					palabra += letras[numcode.index(caracter)]
				except:
					palabra += str(caracter)
			caracter = ""
		else:
			caracter+=i
	return palabra

from subprocess import run 
from time import sleep
text2 = "Los estilos de vida son la llave que abre el candado de las cadenas de la vida , esta llave te encadenara a la cultura con la que identifiques y protejera  a quienes amas"
asciiart= """
       CCCCCC            
     CCCC   CC           
     CC      CC          
    CC        CC    C    
    C          C    C    
    C          C    CC   
   CCCCCCCCCCCCCC   CCC  
   CCCCCCCCCCCCCC   C    
   CCCCCCCCCCCCCC   C    
   CCCCCCCCCCCCCC   C    
   CCCCCCCCCCCCCC   C    
   CCCCCCCCCCCCCC   C    
   CCCCC   CCCCCC  CCC   
   CCCCC    CCCCC C  CC  
   CCCCCC  CCCCCC C   C  
   CCCCCCCCCCCCCC CC CC  
   CCCCCCCCCCCCCC  CCC   
"""
chars = "abcdefghijklmnopqrstuvwxyz "
textC ="ruyfkyzoruyfjkfaojgfyutfrgfrrgakfw kfghxkfkrfigtjgjufjkfrgyfigjktgyfjkfrgfaojgfffkyzgfrrgakfzkfktigjktgxgfgfrgfi rz xgfiutfrgfw kfojktzolow kyfdfvxuzkpkxgffgfw oktkyfgsgyf"
key =33
toCompleate = 0
jumps = 34
def cifrarcesar(text,key = key, chars=chars):
    cifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char) + key
            mod = int(num) % len(chars)
            cifrar = cifrar + (chars[mod])
    return  str(cifrar) 
def descifrarcesar(text,key = key,chars=chars):
    descifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char ) - key
            mod = int(num) % len(chars)
            descifrar = descifrar + str(chars[mod])
    return str(descifrar)
def descifrarcesarAnimation(text,key = key,chars=chars):
    descifrar = text
    text = str(text)
    animation = list(text)
    for i in range(len(text)+toCompleate):
           # print()
            char = text[i]
            num = chars.find(char ) - key
            mod = int(num) % len(chars)
            animation[i] =  str(chars[mod])
            descifrar = descifrar + str(chars[mod])
            run("clear",shell =True)
            #print(asciiart)
            print("\033[92m"+asciiart+"\033[00m")
            j=0
            while j<len(text)+toCompleate:
                textAnimation = "".join(animation[j-jumps:j:])
                print(textAnimation)
                j+=jumps
            #print("".join(animation[j-jumps:j:]))
            j=0
            sleep(0.05)
    return str(descifrar) 
print(asciiart)
#txt=cifrarcesar(text2,33,chars);print(txt)
descifrarcesarAnimation(textC,33,chars)
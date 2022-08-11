#sort acepta UNICAMANTE listas, mientras que sorted acepta cualquier tipo de cosa

numeros_ordenados=sorted([2,7,6,1,5,9])
print("etsa lista esta ordenada", numeros_ordenados)

numeros_ordenados=sorted([2,7,6,1,5,9] ,reverse=True)
print("esta lista esta en forma ascendente", numeros_ordenados)


enunciado="me llamo alejo"
print(len(enunciado))


estudiantes= [
    ("daniela" , 19),
    ("alejo" , 20)
]
print(sorted(estudiantes , reverse=True))

nombres=["martin","alejo","dardo"]
nombres.sort()
print(nombres)

def esta_ordenada():
    esta_ordenada=int(input("dame algun elemento: "))
    indice=1
    while esta_ordenada<indice:
        print("hola mundo")
        break
    else:
        print("de baja")
esta_ordenada()






    

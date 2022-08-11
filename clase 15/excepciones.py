sumar = lambda numero,suma: numero+suma

def suma_de_elementos (suma=0):
    while True:
        try:
            cantidad_de_elementos=int(input("ingrese un numero: "))
            
        except ValueError:
            print("ingrese numeros, no palabras")
        except Exception as e:
            print(type(e).__name__)
        else:
            break
        finally:
            print("Ahora siga las instrucciones")
    
    
    for i in range(cantidad_de_elementos):
        while True:
            try:
                numero=int(input("ingrese el otro numero: "))
                
            except:
                print("por favor ingrese un numero")
            else:
                break

        
        suma=(numero+suma)
    print(f"la suma es de {suma}")

suma_de_elementos()


def dividir():
    while True:
        try:
            numero=int(input("ingrese un numero: "))
            division= 50/numero
            print(division)
            break
        except ValueError:
            print("ingrese numeros, no textos")
        except ZeroDivisionError:
            print("no se puede dividir por cero")
        except Exception as e:
            print(type(e).__name__)
dividir()
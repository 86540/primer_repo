def dividir (num1,num2):
    try:
        resultado=(num1/num2)
        return resultado
    except TypeError:
        return "no ingresar texto"
    except ZeroDivisionError:
        return "no dividir por cero"
    finally:
        print("bienvenido a la funcion dividir")
resultado=dividir(10,5)
print(f"el resultado es {resultado}")
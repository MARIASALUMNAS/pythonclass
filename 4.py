#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("Convertir GRADOS CELSIUS A FAHRENHEIT")
    numero_1 = float(input("Escriba un número: "))
    media = (numero_1 ) * 9.0/5.0 + 32
    
    print("El paso de grados celsius a grados fahrenheit  {} es {}".format(numero_1,media))
 
if __name__ == "__main__":
    main()


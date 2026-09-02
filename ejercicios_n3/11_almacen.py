""" 
11. En un almacen estan buscando la forma de hacer los cobros mas automáticamente. 
Para esto, se nos pide crear una función que reciba un número entero que 
representa lo que hay que cobrar, le pida al usuario ingresar un monto, y se vaya 
mostrando por pantalla cuánto falta para completar el pago. Repetir este proceso 
hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30: 
> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.  
2 
 
> 10 
> El importe a pagar es de 20 pesos. Por favor, ingrese un monto. 
> 15 
> El importe a pagar es de 5 pesos. Por favor, ingrese un monto. 
> 5  
"""

def cobro(deuda_inicial):
    deuda = deuda_inicial
    while deuda > 0:
        pago = int(input(f"El importe a pagar es de {deuda}. Por favor, ingrese un monto: "))
        deuda = deuda - pago
    print("Pagaste la deuda!")


monto = int(input("Ingrese un monto: "))
cobro(monto)
# 14. Se tiene un ticket de supermercado que se puede representar como una lista de tuplas 
# (producto, precio). 
# a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que 
# pagar.  
# b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.  
# 2 
# Pensamiento computacional (090) Cátedra Balbiano 
 
# Un ejemplo de lista puede ser: [(“Detergente”, 123), (“Jabón Líquido”, 456)] y nos tendría 
# que devolver 579. (No copien y peguen la lista de la guía, porque hay caracteres que no 
# los va a reconocer el editor de texto). 

ticket_1 = [("Leche", 3.99), ("Ravioles", 2.99), ("Manteca", 1.99)]
ticket_2 = [("Azucar", 2.76), ("Yogurt", 5.99)]

def calcular_total(ticket):
    total = 0
    for producto, precio in ticket:
        total = total + precio
    return total

def juntar_tickets(ticket_a, ticket_b):
    combinar_ticket = ticket_a + ticket_b

    total_gral = calcular_total(combinar_ticket)
    return total_gral

ticket1 = calcular_total(ticket_1)

print("Total: ", ticket1)

union_tickets = juntar_tickets(ticket_1, ticket_2)
print("El total de sus dos ticket es: ", union_tickets)
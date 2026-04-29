from descuento import calcular_descuento, calcular_total_con_descuento, obtener_porcentaje_descuento

def menu():
    print("=== Sistema de Descuentos ===")
    
    try:
        total = float(input("Ingrese el total de la compra: "))
        
        descuento = calcular_descuento(total)
        total_final = calcular_total_con_descuento(total)
        porcentaje = obtener_porcentaje_descuento(total)

        print(f"Descuento aplicado del {porcentaje}%: ${descuento}")
        print(f"Total a pagar: ${total_final}")


    except ValueError:
        print("Error: Ingrese un número válido")


if __name__ == "__main__":
    menu()

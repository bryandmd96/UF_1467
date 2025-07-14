
menu = {"Pizza Margarita" : 8.99, "Hamburguesa Clásica": 5.99, "Ensalada César": 7.5, "Agua Mineral": 1.5}

def place_order(selected_food, money):
    try: 
        if selected_food not in menu:
            raise ValueError("El alimento seleccionado no está en el menú")

        preci = menu[selected_food]
        if preci > money:
            raise ValueError("No se disponen de suficientes fondos para realizar el pedido")
            
        total_price = preci
        print(f"Pedido realizado con éxito. Alimento seleccionado: {selected_food}, Total a pagar: {total_price} €")

    except ValueError as error:
        print(f"Error en el pedido: {error}")
        
    print("------" * 20)
      

def main():
    print("------" * 20)
    print("Hola! Bienvenido al restaurante Fercho. \nAqui esta el menú:")
    for key, value in menu.items():
        print(f"{key} : {value}")
    print("------" * 20)
    
    fine = True
    while fine == True:
        try:
            money = float(input("De cuanto dinero dispones: "))
            fine = False
        except ValueError:
            print("Debe ser una cantidad real")
    
    print(f"{money}€")
    selected_food = str(input("Seleccione un producto a consumir: ")).title()
    print(f"Producto seleccionado: {selected_food}")
    

    place_order(selected_food, money)

    

if __name__ == "__main__":
    main()
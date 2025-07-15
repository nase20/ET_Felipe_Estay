productos = {'C-123'.upper(): ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
        'C-111'.upper(): ['LENOVO', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
        'C-234'.upper(): ['ASUS', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
        'C-456'.upper(): ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
        'C-1222'.upper(): ['ASUS', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
        'C-477'.upper(): ['LENOVO', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
        'C-334'.upper(): ['LENOVO', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
        'C-2906'.upper(): ['DELL', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'C-123'.upper(): [387990,10], 
        'C-111'.upper(): [327990,4], 
        'C-234'.upper(): [424990,1],
        'C-456'.upper(): [664990,21], 
        'C-477': [290890,32], 
        'C-334'.upper(): [444990,7],
        'C-1222'.upper(): [749990,2], 
        'C-2906'.upper(): [349990,1]}
def buscar_stock(lst_productos,lst_stock, marca_buscada)->int:
        for codigo, datos in lst_productos.items():
                if datos[0]==marca_buscada:
                        print(lst_stock[codigo][1])
                        
def actualizar_precio(lst_stock:dict, precio:int, codigo:str)->bool:
        if codigo not in lst_stock:
                return False
        lst_stock[codigo][0]=precio
        return True
def buscar_precio(lst_productos:dict, lst_stock:dict, p_min:int, p_max:int)->None:
        for codigo, datos in lst_stock.items():
                if datos[0]>p_min and datos[0]<p_max:
                        print(lst_productos[codigo])
                        print(lst_productos[codigo][0])
while True:
        print("""
        -------- Menu de compra------------
        1.- consultar stock de una marca especifica.
        2.- buscar prroductos por rango de precio.
        3.- actualizar precio de un producto.
        4.- salir.
        """)
        try:
                opcion=int(input("seleccione una opcion: "))
                if opcion==1:
                        marca=input("seleccione una marca: ").upper()
                        buscar_stock(productos, stock, marca)
                elif opcion==2:
                        precio_min=int(input("ingrese precio minimo: "))
                        precio_maximo=int(input("ingrese precio maximo: "))
                        buscar_precio(productos, stock, precio_min, precio_maximo)
                elif opcion==3:
                        code=(input("codigo producto a actualizar: ")).upper()
                        prec=int(input("ingrese nuevo precio: "))
                        if actualizar_precio(stock,prec, code ):
                                print("precio actualizado")
                        else:
                                print("no paso")
                elif opcion==4:
                        break
        except:
                print("ingrese una opcion valida.")

productos = {
   
}

categorias = {
   
}

diccionario = {
   
}

noC = int(input("digite el número de categorías\n"))
for noC in range(noC):
    categorias[noC+1] = {
    "nombreC" : input("escriba el nombre de la categoría\n"),
    "id" : int(input("digite el id de la categoría\n"))
    }
    
    
print(categorias)

noP = int(input("digite el número de productos\n"))
for noP in range(noP):
    productos[noP + 1] = {
    "nombre" : input("escriba el nombre del producto\n"),
    "precio" : int(input("digite el precio del producto\n")),
    "id_categoria" : int(input("digite el id de la categoría\n"))
    }
    
print(productos)

for x in range(len(categorias)):
    for y in range(len(productos)):
        if (categorias[x+1]["id"] == productos[y+1]["id_categoria"]):
            diccionario[y + 1] = {
                "name" : productos[y+1]["nombre"],
                "precio" : productos[y+1]["precio"],
                "nameC" : categorias[x+1]["nombreC"]
            }
        
print(diccionario)
import os

opciones={
    1: ["Diego Montalvo","Programador, Viajar, Bicleta"],
    2: ["Programadora 1","Estudiar, Anime"],
    3: ["Programadora 2","Dibujar, Cantar"]
}
def mostrar_integrantes():
    print("Las integrantes del club de programadoras 2023 son : \n")
    for valor in opciones.values():
        print(f"Nombre : {valor[0]}\nHobbies : {valor[1]}\n")







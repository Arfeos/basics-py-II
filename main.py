from libreria import agregar_libro, listar_libros, libros_por_autor, existe_libro
#  Añade una colección de libros
libros = [
    agregar_libro("Harry Potter", "J.K. Rowling"),
    agregar_libro("Harry Potter 2", "J.K. Rowling"),
    agregar_libro("1984", "George Orwell"),
    agregar_libro("El Hobbit", "J.R.R. Tolkien")
]

# Muestra la colección de libros creada
print(listar_libros(libros))

# Busca un libro por el autor
print(libros_por_autor(libros, "J.K. Rowling"))

# Verifica si un libro está disponible

print(existe_libro(libros, "1984"))
print(existe_libro(libros, "Drácula"))
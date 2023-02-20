from ipclass import clasificador

print("\nCLASIFICADOR DE IP\n")

ip = str(input("Ingrese la direccion IP: "))
resultado =  clasificador(ip)

print("Su resultado es: ")
print(resultado)
print("\n\n")
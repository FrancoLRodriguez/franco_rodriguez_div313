


consumo = int(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial, Industrial): ")

cargo_fijo = 7000
costo_m3 = 200
bonificacion = 0
recargo = 0
subtotal = consumo * costo_m3 + cargo_fijo

match tipo_cliente:
    case "Residencial":
        if consumo <= 30:
            bonificacion = subtotal * 0.10
        elif consumo > 80:
            recargo = subtotal * 0.15
    case "Comercial":
        if consumo > 150:
            bonificacion = subtotal * 0.08
        elif consumo > 300:
            bonificacion = subtotal * 0.12
        elif consumo < 50:
            recargo = subtotal * 0.05
    case "Industrial":
        if consumo > 500:
            bonificacion = subtotal * 0.20
        elif consumo > 1000:
            bonificacion = subtotal * 0.30
        elif consumo < 200: 
            recargo = subtotal * 0.10
    case _:
        print("tipo de cliente no valido")

subtotal_ajustado = subtotal - bonificacion + recargo


if(subtotal < 35000):
    bonificacion_especial = bonificacion + (subtotal * 0.05)
    descuento_especial = subtotal_ajustado * 0.05
    subtotal_ajustado -= descuento_especial

iva = subtotal_ajustado * 0.21
total = subtotal_ajustado + iva

# --- Salida ---
print(f"\nSubtotal base (sin ajustes ni IVA): ${subtotal}")
if bonificacion:
    print(f"Bonificación aplicada: ${bonificacion}")
if recargo:
    print(f"Recargo aplicado: ${recargo}")
if descuento_especial:
    print(f"Descuento especial (Residencial): ${descuento_especial}")
print(f"Subtotal con ajustes (antes de IVA): ${subtotal_ajustado}")
print(f"IVA (21%): ${iva}")
print(f"El total a pagar es: ${total}")

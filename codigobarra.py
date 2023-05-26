import barcode
from barcode.writer import ImageWriter

def generate_barcode(number):
    # Convierte el número en una cadena de texto
    number_str = str(number)

    # Crea un objeto Code 128 con el número proporcionado
    code128 = barcode.Code128(number_str, writer=ImageWriter())

    # Genera el código de barras y guarda la imagen en un archivo
    filename = f'barcode_{number_str}.png'
    code128.save(filename)

    print(f"El código de barras {number_str} ha sido generado correctamente.")

start_number = 10820231000
end_number = 10820231200

for number in range(start_number, end_number + 1):
    generate_barcode(number)
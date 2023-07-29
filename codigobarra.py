import barcode
from barcode.writer import ImageWriter

def generate_barcode(number):
    # Convert the number to a string
    number_str = str(number)

    # Create a Code 128 barcode object with the given number
    code128 = barcode.Code128(number_str, writer=ImageWriter())

    # Generate the barcode and save the image to a file
    filename = f'barcode_{number_str}.png'
    code128.save(filename)

    print(f"The barcode {number_str} has been generated successfully.")

start_number = 10820231000
end_number = 10820231200

for number in range(start_number, end_number + 1):
    generate_barcode(number)

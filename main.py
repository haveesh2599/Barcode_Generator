import barcode

from barcode.writer import ImageWriter

data = input("Enter code, text or URL: ")

barcode.get('code128', data, 
            writer=ImageWriter()).save('barcode')

print("Barcode generated and is saved")
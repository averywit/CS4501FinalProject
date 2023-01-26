import hashlib
import base64
from io import BytesIO
from PIL import Image
from colorama import Fore

image = input("Enter the image you would like modified: ")

buffered1 = BytesIO()
original_image = Image.open(image)
original_image.save(buffered1, format="JPEG")
original_hash = hashlib.sha256(base64.b64encode(buffered1.getvalue())).hexdigest()

buffered2 = BytesIO()
modified_image = Image.open(image)
modified_image = modified_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
modified_image.save(buffered2, format="JPEG")
modified_hash = hashlib.sha256(base64.b64encode(buffered2.getvalue())).hexdigest()
modified_image.save("/Users/avery/Downloads/personal/Modified.jpg")

print("")
print(Fore.RESET + "Original hash: " + Fore.GREEN + original_hash)
print(Fore.RESET + "Modified hash: ", end="")

i = 0
count = 0
while i < len(original_hash):
    if original_hash[i] != modified_hash[i]:
        print(Fore.RED + modified_hash[i], end="")
        count += 1
    else:
        print(Fore.GREEN + modified_hash[i], end="")
    i += 1

print("\n")
print(Fore.RESET + "Hamming distance: " + Fore.RED + str(count))

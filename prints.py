from colorama import Fore
def print_inputs(version):
    if version == 0:
        option = input(Fore.WHITE+"(1) - Encode\n(2) - Decode\n(3) - Exit\n\n>>> ")
        return option
    if version == 1:
        option = input(Fore.WHITE+"\n(0) - Return to main menu\n(1) - Text to Text\n(2) - Text to Image\n(3) - Image to Image\n(4) - Image to Text\n(5) - Exit\n\n>>> ")
        return option
    if version == 2:
        option = input(Fore.WHITE+"\n(0) - Return to Encode Menu\n(1) - Grayscale to Grayscale\n(2) - Grayscale to Color\n(3) - Color to Color\n(4) - Color to Grayscale\n(5) - Exit\n\n>>> ")
        return option
    if version == 3:
        option = input(Fore.BLUE+"(1) - Grayscale to Text\n(2) - Color to Text\n\n"+Fore.WHITE+">>> ")
        return option
    if version == 4:
        option = input(Fore.WHITE+"\n(0) - Return to main menu\n(1) - Text to Text\n(2) - Image to Text\n(3) - Image to Image \n(4) - Text to Image\n(5) - Exit\n\n>>> ")
        return option
    if version == 5:
        text = input(Fore.BLUE+"\n\nEnter text to encrypt:\n"+Fore.WHITE+">>> ")
        return text
    if version == 6:
        rotation = int(input(Fore.BLUE+"\nRotation:\n"+Fore.WHITE+">>> "))
        return rotation
    if version == 7:
        saveToFile = input(Fore.BLUE+"\nSave the encrypted text to an external file? [Y/N]\n"+Fore.WHITE+">>> ").upper()
        return saveToFile
    if version == 8:
        path = input(Fore.BLUE+"\nEnter path to save the file:\n"+Fore.WHITE+">>> ")
        return path
    if version == 9:
        name = input(Fore.BLUE+"\nEnter a name for the file:\n"+Fore.WHITE+">>> ")
        return name
    if version == 10:
        text_path = input(Fore.BLUE+"\n\nEnter path to file:\n"+Fore.WHITE+">>> ")
        return text_path
    if version == 11:
        width = int(input(Fore.BLUE+"\nImage width: \n"+Fore.WHITE+">>> "))
        return width
    if version == 12:
        height = int(input(Fore.BLUE+"\nImage height: \n"+Fore.WHITE+">>> "))
        return height
    if version == 13:
        extension = input(Fore.BLUE+"\nChoose extension:\n(1) - TXT\n(2) - PDF\n"+Fore.WHITE+">>> ")
        return extension
    if version == 14:
        xorInt = int(input(Fore.BLUE+"\nXOR: \n"+Fore.WHITE+">>> "))
        return xorInt
    if version == 15:
        text = input(Fore.BLUE+"\n\nEnter text to decrypt:\n"+Fore.WHITE+">>> ")
        return text
    if version == 16:
        saveToFile = input(Fore.BLUE+"\nSave the decrypted text to an external file? [Y/N]\n"+Fore.WHITE+">>> ").upper()
        return saveToFile
    if version == 17:
        pxUse = int(input(Fore.BLUE+"\nPixels to use: \n"+Fore.WHITE+">>> "))
        return pxUse
    if version == 18:
        substraction_val = int(input(Fore.BLUE+"\nSubstraction value: \n"+Fore.WHITE+">>> "))
        return substraction_val
    if version == 19:
        savePixels = input(Fore.BLUE+"\nSave the pixel output in the name of the image? [Y/N]: \n"+Fore.WHITE+">>> ").upper()
        return savePixels
    if version == 20:
        img_ext = input(Fore.BLUE+"\nChoose extension for the output image:\n(1) - JPG\n(2) - PNG\n\n"+Fore.WHITE+">>> ")
        return img_ext
    if version == 21:
        colormode = input(Fore.BLUE+"\nColor space of the image:\n(1) - Grayscale\n(2) - RGB\n\n"+Fore.WHITE+">>> ")
        return colormode

def print_outputs(version, path="", pixelOutput="", hex_output="", numPixels="", subsVal=""):
    if version == 0:
        print(Fore.GREEN+f"\nThe file has been saved to {path}")
    if version == 1:
        print(Fore.GREEN+f"\nFor decrypting use the first {pixelOutput} pixels")
    if version == 2:
        print(Fore.GREEN+f"\nEncrypted text:\n {hex_output}")
    if version == 3:
        print(Fore.GREEN+f"\nFor decrypting use the first {numPixels} pixels")
    if version == 4:
        print(Fore.GREEN+f"\nSubstraction Value: {subsVal}")
    
def print_plain(version):
    if version == 0:
        print(Fore.WHITE+"\n[:[:[: GOODBYE :]:]:]")
    if version == 1:
        print(Fore.WHITE+"Encode Menu\n-------------------------------")
    if version == 2:
        print(Fore.WHITE+"Decode Menu\n-------------------------------")
    if version == 3:
        print(Fore.WHITE+"Image to Image\n-------------------------------")
    if version == 4:
        print(Fore.WHITE+"Image to Text\n-------------------------------")
    if version == 5:
        print(Fore.WHITE+"Text to Text\n-------------------------------")
    if version == 6:
        print(Fore.WHITE+"Text to Image\n-------------------------------")
    if version == 7:
        print(Fore.WHITE+"\nEncrypted Text:\n")
    if version == 8:
        print(Fore.WHITE+"\nImage Parameters:")
    if version == 9:
        print(Fore.RED+"\nThe file you selected is not readable.")
    if version == 10:
        print(Fore.RED+"\nThe path is invalid.")
    if version == 11:
        print(Fore.WHITE+"\nDecrypted Text: \n")
    if version == 12:
        print(Fore.RED+"\nThe size of the image is not enough to contain the entire text.")
    if version == 13:
        print(Fore.RED + "\nWarning! This process may require a lot of computing power...")
    if version == 14:
        print(Fore.BLUE+"\nChoose one option: ")

def print_process(version):
    if version == 0:
        print(Fore.YELLOW+"\n[+] Extracting image data...")
    if version == 1:
        print(Fore.YELLOW+"\n[+] Compressing pixel data...")
    if version == 2:
        print(Fore.YELLOW+"\n[+] Reconstructing decrypted image...")
    if version == 3:
        print(Fore.YELLOW+"\n[+] Analyzing pixel data...")
    if version == 4:
        print(Fore.YELLOW+"\n[+] Generating string replacements...")
    if version == 5:
        print(Fore.YELLOW+"\n[+]Applying first XOR...")
    if version == 6:
        print(Fore.YELLOW+"\n[+]Applying ROT...")
    if version == 7:
        print(Fore.YELLOW+"\n[+]Applying second XOR...")
#!/usr/bin/env python3
import os
import pdfkit
from pdfminer.high_level import extract_text
from logo import *
from level3_menus import *
from prints import *
from encode import *
from decode import *
from colorama import Fore
from tqdm import tqdm

optionsPDF = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'margin-right': '0.75in',
    'encoding': "UTF-8",
    'quiet': ''
}

# LEVEL 0 MENU
#--------------------------------------------------------------------------------------

def menu_main():
    option = print_inputs(0)
    if option == "1":
        menu_encode()
    elif option == "2":
        menu_decode()
    elif option == "3":
        print_plain(0)
        exit()
    else:
        os.system("clear")
        printIntro()
        menu_main()
    return option

# LEVEL 1 MENUS
#--------------------------------------------------------------------------------------

def menu_encode():
    os.system("clear")
    print_plain(1)
    option = print_inputs(1)
    if option == "0":
        os.system("clear")
        printIntro()
        menu_main()
    elif option == "1":
        os.system("clear")
        menu_text_to_text(method="encode")
    elif option == "2":
        os.system("clear")
        menu_text_to_image(method="encode")    
    elif option == "3":
        os.system("clear")
        print_plain(3)
        menu_image_to_image(method="encode")
    elif option == "4":
        os.system("clear")
        print_plain(4)
        menu_image_to_text(method="encode")
    elif option == "5":
        print_plain(0)
        exit()
    else:
        os.system("clear")
        menu_encode()

def menu_decode():
    os.system("clear")
    print_plain(2)
    option = print_inputs(4)
    if option == "0":
        os.system("clear")
        printIntro()
        menu_main()
    elif option == "1":
        os.system("clear")
        print_plain(5)
        menu_text_to_text(method="decode")
    elif option == "2":
        os.system("clear")
        print_plain(4)
        menu_image_to_text(method="decode")
    elif option == "3":
        os.system("clear")
        print_plain(3)
        menu_image_to_image(method="decode")
    elif option == "4":
        os.system("clear")
        menu_text_to_image(method="decode")
    elif option == "5":
        print_plain(0)
        exit()
    else:
        os.system("clear")
        menu_decode()

# LEVEL 2 MENUS
#--------------------------------------------------------------------------------------


def menu_text_to_text(method):
    if method == "encode":
        print_plain(5)
        option_text = menu_text_input(method_m="Encode")
        if option_text == "0":
            os.system("clear")
            menu_encode()
        elif option_text == "1":
            os.system("clear")
            print_plain(5)
            text = print_inputs(5)
            rotation = print_inputs(6)
            xorInt = print_inputs(14)
            saveToFile = print_inputs(7)
            string = replace_s(text)
            hex = xorString(string, 13)
            rotHex = rot(hex, DIC, rotation)
            hex_output = xorHex(rotHex, xorInt)
            if saveToFile == "N":
                print_outputs(2, "", "", hex_output)
            elif saveToFile == "Y":
                path = print_inputs(8)
                if not path.endswith("/"):
                    path += "/"
                if not path.startswith("/"):
                    path = "/"+path
                name = print_inputs(9)
                extension = print_inputs(13)
                if extension == "1":
                    ext = ".txt"
                    outputpath = path + name + ext
                    with open(outputpath, "a", encoding="utf-8") as f:
                        f.write(hex_output)
                elif extension == "2":
                    ext = ".pdf"
                    outputpath = path + name + ext
                    pdfkit.from_string(hex_output, outputpath, options = optionsPDF)
                print_outputs(0, path)
            elif saveToFile != "Y" and saveToFile != "N":
                os.system("clear")
                menu_text_to_text()
        elif option_text == "2":
            os.system("clear")
            print_plain(5)
            text_path = print_inputs(10)
            if not text_path.startswith("/"):
                text_path = "/"+text_path
            rotation = print_inputs(6)
            xorInt = print_inputs(14)
            saveToFile = print_inputs(7)
            LINES = []
            if text_path.endswith(".txt"):
                with open(text_path, "r", encoding="utf-8") as f:
                    file = f.readlines()
                    for l in file:
                        LINES.append(l)
            elif text_path.endswith(".pdf"):
                file = extract_text(text_path)
                LINES = file.split("\n")
            OUTPUT = []
            for l in LINES:
                string = replace_s(l)
                hex = xorString(string, 13)
                rotHex = rot(hex, DIC, rotation)
                hex_output = xorHex(rotHex, xorInt)
                OUTPUT.append(hex_output)
            if saveToFile == "N":
                print_plain(7)
                for line in OUTPUT:
                    print(line)
            elif saveToFile == "Y":
                path = print_inputs(8)
                if not path.endswith("/"):
                    path += "/"
                if not path.startswith("/"):
                    path = "/"+path
                name = print_inputs(9)
                extension = print_inputs(13)
                with open(path+name+".txt", "a", encoding="utf-8") as f:
                    for line in OUTPUT:
                        f.write(line)
                if extension == "1":
                    ext = ".txt"
                    print_outputs(0, path)
                elif extension == "2":
                    ext = ".pdf"
                    pdfkit.from_file(path+name+".txt", path+name+ext, options = optionsPDF)
                    os.remove(path+name+".txt")
                    print_outputs(0, path)
                elif extension != "1" and extension != "2":
                    extension = print_inputs(13)
            elif saveToFile != "N" and saveToFile != "Y":
                menu_text_to_text(method)
        elif option_text == "3":
            print_plain(0)
            exit()
        else:
            os.system("clear")
            menu_text_to_text()
    elif method == "decode":
        os.system("clear")
        print_plain(5)
        option_text = menu_text_input(method_m="Decode")
        if option_text == "0":
            os.system("clear")
            menu_decode()
        elif option_text == "1":
            #Terminal input
            os.system("clear")
            print_plain(5)
            text = print_inputs(15)
            rotation = print_inputs(6)
            xorInt = print_inputs(14)
            saveToFile = print_inputs(16)
            output_str = xorHex(text, xorInt)
            result = rotDecode(output_str, DIC, rotation)
            str_output = xorResultDecode(result, 32)
            if saveToFile == "N":
                #os.system("clear")
                print_plain(5)
                print_plain(11)
                print(str_output)
            elif saveToFile == "Y":
                path = print_inputs(8)
                if not path.endswith("/"):
                    path += "/"
                if not path.startswith("/"):
                    path = "/"+path
                name = print_inputs(9)
                extension = print_inputs(13)
                with open(path+name+".txt", "a", encoding="utf-8") as f:
                    f.write(str_output)
                if extension == "1":
                    ext = ".txt"
                    print_outputs(0, path)
                elif extension == "2":
                    ext = ".pdf"
                    pdfkit.from_file(path+name+".txt", path+name+ext, options = optionsPDF)
                    os.remove(path+name+".txt")
                    print_outputs(0, path)
                elif extension != "1" and extension != "2":
                    extension = print_inputs(13)

        elif option_text == "2":
            os.system("clear")
            print_plain(5)
            text_path = print_inputs(10)
            if not text_path.startswith("/"):
                text_path = "/"+text_path
            rotation = print_inputs(6)
            xorInt = print_inputs(14)
            saveToFile = print_inputs(16)
            LINES = []
            if text_path.endswith(".txt"):
                with open(text_path, "r", encoding="utf-8") as f:
                    file = f.readlines()
                    for l in file:
                        LINES.append(l)
            elif text_path.endswith(".pdf"):
                file = extract_text(text_path)
                LINES = file.split("\n")
            OUTPUT = []
            for l in LINES:
                output_str = xorHex(l, xorInt)
                result = rotDecode(output_str, DIC, rotation)
                str_output = xorResultDecode(result, 33)
                OUTPUT.append(str_output+"\n")
            if saveToFile == "N":
                os.system("clear")
                print_plain(11)
                for line in OUTPUT:
                    print(line)
            elif saveToFile == "Y":
                path = print_inputs(8)
                if not path.endswith("/"):
                    path += "/"
                if not path.startswith("/"):
                    path = "/"+path
                name = print_inputs(9)
                extension = print_inputs(13)
                with open(path+name+".txt", "a", encoding="utf-8") as f:
                    for line in OUTPUT:
                        f.write(line)
                if extension == "1":
                    ext = ".txt"
                    print_outputs(0, path)
                elif extension == "2":
                    ext = ".pdf"
                    pdfkit.from_file(path+name+".txt", path+name+ext, options = optionsPDF)
                    os.remove(path+name+".txt")
                    print_outputs(0, path)
                elif extension != "1" and extension != "2":
                    extension = print_inputs(13)
            elif saveToFile != "N" and saveToFile != "Y":
                menu_text_to_text(method)

        elif option_text == "3":
            print_plain(0)
               
def menu_text_to_image(method):
    if method == "encode":
        #Initialize colormode
        colormode = ""
        #Initialize text
        text = ""
        #print Text to Image menu header
        print_plain(6)
        #Text Input Menu (Terminal or File)
        option_text = menu_text_input(method)
        #Define image extension
        ext = ".png"
        #Get text to encrypt
        if option_text == "0":
            os.system("clear")
            menu_encode()
        #If text input is from the terminal
        elif option_text == "1":
            os.system("clear")
            print_plain(6)
            text = print_inputs(5)
        #If text input is from a file
        elif option_text == "2":
            #Get the path to the file
            os.system("clear")
            print_plain(6)
            text_path = print_inputs(10)
            if not text_path.startswith("/"):
                text_path = "/"+text_path
            #If the path ends with .txt
            if text_path.endswith(".txt"):
                with open(text_path, 'r') as f:
                    text = f.read()
            #If the path ends with .pdf
            if text_path.endswith(".pdf"):
                text = extract_text(text_path)
        #Get the color mode
        os.system("clear")
        print_plain(6)
        img_mode = menu_img_mode(type="output")
        if img_mode == "0":
            os.system("clear")
            menu_text_to_image(method)
        elif img_mode == "1":
            colormode = "RGB"
        elif img_mode == "2":
            colormode = "L" #L represents Grayscale
        elif img_mode == "3":
            print_plain(0)
            exit()
        else:
            os.system("clear")
            menu_text_to_image(method)
        #Get the rotation integer
        os.system("clear")
        print_plain(6)
        print_plain(8)
        rotFactor = print_inputs(6)
        #Get the XOR integer
        xorInt = print_inputs(14)
        #Get the width and height of the generated image
        width = print_inputs(11)
        height = print_inputs(12)
        #Get the path to save the file
        path = print_inputs(8)
        if not path.endswith("/"):
            path += "/"
        if not path.startswith("/"):
            path = "/"+path
        #Get the name of the generated image
        name = print_inputs(9)
        #if method == "encode":
        string = replace_s(text)
        hex_str = xorString(string, 13)
        rotHex = rot(hex_str, DIC, rotFactor)
        hex_output = xorHex(rotHex, xorInt)
        pixelOutput, rangeX, rangeY, subsVal = ordHexOut(hex_output)
        savePixels = pixBool()
        imgFromOut(pixelOutput, savePixels, width, height, path, name, colormode, rangeX, rangeY)
        print_outputs(4, "", "", "", "", subsVal)
        print_outputs(0, path)
    if method == "decode":
        os.system("clear")
        print_plain(6)
        print_plain(13)
        text_path = print_inputs(10)
        if not text_path.startswith("/"):
           text_path = "/" + text_path 
        rotFactor = print_inputs(6)
        xorInt = print_inputs(14)
        width = print_inputs(11)
        height = print_inputs(12)
        img_ext = print_inputs(20)
        colormode = print_inputs(21)
        path = print_inputs(8)
        if not path.endswith("/"):
            path += "/"
        if not path.startswith("/"):
            path = "/"+path
        name = print_inputs(9)
        if text_path.endswith(".pdf"):
            text = extract_text(text_path)
        elif text_path.endswith(".txt"):
            with open(text_path, "r") as f:
                text = f.read()
        else:
            print_plain(9)
            exit()
        print_process(5)
        hex_str = xorHex(text, xorInt)
        print_process(6)
        rotHex = rotDecode(hex_str, DIC, rotFactor)
        print_process(7)
        result = xorResultDecode(rotHex, 33)
        if colormode == "1": #grayscale
            px_data = text2img(result, int(colormode))
            construct_img(px_data, width, height, path, name, img_ext, colormode)
        else: #color
            construct_img(result, width, height, path, name, img_ext, colormode)
        print_outputs(0, path)

def menu_image_to_image(method):
    os.system("clear")
    print_plain(3)
    if method == "encode":
        option_img = print_inputs(2)
        #grayscale to grayscale
        if int(option_img) == 1:
            os.system("clear")
            img_path = print_inputs(10)
            if not img_path.startswith("/"):
                img_path = "/"+img_path
            rotation = print_inputs(6)
            xorFactor = print_inputs(14)
            save_path = print_inputs(8)
            if not save_path.startswith("/"):
                save_path = "/" + save_path
            if not save_path.endswith("/"):
                save_path += "/"
            name = print_inputs(9)
            extension = print_inputs(20)
            img_img(img_path, rotation, xorFactor, save_path, name, int(option_img), extension)
            

    elif method == "decode":
        return 0

def menu_image_to_text(method):
    os.system("clear")
    print_plain(4)
    img_path = print_inputs(10)
    if not img_path.startswith("/"):
        img_path = "/" + img_path
    rotFactor = print_inputs(6)
    xorInt = print_inputs(14)
    if method == "encode":
        print_plain(14)
        option_img = print_inputs(3)
        saveToFile = print_inputs(7)
        img_data = extract_pixels(img_path, int(option_img))
        compressed_data = compress_pixels(img_data, int(option_img))
        #print(compressed_data)
        print_process(4)
        string = replace_s(compressed_data)
        print_process(5)
        hex = xorString(string, 13)
        print_process(6)
        rotHex = rot(hex, DIC, rotFactor)
        print_process(7)
        hex_output = xorHex(rotHex, xorInt)
        if saveToFile == "N":
            print_plain(7)
            print(hex_output)
        elif saveToFile == "Y":
            path = print_inputs(8)
            if not path.endswith("/"):
                path += "/"
            if not path.startswith("/"):
                path = "/" + path
            name = print_inputs(9)
            extension = print_inputs(13)
            with open(path+name+".txt", "a") as f:
                f.write(hex_output)
            if extension == "2":
                pdfkit.from_file(path+name+".txt", path+name+".pdf", options=optionsPDF)
                os.remove(path+name+".txt")
            print_outputs(0, path)
    elif method == "decode":
        pxUse = print_inputs(17)  
        substraction_val = print_inputs(18)
        os.system("clear")
        #start decoding
        outputFromImg = readImg(img_path, pxUse, substraction_val)
        xorHexStr = xorHex(outputFromImg, xorInt)
        rotDecodeStr = rotDecode(xorHexStr, DIC, rotFactor)
        result = xorResultDecode(rotDecodeStr, 32)
        print_plain(11)
        print(result)


if __name__ == "__main__":
    printIntro()
    menu_main()

#/home/sk01-2ef/Documents/Cryptography/DevilCrypt/140_bridge.png
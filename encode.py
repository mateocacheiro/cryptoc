import re
from PIL import Image
import random
from prints import print_outputs, print_inputs, print_plain, print_process
from tqdm import tqdm
from colorama import Fore


xorFactor = 13
dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"
DIC = []
for char in dictionary:
    DIC.append(char)

def pixBool():
    isTrue = False
    savePixels = print_inputs(19)
    if savePixels == 'Y':
        isTrue = True
    elif savePixels == 'N':
        isTrue = False
    else:
        pixBool()
    return isTrue

def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def replace_s(l):
    string = multiple_replace(l, {'\\t':'tabsymb','`':'backtildesymb','.':'dotsymb','\\n':'newlinesymb', 'º':'degreesymb', '@':'atsymb', '/':'slashsymb', ' ':'spacesymb','?':'questionsymb','"':'doublequotes',",":'commasymb',';':'semicolonsymb','+':'plussymb','-':'hyphonsymb','_':'underscoresymb','#':'hashtagsymb','%':'percentagesymb','!':'exclamationsymb','$':'dollarsymb','€':'eurosymb','~':'tildesymb','(':'oparsymb',')':'cparsymb','*':'wildcardsymb',"|":'vbarsymb','º':'ordsymb','&':'andsymb','=':'equalsymb','\\':'backwardsslashsymb', '\'':'apostrophe','{':'curlbro','[':'squarebro','}':'curlbrc',']':'squarebrc',':':'doubledots','1':'onenum','2':'twonum','3':'threenum','4':'fournum','5':'fivenum','6':'sixnum','7':'sevennum','8':'eightnum','9':'ninenum','0':'zeronum','A':'mayusa', 'B':'mayusb', 'C':'mayusc', 'D':'mayusd', 'E':'mayuse', 'F':'mayusf', 'G':'mayusg', 'H':'mayush', 'I':'mayusi', 'J':'mayusj', 'K':'mayusk', 'L':'mayusl', 'M':'mayusm', 'N':'mayusn', 'O':'mayuso', 'P':'mayusp', 'Q':'mayusq', 'R':'mayusr', 'S':'mayuss', 'T':'mayust', 'U':'mayusu', 'V':'mayusv', 'W':'mayusw', 'X':'mayusx', 'Y':'mayusy', 'Z':'mayusz'})
    return string

def xorString(string, xorFactor):
    for z in tqdm(range(20)):
        NSTR = []
        strOutput = ""
        for x in string:
            NSTR.append(chr(ord(x) ^ xorFactor + 2))
        for char in NSTR:
            strOutput = strOutput + char
        string = strOutput
        with open("/home/sk01-2ef/XOR_logs.txt", "a") as f:
            f.write(f"XOR Factor {xorFactor+2}: \n")
            f.write("\n" + strOutput + "\n\n")
        xorFactor += 1
        NSTR = []
            
    hex_str = string.encode("utf-8").hex()
    return hex_str

def xorHex(hex_str, xorInt):
    STR = []
    output = ""
    for x in tqdm(hex_str):
        STR.append(chr(ord(x) ^ xorInt))
    for x in STR:
        output += x
    return output

def rot(string, DIC, rotFactor):
    output = ""
    ROT = []
    for x in tqdm(string):
        if x in DIC:
            index = DIC.index(x)
            rotIndex = index + rotFactor
            if rotIndex >= len(DIC):
                while rotIndex >= len(DIC):
                    rotIndex -= len(DIC)
            x = DIC[rotIndex]
            ROT.append(x)
    for char in ROT:
        output += char
    return output

def ordHexOut(hex_output):
    STR = []
    SEC = []
    subsVal = 0
    for char in tqdm(hex_output):
        char = ord(char)
        STR.append(char)
    if max(STR) > 255:
        if min(STR) > 107:
            subsVal = abs(255-max(STR))+107
        else:
            subsVal = abs(255-max(STR))
        for x in STR:
            SEC.append(x-subsVal)
        STR = []
        for x in SEC:
            STR.append(x)
    rangeX = min(STR)
    rangeY = max(STR)
    return STR, rangeX, rangeY, subsVal

def imgFromOut(pixelOutput, savePixels, width, height, outputPath, outputName, colormode, rangeX, rangeY):

    if colormode == "L":

        img = Image.new(mode=colormode, size=(width, height))

        for x in range(width):
            for y in range(height):
                randompx = random.randint(rangeX, rangeY)
                img.putpixel((x, y), randompx)

        if len(pixelOutput) <= img.width:
            for x in range(img.width):
                if x < len(pixelOutput):
                    img.putpixel((x, 0), pixelOutput[x])

        else:
            numRows = int(len(pixelOutput)/img.width)
            index = 0
            row = 0
            if numRows < img.height:
                numPixelsRow = len(pixelOutput) % img.width
                while row != numRows:
                    for x in range(img.width):
                        img.putpixel((x, row), pixelOutput[(img.width*row+1)+x])
                    row += 1
                if numPixelsRow > 0:
                    while index != numPixelsRow:
                        for x in range(numPixelsRow):
                            img.putpixel((x, numRows), pixelOutput[(numRows*img.width)+index])
                            index +=1
            else:
                print_plain(12)
        
        if savePixels:
            path = outputPath+str(len(pixelOutput))+"_"+outputName+".png"
        else:
            path = outputPath+outputName+".png"
            print_outputs(1, "", len(pixelOutput))

        img.save(path)

    elif colormode == "RGB":

        numPixels = int(len(pixelOutput)/3)
        pixelMod = len(pixelOutput)%3

        img = Image.new(mode=colormode, size=(width, height))

        for x in range(width):
            for y in range(height):
                randR = random.randint(rangeX, rangeY)
                randG = random.randint(rangeX, rangeY)
                randB = random.randint(rangeX, rangeY)
                img.putpixel((x,y), (randR, randG, randB))
    
        outputIndex = 0

        if numPixels <= img.width:

            for x in range(numPixels):
                pixelValues = []
                pixelIndex = 0
                while pixelIndex < 3:
                    pixelValues.append(pixelOutput[outputIndex])
                    pixelIndex += 1
                    outputIndex += 1
                img.putpixel((x, 0), (pixelValues[0], pixelValues[1], pixelValues[2]))

            if pixelMod == 1:
                pixelValues = []
                randR = pixelOutput[outputIndex]
                randG = random.randint(rangeX, rangeY)
                randB = random.randint(rangeX, rangeY)
                img.putpixel((outputIndex, 0), (randR, randG, randB))
        
            if pixelMod == 2:
                randR = pixelOutput[outputIndex]
                randG = pixelOutput[outputIndex+1]
                randB = random.randint(rangeX, rangeY)
                img.putpixel((outputIndex, 0), (randR, randG, randB))

        elif numPixels > img.width:

            numRows = numPixels / img.width
            row = 0

            if numRows < img.height:

                numPixelsRow = numPixels % img.width

                while row != numRows:

                    for x in range(img.width):

                        pixelValues = []
                        pixelIndex = 0
                        while pixelIndex < 3:
                            pixelValues.append(pixelOutput[outputIndex])
                            pixelIndex += 1
                            outputIndex += 1
                        img.putpixel((x, row), (pixelValues[0], pixelValues[1], pixelValues[2]))

                    row += 1
                
                if numPixelsRow > 0:

                    index = 0

                    while index != numPixelsRow:
                        for x in range(numPixelsRow):
                            pixelValues = []
                            pixelIndex = 0
                            while pixelIndex < 3:
                                pixelValues.append(pixelOutput[outputIndex])
                                pixelIndex += 1
                                outputIndex += 1
                            img.putpixel((x, row), (pixelValues[0], pixelValues[1], pixelValues[2]))
                            index += 1

                    if pixelMod == 1:

                        randR = pixelOutput[outputIndex]
                        randG = random.randint(rangeX, rangeY)
                        randB = random.randint(rangeX, rangeY)
                        img.putpixel((numPixelsRow+1, row), (randR, randG, randB))

                    if pixelMod == 2:

                        randR = pixelOutput[outputIndex]
                        randG = pixelOutput[outputIndex+1]
                        randB = random.randint(rangeX, rangeY)
                        img.putpixel((numPixelsRow+1, row), (randR, randG, randB))

            else:
                print_plain(12)
        
        if savePixels:
            path = outputPath+str(numPixels+1)+"_"+outputName+".png"
        else:
            path = outputPath+outputName+".png"
            print_outputs(3, "", "", "", numPixels+1)
        
        img.save(path)

def extract_pixels(img_path, colormode):
    print_process(0)
    output = ""
    if colormode == 1:
        img = Image.open(img_path).convert('L')
        data = []
        for y in tqdm(range(img.height)):
            for x in range(img.width):
                pixel = img.getpixel((x,y))
                data.append(pixel)
        output = str(data)[1:][:-1].replace(", ","/")
    elif colormode == 2:
        img = Image.open(img_path).convert('RGB')
        data = []
        for y in tqdm(range(img.height)):
            for x in range(img.width):
                pixel = img.getpixel((x,y))
                for value in range(len(pixel)):
                    data.append(pixel)
        output = str(data)[1:][:-1].replace("), ",")/").replace(")/(","/").replace(", ",",")[1:][:-1]
    return output

def compress_pixels(data, colormode):
    print_process(1)
    output = ""
    pxContainer = 0
    data_list = data.split("/")
    if colormode == 1:
        for x in tqdm(range(len(data_list)-1)):
            current = data_list[x]
            if x < len(data_list):
                next = data_list[x+1]
            if current == next:
                pxContainer += 1
            else:
                if pxContainer == 0:
                    output += f"{current}/"
                else:
                    output += f"{pxContainer+1}x{current}/"
                pxContainer = 0
        output = str(output[:-1])
        return output
    else:
        pass

def img_img(img_path, rotation, xorFactor, save_path, name, colormode, extension):
    #Create image instance
    #Read its pixels
    #Rotate the values and XOR them
    #Turn them to the pixel value range
    #Create new image with the new values
    #Save final image

    img = Image.open(img_path).convert("L")

    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
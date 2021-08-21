from prints import print_process
from PIL import Image
import re
from colorama import Fore
from tqdm import tqdm
#imgName = input("Image: ")
#imgPath = "/home/sk01-2ef/Documents/Cryptography/DevilCrypt/"+imgName+".png"
#pxUse = int(input("Pixels to use: "))
dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"
DIC = []
for char in dictionary:
    DIC.append(char)
#xorFactor = 33

def readImg(imgPath, pxUse, substractionValue):
    img = Image.open(imgPath)
    PXC = []
    CHR = []
    output = ""
    #check de color mode of the image
    imgMode = img.mode
    if imgMode == 'L':
        for x in range(img.width):
            if x < pxUse:
                pixel = img.getpixel((x,0))
                PXC.append(pixel)
        for x in PXC:
            CHR.append(chr(x+substractionValue))
        for x in CHR:
            output += x
    elif imgMode == 'RGB':
        print(f"This image is in {imgMode} which hasn't been implemented yet, sorry.")
    else:
        print("Image mode not supported.")
    return output

def multiple_replace_dec(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def rotDecode(string, DIC, rotFactor):
    output = ""
    ROT = []
    for x in tqdm(string):
        if x in DIC:
            index = DIC.index(x)
            rotIndex = index - rotFactor
            if rotIndex >= len(DIC):
                rotIndex -= len(DIC)
            x = DIC[rotIndex]
            ROT.append(x)
    for char in ROT:
        output += char
    result = bytes.fromhex(output).decode("utf-8")
    return result

def xorResultDecode(string, xorFactor):
    for i in range(20):
        NSTR = []
        strOutput = ""
        for x in string:
            NSTR.append(chr(ord(x) ^ xorFactor + 2))
        for char in NSTR:
            strOutput = strOutput + char
        string = strOutput
        #print(f"Iteration #{i+1} / XOR Factor #{xorFactor+2}:\n{strOutput}\n\n")
        xorFactor -= 1
        NSTR = []
    strOutput = strOutput.lower()
    print_process(4)
    strOutput = multiple_replace_dec(strOutput, {'tabsymb':'\\t','newlinesymb':'\\n','backtildesymb':'`','dotsymb':'.', 'atsymb':'@', 'slashsymb':'/','degreesymb':'º', 'spacesymb':' ','questionsymb':'?','doublequotes':'"',"commasymb":',','semicolonsymb':';','plussymb':'+','hyphonsymb':'-','underscoresymb':'_','hashtagsymb':'#','percentagesymb':'%','exclamationsymb':'!','dollarsymb':'$','eurosymb':'€','tildesymb':'~','oparsymb':'(','cparsymb':')','wildcardsymb':'*',"vbarsymb":'|','ordsymb':'º','andsymb':'&','equalsymb':'=','doubledots':':','backwardsslashsymb':'\\','apostrophe':'\'','curlbro':'{','squarebro':'[','curlbrc':'}','squarebrc':'}','questionsymb':'?','onenum':'1','twonum':'2','threenum':'3','fournum':'4','fivenum':'5','sixnum':'6','sevennum':'7','eightnum':'8','ninenum':'9','zeronum':'0','mayusa':'A', 'mayusb':'B', 'mayusc':'C', 'mayusd':'D', 'mayuse':'E', 'mayusf':'F', 'mayusg':'G', 'mayush':'H', 'mayusi':'I', 'mayusj':'J', 'mayusk':'K', 'mayusl':'L', 'mayusm':'M', 'mayusn':'N', 'mayuso':'O', 'mayusp':'P', 'mayusq':'Q', 'mayusr':'R', 'mayuss':'S', 'mayust':'T', 'mayusu':'U', 'mayusv':'V', 'mayusw':'W', 'mayusx':'X', 'mayusy':'Y', 'mayusz':'Z'})
    return strOutput

def text2img(text, colormode):
    print_process(3)
    TEXT = text.split("/")
    px_data = ""
    if colormode == 1:
        for x in tqdm(TEXT):
            if "x" not in x:
                px_data += f"{x}/"
            else:
                px_rep = x.split("x")
                for rep in range(0, int(px_rep[0])):
                    px_data += f"{px_rep[1]}/"
    return px_data[:-1]

def construct_img(result, width, height, path, name, ext, colormode):
    print_process(2)
    data = result.split("/")
    index = 0
    if colormode == "1":
        img = Image.new(mode="L", size=(width, height))
        for y in range(img.height):
            for x in range(img.width):
                img.putpixel((x,y), data[index])
                if index < len(data)-1:
                    index += 1
        if ext == "1":
            img.save(path+name+".jpg")
        if ext == "2":
            img.save(path+name+".png")
    if colormode == "2":
        img = Image.new(mode="RGB", size=(width, height))
        for y in range(img.height):
            for x in range(img.width):
                pixel = data[index]
                pixelValues = pixel.split(",")
                R = int(pixelValues[0])
                G = int(pixelValues[1])
                B = int(pixelValues[2])
                img.putpixel((x,y), (R, G, B))
                if index < len(data)-1:
                    index += 1
        if ext == "1":
            img.save(path+name+".jpg")
        if ext == "2":
            img.save(path+name+".png")
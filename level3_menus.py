from prints import print_plain
import os
def menu_text_input(method_m):
    option_text = input(f"\n(0) - Return to {method_m} Menu\n(1) - Text from terminal input\n(2) - Text from file (.txt / .pdf)\n(3) - Exit\n\n>>> ")
    return option_text

def menu_img_mode(type):
    m = input(f"\nChoose color mode of the {type} image:\n\n(0) - Return to Text to Image menu\n(1) - Color (RGB)\n(2) - Grayscale\n(3) - Exit\n\n>>> ")
    return m
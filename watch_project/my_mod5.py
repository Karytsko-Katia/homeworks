import time
import my_mod

def draw_digit(digit):
    return my_mod.digit_patterns[digit]


def update_time():
    current_time = time.strftime("%H:%M:%S")
    lines = ["", "", "", "", ""]

    if int(time.strftime("%S")) % 2 == 0:
         colon = True
    else:
         colon = False

    for char in current_time:
        if char == ':':
              digit = draw_digit(':') if colon else draw_digit(' ')
        else:
             digit = draw_digit(char)
        for i in range(5):
            lines[i] += digit[i] + "  "

    for line in lines:
        print(line)


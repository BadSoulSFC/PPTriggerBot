import keyboard as kb
import time
from ctypes import windll
from pynput.mouse import Button, Controller


def main():
    mouse = Controller()
    # x, y = 720, 450
    # range of 8
    pdata_list = []
    pdata_check_list = []
    x_pixel_list = []
    y_pixel_list = []
    screen_res = input('Input your screen resolution: Example - 1920x1080 : \n')
    x_, y_ = screen_res.split('x')
    x_res = int(x_)/2
    y_res = int(y_)/2
    x = range(int(x_res-4), int(x_res+5) )
    y = range(int(y_res - 4), int(y_res + 5))
    for x_pixels in x:
        x_pixel_list.append(x_pixels)
    for y_pixels in y:
        y_pixel_list.append(y_pixels)

    while True:
        storeddata = False
        while kb.is_pressed('x'):
            if not storeddata:
                for i in range(9):
                    pdata_list.append(windll.gdi32.GetPixel(
                        windll.user32.GetDC(0),
                        x_pixel_list[i],
                        y_pixel_list[i]
                    ))
                storeddata = True
            for check_pixels in range(9):
                pdata_check_list.append(windll.gdi32.GetPixel(
                    windll.user32.GetDC(0),
                    x_pixel_list[check_pixels],
                    y_pixel_list[check_pixels]
                ))
            if pdata_check_list == pdata_list:
                pdata_check_list = []
            else:
                mouse.press(Button.left)
                mouse.release(Button.left)
                pdata_list = []
                pdata_check_list = []
                storeddata = False
            time.sleep(0.035)
        if kb.is_pressed('end'):
            break


if __name__ == '__main__':
    main()

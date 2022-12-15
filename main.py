import board
import busio
import displayio
import terminalio
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_st7789 import ST7789
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect

# Clean display and reinitialize
displayio.release_displays()
spi = busio.SPI(board.GP10, MOSI=board.GP11)
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000) # Configure SPI for 24MHz
spi.unlock()
tft_cs = board.GP9
tft_dc = board.GP8
displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP12)
display = ST7789(display_bus, width=135, height=240, rowstart=40, colstart=53)
display.rotation = 270

# Create splash scren and display
splash = displayio.Group()
display.show(splash)
color_bitmap = displayio.Bitmap(240, 135, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x222222
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)
inner_bitmap = displayio.Bitmap(240, 135, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x660000
inner_sprite = displayio.TileGrid(inner_bitmap, 
                                  pixel_shader=inner_palette, 
                                  x=00, y=00)
splash.append(inner_sprite)

text_group = displayio.Group(x=100, y=70)
text = "Semper Finein"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)
a_box=Rect(208, 12, 20, 20, fill=None, outline=0x333333)
b_box=Rect(208, 103, 20, 20, fill=None, outline=0x333333)
u_box=Rect(37, 35, 20, 20, fill=None, outline=0x333333)
c_box=Rect(37, 60, 20, 20, fill=None, outline=0x333333)
l_box=Rect(12, 60, 20, 20, fill=None, outline=0x333333)
d_box=Rect(37, 85, 20, 20, fill=None, outline=0x333333)
r_box=Rect(62, 60, 20, 20, fill=None, outline=0x333333)

splash.append(a_box)
splash.append(b_box)
splash.append(u_box)
splash.append(c_box)
splash.append(l_box)
splash.append(d_box)
splash.append(r_box)


# Define board pins and initialize
key_UP = DigitalInOut(board.GP2)
key_DOWN = DigitalInOut(board.GP18)
key_LEFT = DigitalInOut(board.GP16)
key_RIGHT = DigitalInOut(board.GP20)
key_CTRL = DigitalInOut(board.GP3)
key_A = DigitalInOut(board.GP15)
key_B = DigitalInOut(board.GP17)
for i in [key_UP, key_DOWN, key_LEFT, key_RIGHT, key_CTRL, key_A, key_B]:
    i.direction = Direction.INPUT
    i.pull = Pull.UP


while True:
    if key_A.value == False:
        a_box.fill = 0x333333
    else:
        a_box.fill = None
    if key_B.value == False:
        b_box.fill = 0x333333
    else:
        b_box.fill = None

    if key_UP.value == False:
        u_box.fill = 0x333333
    else:
        u_box.fill = None
    if key_DOWN.value == False:
        d_box.fill = 0x333333
    else:
        d_box.fill = None
    if key_LEFT.value == False:
        l_box.fill = 0x333333
    else:
        l_box.fill = None
    if key_RIGHT.value == False:
        r_box.fill = 0x333333
    else:
        r_box.fill = None
    if key_CTRL.value == False:
        c_box.fill = 0x333333
    else:
        c_box.fill = None
    time.sleep(0.1)

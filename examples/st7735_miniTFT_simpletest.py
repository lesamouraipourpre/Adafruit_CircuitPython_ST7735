"""
This example will test out the display on the Mini TFT FeatherWing
"""
import board
import displayio
from adafruit_seesaw.seesaw import Seesaw
import adafruit_st7735.st7735 as st7735

reset_pin = 8
i2c = board.I2C()
ss = Seesaw(i2c, 0x5E)
ss.pin_mode(reset_pin, ss.OUTPUT)

spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D6

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D9)

ss.digital_write(reset_pin, True)
display = st7735.MINI160X80(display_bus)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

try:
    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   position=(0, 0))
except TypeError:
    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   x=0, y=0)
splash.append(bg_sprite)

while True:
    pass

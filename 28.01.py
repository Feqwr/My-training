from mcpi.minecraft import Minecraft
from time import sleep
from random import randint

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

while True:  # Бесконечный цикл
    command = input('Do you want to teleport to build? Yes or no:')

    if command == 'no':
        air = 0
        red = 152
        gra = 1
        white = 42
        bla = 49
        glo = 41

        pixel_list = [
            [air, air, air, bla, bla, air, air, air, air, air, air, air, air, air, air, air, air],
            [air, air, bla, white, red, bla, air, air, air, air, air, air, air, air, air, air, air],
            [air, air, air, bla, white, red, bla, air, air, air, air, air, air, air, air, air, air],
            [air, air, air, air, bla, white, red, bla, air, air, air, air, air, air, air, air, air],
            [air, air, air, air, air, bla, white, red, bla, air, air, air, air, air, air, air, air],
            [air, air, air, air, air, air, bla, white, bla, air, air, air, air, air, air, air, air],
            [air, air, air, air, air, air, bla, red, bla, air, air, air, air, air, air, air, air],
            [air, air, air, air, air, air, bla, white, bla, air, air, air, air, air, air, air, air],
            [air, air, air, air, air, bla, bla, red, bla, bla, bla, bla, bla, air, air, air, air],
            [air, air, air, bla, bla, gra, bla, bla, bla, gra, gra, gra, gra, bla, air, air, air],
            [air, air, bla, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, bla, air, air],
            [bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla],
            [bla, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, bla],
            [bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla],
            [air, bla, red, red, red, red, red, red, red, red, red, red, red, red, red, bla, air],
            [air, bla, red, red, red, red, red, red, red, red, red, red, red, red, red, bla, air],
            [air, bla, bla, red, red, red, red, red, red, red, red, red, red, red, bla, bla, air],
            [air, air, bla, red, red, red, red, red, red, red, red, red, red, red, bla, air, air],
            [air, air, bla, red, red, red, red, glo, red, glo, red, red, red, red, bla, air, air],
            [air, air, bla, red, red, red, glo, red, glo, red, glo, red, red, red, bla, air, air],
            [air, air, bla, red, red, red, glo, red, glo, red, glo, red, red, red, bla, air, air],
            [air, air, air, bla, red, red, glo, red, glo, red, glo, red, red, bla, air, air, air],
            [air, air, air, bla, red, red, glo, red, red, red, glo, red, red, bla, air, air, air],
            [air, air, air, bla, red, red, red, red, red, red, red, red, red, bla, air, air, air],
            [air, air, air, air, bla, red, red, red, red, red, red, red, bla, air, air, air, air],
            [air, air, air, air, bla, red, red, red, red, red, red, red, bla, air, air, air, air],
            [air, air, air, air, bla, red, red, red, red, red, red, red, bla, air, air, air, air],
            [air, air, air, air, bla, bla, bla, bla, bla, bla, bla, bla, bla, air, air, air, air],

        ]
        x_start = x
        for row in reversed(pixel_list):
            for block in row:
                mc.setBlock(x, y, z, block)
                x += 1
            y += 1
            x = x_start
        break
    elif command == 'yes':
        x, y, z = mc.player.getTilePos()
        sleep(5)
        mc.player.setPos(x,y,z)
    air = 0
    red = 152
    gra = 1
    white = 42
    bla = 49
    glo = 41

    pixel_list = [
        [air, air, air, bla, bla, air, air, air, air, air, air, air, air, air, air, air, air],
        [air, air, bla, white, red, bla, air, air, air, air, air, air, air, air, air, air, air],
        [air, air, air, bla, white, red, bla, air, air, air, air, air, air, air, air, air, air],
        [air, air, air, air, bla, white, red, bla, air, air, air, air, air, air, air, air, air],
        [air, air, air, air, air, bla, white, red, bla, air, air, air, air, air, air, air, air],
        [air, air, air, air, air, air, bla, white, bla, air, air, air, air, air, air, air, air],
        [air, air, air, air, air, air, bla, red, bla, air, air, air, air, air, air, air, air],
        [air, air, air, air, air, air, bla, white, bla, air, air, air, air, air, air, air, air],
        [air, air, air, air, air, bla, bla, red, bla, bla, bla, bla, bla, air, air, air, air],
        [air, air, air, bla, bla, gra, bla, bla, bla, gra, gra, gra, gra, bla, air, air, air],
        [air, air, bla, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, bla, air, air],
        [bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla],
        [bla, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, gra, bla],
        [bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla, bla],
        [air, bla, red, red, red, red, red, red, red, red, red, red, red, red, red, bla, air],
        [air, bla, red, red, red, red, red, red, red, red, red, red, red, red, red, bla, air],
        [air, bla, bla, red, red, red, red, red, red, red, red, red, red, red, bla, bla, air],
        [air, air, bla, red, red, red, red, red, red, red, red, red, red, red, bla, air, air],
        [air, air, bla, red, red, red, red, glo, red, glo, red, red, red, red, bla, air, air],
        [air, air, bla, red, red, red, glo, red, glo, red, glo, red, red, red, bla, air, air],
        [air, air, bla, red, red, red, glo, red, glo, red, glo, red, red, red, bla, air, air],
        [air, air, air, bla, red, red, glo, red, glo, red, glo, red, red, bla, air, air, air],
        [air, air, air, bla, red, red, glo, red, red, red, glo, red, red, bla, air, air, air],
        [air, air, air, bla, red, red, red, red, red, red, red, red, red, bla, air, air, air],
        [air, air, air, air, bla, red, red, red, red, red, red, red, bla, air, air, air, air],
        [air, air, air, air, bla, red, red, red, red, red, red, red, bla, air, air, air, air],
        [air, air, air, air, bla, red, red, red, red, red, red, red, bla, air, air, air, air],
        [air, air, air, air, bla, bla, bla, bla, bla, bla, bla, bla, bla, air, air, air, air],

    ]

    x_start = x
    for row in reversed(pixel_list):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = x_start

    break




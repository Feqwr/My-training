# import random
# import time
# from mcpi.minecraft import Minecraft
#
# from random import choice
#
# mc = Minecraft.create()
#
#
#
# def grow_tree3(block_leaves, x, y, z):
#     num = random.randint(3, 14)
#     num2 = num + 1
#     mc.postToChat('Строю дерево - !')
#     mc.setBlocks(x, y, z, x, y + num, z, 17)  # Ствол дерева
#     mc.setBlocks(x - 3, y + num, z - 3, x + 3, y + num, z + 3, block_leaves)  # 1-ый слой листвы
#     mc.setBlocks(x - 2, y + num2, z - 2, x + 2, y + num2, z + 2, block_leaves) # 2-ой слой листвы
# while True:
#     block_leavesev = choice([200, 18, 221, 178, 226, 233, 161])
#     x1, y1, z1 = mc.player.getPos()
#     time.sleep(5)
#     grow_tree3(block_leavesev, x1, y1, z1)

#Практическая работа2 урок 15
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

def symbol_y(x, y, z, block_type):
    for i in range (4):
        x1, y2, z2 = x+2, y, z
        x7,y7,z7 = x+4,y+1,z
        mc.setBlock(x, y + 2, z, block_type)
        mc.setBlock(x, y + 3 - i, z, block_type)
        mc.setBlock(x1,y,z, block_type)
        mc.setBlocks(x1,y,z,x1+3,y+3,z,block_type)
        mc.setBlocks(x7,y7,z,x7-1,y+2,z, 0)
def sent(text):
    mc.postToChat(text)

x1,x2,x4 = mc.player.getTilePos()
type = 1
textt = ('Ю')
sleep(2)
sent(textt)
symbol_y(x1,x2,x4,type)
sleep(1)

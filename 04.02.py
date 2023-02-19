# from mcpi.minecraft import Minecraft
# import time
#
# mc = Minecraft.create()
#
# arbuz = 103
#
# def arbuzy():
#     x, y, z = mc.player.getTilePos()
#     mc.setBlock(x, y - 1, z, arbuz)
#     time.cleep(5)
#
# while True:
#     arbuzy()

# import random
# import time
# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
#
#
# def set_pose():
#     time.sleep(5)
#     mc.player.setTilePos(random.randint(150, 360), random.randint(15, 45), random.randint(100, 300))
#     x, y, z = mc.player.getTilePos()
#     mc.setBlock(x, y, z, 56)
# def set_dom():
#     x, y, z = mc.player.getTilePos()
#     mc.postToChat('Строю дом')
#     mc.setBlocks(x, y, z, x + 5, y + 5, z + 5, 5)
#     mc.setBlocks(x, y, z, x - 3, y - 3, z - 3, 0)
#     mc.setBlocks(x, y+2, z, x, y+3, z, 0)
#
#
# while True:
#     set_pose()
#     set_dom()

import random
import time
from mcpi.minecraft import Minecraft

from random import choice

mc = Minecraft.create()


# def grow_tree2():
#     x, y, z = mc.player.getTilePos()
#     xx = random.randint(20, 50)
#     x += xx
#     zz = random.randint(20,50)
#     z += zz
#     y = y
#     block_leaves = choice([200, 18, 221, 178, 226, 233, 161])
#     num = random.randint(3, 14)
#     num2 = num + 1
#     mc.postToChat('Строю дерево!')
#     mc.setBlocks(x, y, z, x, y + num, z, 17)  # Ствол дерева
#     mc.setBlocks(x - 3, y + num, z - 3, x + 3, y + num, z + 3, block_leaves)  # 1-ый слой листвы
#     mc.setBlocks(x - 2, y + num2, z - 2, x + 2, y + num2, z + 2, block_leaves) # 2-ой слой листвы


def grow_tree():
    x, y, z = mc.player.getTilePos()
    block_leaves = choice([200, 18, 221, 178, 226, 233, 161])
    num = random.randint(3, 14)
    num2 = num + 1
    mc.postToChat('Строю дерево!')
    mc.setBlocks(x, y, z, x, y + num, z, 17)  # Ствол дерева
    mc.setBlocks(x - 3, y + num, z - 3, x + 3, y + num, z + 3, block_leaves)  # 1-ый слой листвы
    mc.setBlocks(x - 2, y + num2, z - 2, x + 2, y + num2, z + 2, block_leaves) # 2-ой слой листвы

# def grow_tree3():
#     x2, y2, z2 = mc.player.getTilePos()
#     zzmin = random.randint(x2-20, x2-50)
#     xxmin = random.randint(z2-20, z2-50)
#     x2 = xxmin
#     y2 = y2
#     z2 = zzmin
#     block_leaves = choice([200, 18, 221, 178, 226, 233, 161])
#     num = random.randint(3, 14)
#     num2 = num + 1
#     mc.postToChat('Строю дерево - !')
#     mc.setBlocks(x2, y2, z2, x2, y2 + num, z2, 17)  # Ствол дерева
#     mc.setBlocks(x2 - 3, y2 + num, z2 - 3, x2 + 3, y2 + num, z2 + 3, block_leaves)  # 1-ый слой листвы
#     mc.setBlocks(x2 - 2, y2 + num2, z2 - 2, x2 + 2, y2 + num2, z2 + 2, block_leaves) # 2-ой слой листвы
while True:
    time.sleep(2.5)
    grow_tree()

# from mcpi.minecraft import Minecraft
# from time import sleep
#
# mc = Minecraft.create()
#
# # a = 4
#
# x, y, z = mc.player.getTilePos()
#
# black = 1
# reded = 95
# aired = 13
#
# pixel_list = [
#     [aired, black, black, black, aired, black, black, black, black, black, black, black, black, black, black, aired, black, black, black, black],
#     [black, reded, reded, black, reded, reded, black, reded, reded, black, black, reded, reded, aired, reded, reded, black, reded, reded, black],
#     [black, reded, reded, aired, reded, reded, black, reded, reded, black, black, reded, reded, black, reded, reded, black, reded, reded, aired],
#     [aired, black, black, black, aired, black, black, black, black, black, black, black, black, black, black, aired,
#      black, black, black, black],
#     [black, reded, reded, black, reded, reded, black, reded, reded, black, black, reded, reded, aired, reded, reded,
#      black, reded, reded, black],
#     [black, reded, reded, aired, reded, reded, black, reded, reded, black, black, reded, reded, black, reded, reded,
#      black, reded, reded, aired],
#     [aired, black, black, black, aired, black, black, black, black, black, black, black, black, black, black, aired,
#      black, black, black, black],
#     [black, reded, reded, black, reded, reded, black, reded, reded, black, black, reded, reded, aired, reded, reded,
#      black, reded, reded, black],
#     [black, reded, reded, aired, reded, reded, black, reded, reded, black, black, reded, reded, black, reded, reded,
#      black, reded, reded, aired],
#     [aired, black, black, black, aired, black, black, black, black, black, black, black, black, black, black, aired,
#      black, black, black, black],
#     [black, reded, reded, black, reded, reded, black, reded, reded, black, black, reded, reded, aired, reded, reded,
#      black, reded, reded, black],
#     [black, reded, reded, aired, reded, reded, black, reded, reded, black, black, reded, reded, black, reded, reded,
#      black, reded, reded, aired],
#     [aired, black, black, black, aired, black, black, black, black, black, black, black, black, black, black, aired,
#      black, black, black, black],
#     [black, reded, reded, black, reded, reded, black, reded, reded, black, black, reded, reded, aired, reded, reded,
#      black, reded, reded, black],
#     [black, reded, reded, aired, reded, reded, black, reded, reded, black, black, reded, reded, black, reded, reded,
#      black, reded, reded, black],
#     [black, black, black, black, black, black, black, black, black, black, black, black, black, black, black, black, black, black, black, black]
# ]
#
# x_start = x
# for row in reversed(pixel_list):
#     for block in row:
#         mc.setBlock(x, y, z, block)
#         x += 1
#     y += 1
#     x = x_start


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

blocks = [[1, 1, 1, 1, 1],
          [4, 0, 0, 0, 4],
          [4, 0, 0, 0, 4],
          [4, 0, 0, 0, 4],
          [4, 4, 4, 4, 4]]


for t in range(6):
    for i in blocks:
        for j in i:
            if i == 0:
                mc.setBlock(x, y, z, 0)
            else:
                mc.setBlock(x, y, z, 35, i)
            x += 1
        x -= 6
        z += 1
    y += 1
    x = x
    z = z
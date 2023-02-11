# from mcpi.minecraft import Minecraft
# from random import randint
# from time import sleep
#
# mc = Minecraft.create()
#
# def hello(name):
#     print(f'Hello, {name}')
# hello(input())


# #Практическая работа1 урок 15
# from mcpi.minecraft import Minecraft
# from random import randint
# from time import sleep
#
# mc = Minecraft.create()
#
#
# def put_block(id):
#     x, y, z = mc.player.getTilePos()
#     mc.setBlock(x, y - 1, z, id)
# def sent(chat):
#     mc.postToChat(chat)
# while True:
#     block_id = randint(1, 5)
#     sent_ch = ('Build a block!')
#     sleep(2)
#     sent(sent_ch)
#     put_block(block_id)

#Практическая работа2 урок 15
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

def symbol_H(x, y, z, block_type):
    for i in range(4):
        mc.setBlock(x, y + 3 + i, z, block_type)
        mc.setBlock(x, y + 3 - i, z, block_type)
    mc.setBlocks(x, y, z, x, y + 5, z, block_type)
    x3, y3, z3= x+3, y+3, z+3
    mc.setBlocks(x, y3, z,x+2, y3, z, block_type)
    for i in range(4):
        mc.setBlock(x3, y3 - i, z, block_type)
        mc.setBlock(x3, y3 + i, z, block_type)
def symbol_ya(x, y, z, block_type):
   mc.setBlocks(x + 4, y, z, x + 4, y + 5, z, block_type)
   mc.setBlocks(x, y + 5, z, x + 4, y + 5, z, block_type)
   mc.setBlocks(x, y + 3, z, x + 4, y + 3, z, block_type)
   mc.setBlock(x, y + 4, z, block_type)
   for i in range(3):
       mc.setBlock(x + i, y + i, z, block_type)
def sent(text):
    mc.postToChat(text)

x1,x2,x4 = mc.player.getTilePos()
type = 1
textt = ('H')
texttt = ('Я')
sleep(2)
sent(textt)
symbol_ya(x1,x2,x4,type)
sleep(1)
sent(texttt)
symbol_H(x1+6,x2,x4, type)

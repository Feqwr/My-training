#Practick 1

# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
#
# valuable_blocks = [14,129,56,41,57,133]
# srvaluble_blocks = [15,42,22,73,152]
#
# def check_valuable(list_blocks):
#     x, y, z = mc.player.getTilePos()
#     block_under = mc.getBlock(x,y-1,z)
#     if block_under in list_blocks:
#         return 'Valuable Block'
#     elif block_under in srvaluble_blocks:
#         return 'Average Block value'
#     return 'Not aluble block'
#
# message = check_valuable(valuable_blocks)
# mc.postToChat(message)

#Practic 2

# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
#
# valuable_blocks = [14,129,56,41,57,133]
# srvaluble_blocks = [15,42,22,73,152]
#
# def get_wool_state(color):
#     if color == "Белый":
#         return 0
#     elif color == "Оранжевый":
#         return 1
#     elif color == "Сиреневый":
#         return 2
#     elif color == "Светло-синий":
#         return 3
#     elif color == "Желтый":
#         return 4
#     elif color == "Лаймовый":
#         return 5
#     elif color == "Розовый":
#         return 6
#     elif color == "Серый":
#         return 7
#     else:
#         print('Цвет блока не верный')
#
#
# color_string = input('Введите цвет блока:')
# state = get_wool_state(color_string)
#
# x, y, z = mc.player.getTilePos()
# mc.setBlock(x,y,z,35,state)

# Practic 3
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def block_id_remider(name):
    if name == 'камень':
        return 1
    elif name == 'песок':
        return 12
    elif name == 'губка':
        return 19
    elif name == 'золото':
        return 41
    elif name == 'тнт':
        return 46
    elif name == 'трава':
        return 2
    elif name == 'доски':
        return 5
    elif name == 'дуб':
        return 17
    elif name == 'кровать':
        return 26
    elif name == 'кирпичи':
        return 45
    elif name == 'обсидиан':
        return 49
    elif name == 'сундук':
        return 54
    elif name == 'верстак':
        return 58
    elif name == 'печь':
        return 61
    elif name == 'чаровальня':
        return 116
    elif name == 'командный блок':
        return 137
    elif name == 'наковальня':
        return 145
    else:
        print('Неверное название')
print('Выберите блок из: Камень, песок, губка, золото, тнт,')
print('трава, доски, дуб, кровать, кирпичи, обсидиан, сундук,')
block_name = input('верстак, печь, чаровальня, командный блок, наковальня:')
block_id = block_id_remider(block_name )

x, y, z = mc.player.getTilePos()
mc.setBlock(x,y,z,block_id )
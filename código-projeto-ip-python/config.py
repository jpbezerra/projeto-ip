"FALTA COLOCAR OUTRAS CONFIGS DOS INIMIGOS E ATAQUES E SE DER TEMPO COLOCAR O RESTO DAS ANIMAÇÕES (MÉDIA PRIORIDADE)"
"FALTA COMPLETAR O MAPA (NÃO CONSEGUI FUNDIR O CÓDIGO 100%, FALTARAM OS COLETÁVEIS) (ALTA PRIORIDADE)"

#BASIC CONFIGS
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 490
PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
KEY_LAYER = 2
GROUND_LAYER = 1
ENEMY_SPEED = 2
PLAYER_SPEED = 2
TILESIZE = 32
FPS = 60

# maze = [
#     'BBBBBBBBBBBBBBBBBBBB',
#     'B..................B',
#     'B.......P..........B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'B..................B',
#     'BBBBBBBBBBBBBBBBBBBB',
# ]

maze = [
        "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        "B..E..................E........................B",
        "B..........P...................................B",
        "B...............................BBBBBBB...BBBBBB",
        "B........................B.......B....B........B",
        "B.......1.........2......B............B........B",
        "B........................B............B........B",
        "B...........3............B.......B....B........B",
        "B........................B.......B....B........B",
        "B........................B.......B....B........B",
        "B........................B.......B....B........B",
        "B........................B.......B....B........B",
        "B........................BBBBBBBBB....B........B",
        "B.....................................B........B",
        "B..............................................B",
        "B..............................................B",
        "B.....................B...BBBBBBBBB.....BBBB...B",
        "B.....................B...B.......B........B...B",
        "B.....................B...B.......B........B...B",
        "B.....................B...B.......BBBBBBBBBB...B",
        "B.....................B...B....................B",
        "B.....................B...B....................B",
        "B.....................B...BBBBBBBBBBBBBBBBBBBBBB",
        "B.....................B........................B",
        "B.....................B........................B",
        "B.....................B........................B",
        "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        ]

#INTRO SCREEN
FONT_SIZE_INTRO_SCREEN = 32
INTRO_BUTTON_WIDTH = 150
INTRO_BUTTON_HEIGHT = 50

PLAY_BUTTON_X = 250
PLAY_BUTTON_Y = 75

EXIT_BUTTON_X = 250
EXIT_BUTTON_Y = 150


#SELECT SCREEN
FONT_SIZE_SELECT_SCREEN = 24

TITLE_SELECT_SCREEN_X = 110
TITLE_SELECT_SCREEN_Y = 25

SELECT_BUTTON_WIDTH = 125
SELECT_BUTTON_HEIGHT = 50

KNIGHT_BUTTON_X = 100
KNIGHT_BUTTON_Y = 75

MAGE_BUTTON_X = 425
MAGE_BUTTON_Y = 75

ARCHER_BUTTON_X = 100
ARCHER_BUTTON_Y = 275

ASSASSIN_BUTTON_X = 425
ASSASSIN_BUTTON_Y = 275

BACK_BUTTON_X = 250
BACK_BUTTON_Y = 375


#COLORS
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 204)
GREEN = (0, 204, 0)


"KNIGHT SPRITES"
#DOWN-ANIMATION
KNIGHT_DOWN_ANIMATION_WIDTH = 195

KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT = 298
KNIGHT_DOWN_ANIMATION_FRAME_2_3_HEIGHT = 315

KNIGHT_DOWN_ANIMATION_Y = 46

KNIGHT_DOWN_ANIMATION_FRAME_1_X = 422
KNIGHT_DOWN_ANIMATION_FRAME_2_X = 175
KNIGHT_DOWN_ANIMATION_FRAME_3_X = 669


"MAGE SPRITES"
#DOWN-ANIMATION
MAGE_DOWN_ANIMATION_WIDTH = 237

MAGE_DOWN_ANIMATION_HEIGHT = 317

MAGE_DOWN_ANIMATION_Y = 37

MAGE_DOWN_ANIMATION_FRAME_1_X = 405
MAGE_DOWN_ANIMATION_FRAME_2_X = 133
MAGE_DOWN_ANIMATION_FRAME_3_X = 678

"ARCHER SPRITES"
#DOWN ANIMATIONS
ARCHER_DOWN_ANIMATION_WIDTH = 165

ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT = 261
ARCHER_DOWN_ANIMATION_FRAME_2_3_HEIGHT = 277

ARCHER_DOWN_ANIMATION_Y = 69

ARCHER_DOWN_ANIMATION_FRAME_1_X = 437
ARCHER_DOWN_ANIMATION_FRAME_2_X = 189
ARCHER_DOWN_ANIMATION_FRAME_3_X = 685


"ASSASSIN SPRITES"
#DOWN ANIMATIONS
ASSASSIN_DOWN_ANIMATION_WIDTH = 125

ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT = 260
ASSASSIN_DOWN_ANIMATION_FRAME_2_3_HEIGHT = 277

ASSASSIN_DOWN_ANIMATION_Y = 61

ASSASSIN_DOWN_ANIMATION_FRAME_1_X = 453
ASSASSIN_DOWN_ANIMATION_FRAME_2_X = 253
ASSASSIN_DOWN_ANIMATION_FRAME_3_X = 645

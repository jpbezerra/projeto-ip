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
#     'BBBBBBBBBBBBBBBB',
#     'B..............B',
#     'B.......P......B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B..............B',
#     'B........E.....B',
#     'BBBBBBBBBBBBBBBB',
# ]

# maze = [
#         "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
#         "B...............................................................................B",
#         "B..........P....................................................................B",
#         "B................................................................BBBBBBB...BBBBBB",
#         "B.........................................................B.......B....B........B",
#         "B........................................1.........2......B............B........B",
#         "B.........................................................B............B........B",
#         "B............................................3............B.......B....B........B",
#         "B.........................................................B.......B....B........B",
#         "B.........................................................B.......B....B........B",
#         "B.........................................................B.......B....B........B",
#         "B.........................................................B.......B....B........B",
#         "B.........................................................BBBBBBBBB....B........B",
#         "B......................................................................B........B",
#         "B...............................................................................B",
#         "B...............................................................................B",
#         "B......................................................B...BBBBBBBBB.....BBBB...B",
#         "B......................................................B...B.......B........B...B",
#         "B......................................................B...B.......B........B...B",
#         "B......................................................B...B.......BBBBBBBBBB...B",
#         "B......................................................B...B....................B",
#         "B......................................................B...B....................B",
#         "B......................................................B...BBBBBBBBBBBBBBBBBBBBBB",
#         "B......................................................B........................B",
#         "B......................................................B........................B",
#         "B......................................................B........................B",
#         "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
#         ]

maze = [
        "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
        "B...............................................................................B",
        "B..........P....................................................................B",
        "B...............................................................................B",
        "B...............................................................................B",
        "B.....E.........E...........E............1.........2............................B",
        "B.....................E.........................................................B",
        "B............................................3..................................B",
        "B.........E.................E...................................................B",
        "B...............................................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B......................B........................................................B",
        "B...............................................................................B",
        "B...............................................................................B",
        "B...............................................................................B",
        "B...............................................................................B",
        "B...............................................................................B",
        "B...............................................................................B",
        "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
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

#UP-ANIMATION
KNIGHT_UP_ANIMATION_WIDTH = 173

KNIGHT_UP_ANIMATION_HEIGHT = 292

KNIGHT_UP_ANIMATION_Y = 37

KNIGHT_UP_ANIMATION_FRAME_1_X = 46
KNIGHT_UP_ANIMATION_FRAME_2_X = 219
KNIGHT_UP_ANIMATION_FRAME_3_X = 386

#RIGHT-ANIMATION
KNIGHT_RIGHT_ANIMATION_WIDTH = 181

KNIGHT_RIGHT_ANIMATION_HEIGHT = 317

KNIGHT_RIGHT_ANIMATION_Y = 5

KNIGHT_RIGHT_ANIMATION_FRAME_1_X = 21
KNIGHT_RIGHT_ANIMATION_FRAME_2_X = 230

#LEFT-ANIMATION
KNIGHT_LEFT_ANIMATION_WIDTH = 187

KNIGHT_LEFT_ANIMATION_HEIGHT = 315

KNIGHT_LEFT_ANIMATION_Y = 30

KNIGHT_LEFT_ANIMATION_FRAME_1_X = 38
KNIGHT_LEFT_ANIMATION_FRAME_2_X = 263


"MAGE SPRITES"
#DOWN-ANIMATION
MAGE_DOWN_ANIMATION_WIDTH = 237

MAGE_DOWN_ANIMATION_HEIGHT = 317

MAGE_DOWN_ANIMATION_Y = 37

MAGE_DOWN_ANIMATION_FRAME_1_X = 405
MAGE_DOWN_ANIMATION_FRAME_2_X = 133
MAGE_DOWN_ANIMATION_FRAME_3_X = 678

#UP-ANIMATION
MAGE_UP_ANIMATION_WIDTH = 233

MAGE_UP_ANIMATION_HEIGHT = 303

MAGE_UP_ANIMATION_Y = 31

MAGE_UP_ANIMATION_FRAME_X = 7


#RIGHT-ANIMATION
MAGE_RIGHT_ANIMATION_WIDTH = 216

MAGE_RIGHT_ANIMATION_HEIGHT = 313

MAGE_RIGHT_ANIMATION_Y = 39

MAGE_RIGHT_ANIMATION_FRAME_X = 39

#LEFT-ANIMATION
MAGE_LEFT_ANIMATION_WIDTH = 169

MAGE_LEFT_ANIMATION_HEIGHT = 337

MAGE_LEFT_ANIMATION_Y = 31

MAGE_LEFT_ANIMATION_FRAME_X = 23


"ARCHER SPRITES"
#DOWN ANIMATIONS
ARCHER_DOWN_ANIMATION_WIDTH = 165

ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT = 261
ARCHER_DOWN_ANIMATION_FRAME_2_3_HEIGHT = 277

ARCHER_DOWN_ANIMATION_Y = 69

ARCHER_DOWN_ANIMATION_FRAME_1_X = 437
ARCHER_DOWN_ANIMATION_FRAME_2_X = 189
ARCHER_DOWN_ANIMATION_FRAME_3_X = 685

#UP-ANIMATION
ARCHER_UP_ANIMATION_WIDTH = 161

ARCHER_UP_ANIMATION_HEIGHT = 249

ARCHER_UP_ANIMATION_Y = 63

ARCHER_UP_ANIMATION_FRAME_1_X = 47
ARCHER_UP_ANIMATION_FRAME_2_X = 213
ARCHER_UP_ANIMATION_FRAME_3_X = 375

#RIGHT-ANIMATION
ARCHER_RIGHT_ANIMATION_WIDTH = 129

ARCHER_RIGHT_ANIMATION_HEIGHT = 257

ARCHER_RIGHT_ANIMATION_Y = 63

ARCHER_RIGHT_ANIMATION_FRAME_1_X = 63
ARCHER_RIGHT_ANIMATION_FRAME_2_X = 199

#LEFT-ANIMATION
ARCHER_LEFT_ANIMATION_WIDTH = 121

ARCHER_LEFT_ANIMATION_HEIGHT = 257

ARCHER_LEFT_ANIMATION_Y = 63

ARCHER_LEFT_ANIMATION_FRAME_1_X = 63
ARCHER_LEFT_ANIMATION_FRAME_2_X = 202


"ASSASSIN SPRITES"
#DOWN ANIMATIONS
ASSASSIN_DOWN_ANIMATION_WIDTH = 125

ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT = 260
ASSASSIN_DOWN_ANIMATION_FRAME_2_3_HEIGHT = 277

ASSASSIN_DOWN_ANIMATION_Y = 61

ASSASSIN_DOWN_ANIMATION_FRAME_1_X = 453
ASSASSIN_DOWN_ANIMATION_FRAME_2_X = 253
ASSASSIN_DOWN_ANIMATION_FRAME_3_X = 645

#UP-ANIMATION
ASSASSIN_UP_ANIMATION_WIDTH = 121

ASSASSIN_UP_ANIMATION_HEIGHT = 263

ASSASSIN_UP_ANIMATION_Y = 63

ASSASSIN_UP_ANIMATION_FRAME_1_X = 63
ASSASSIN_UP_ANIMATION_FRAME_2_X = 209
ASSASSIN_UP_ANIMATION_FRAME_3_X = 351

#RIGHT-ANIMATION
ASSASSIN_RIGHT_ANIMATION_WIDTH = 121

ASSASSIN_RIGHT_ANIMATION_HEIGHT = 257

ASSASSIN_RIGHT_ANIMATION_Y = 79

ASSASSIN_RIGHT_ANIMATION_FRAME_1_X = 63
ASSASSIN_RIGHT_ANIMATION_FRAME_2_X = 197

#LEFT-ANIMATION
ASSASSIN_LEFT_ANIMATION_WIDTH = 121

ASSASSIN_LEFT_ANIMATION_HEIGHT = 257

ASSASSIN_LEFT_ANIMATION_Y = 79

ASSASSIN_LEFT_ANIMATION_FRAME_1_X = 63
ASSASSIN_LEFT_ANIMATION_FRAME_2_X = 197


"ENEMY SPRITES"
#DOWN ANIMATIONS
ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT = 283
ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT = 293

ENEMY_DOWN_ANIMATION_FRAME_1_Y = 53
ENEMY_DOWN_ANIMATION_FRAME_2_Y = 45

"KNIGHT ENEMY SPRITES"
KNIGHT_ENEMY_DOWN_ANIMATION_WIDTH = 180

KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_1_X = 62
KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_2_X = 310

"MAGE ENEMY SPRITES"
MAGE_ENEMY_DOWN_ANIMATION_WIDTH = 204

MAGE_ENEMY_DOWN_ANIMATION_FRAME_1_X = 54
MAGE_ENEMY_DOWN_ANIMATION_FRAME_2_X = 302

"ARCHER ENEMY SPRITES"
ARCHER_ENEMY_DOWN_ANIMATION_WIDTH = 164

ARCHER_ENEMY_DOWN_ANIMATION_FRAME_1_X = 62
ARCHER_ENEMY_DOWN_ANIMATION_FRAME_2_X = 301

"ASSASSIN ENEMY SPRITES"
ASSASSIN_ENEMY_DOWN_ANIMATION_WIDTH = 174

ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_1_X = 77
ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_2_X = 309


"BLOCK SPRITES"
WALL_X = 960
WALL_Y = 448


"GROUND SPRITES"
GROUND_X = 64
GROUND_Y = 352



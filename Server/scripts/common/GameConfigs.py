# -*- coding: utf-8 -*-

"""
"""

# ------------------------------------------------------------------------------
# entity state
# ------------------------------------------------------------------------------
ENTITY_STATE_UNKNOW									= -1
ENTITY_STATE_FREE										= 0
ENTITY_STATE_SEND                                       = 2
ENTITY_STATE_MAX    									= 4


# ------------------------------------------------------------------------------
# entity state
# ------------------------------------------------------------------------------
ROOM_STATE_UNKNOW					= -1
ROOM_STATE_FREE						= 0
ROOM_STATE_PLAYING					= 1
ROOM_STATE_MAX						= 4
#-------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# entity state
# ------------------------------------------------------------------------------
RESULT_OK							= 0   
EROOR_ROOM_NOT_FUND					= 10  #没有这个房间
EROOR_ROOM_CREATIN					= 11  #房间正在创建中
EROOR_ROOM_ENTERED					= 12  #房间正在创建中
EROOR_ROOM_DESTORYED				= 13  #房间已经销毁
EROOR_ROOM_EXIT_FAIL				= 14  #退出房间失败

#-------------------------------------------------------------------------------

#  一个房间最大人数
ROOM_MAX_PLAYER = 35

# 限制玩家最大分割数量
PLAYER_LIMIT_SPLIT = 16

#  一局游戏时间（秒）
GAME_ROUND_TIME = 720 #60 * 12




"""
Global configuration and game constants for THE FLOOR IS FOLLOWING YOU.
"""

import os
import sys

# Suppress pygame community welcome message so users don't confuse it with an error
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Ensure executable dir does not shadow system/site packages like pygame
_exe_dir = os.path.dirname(sys.executable)
if _exe_dir in sys.path:
    sys.path = [p for p in sys.path if os.path.normcase(p) != os.path.normcase(_exe_dir)]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
DATA_DIR = os.path.join(ROOT_DIR, "data")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

SAVE_FILE = os.path.join(DATA_DIR, "save.json")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")

# Display
TITLE = "THE FLOOR IS FOLLOWING YOU"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Physics & Player
PLAYER_WIDTH = 34
PLAYER_HEIGHT = 50
GRAVITY = 1450.0  # px / s^2 (optimized for airy, satisfying jumps)
PLAYER_MOVE_SPEED = 430.0  # max horizontal speed
PLAYER_ACCELERATION = 2900.0  # px / s^2
PLAYER_FRICTION = 2400.0  # px / s^2
PLAYER_JUMP_FORCE = -820.0  # Increased jump velocity for high, soaring leaps (~232px apex)
BOUNCE_JUMP_FORCE = -1180.0  # Bouncing platform launch velocity
SPRING_BOOST_MULTIPLIER = 1.35
TERMINAL_VELOCITY = 1100.0
COYOTE_TIME = 0.16  # Forgiving jump window after stepping off platform
JUMP_BUFFER_TIME = 0.20  # Forgiving jump buffer before landing

# Toxic Floor (Lava)
TOXIC_INITIAL_SPEED = 32.0  # px / s (gentle starting speed so early stage is easy to learn)
TOXIC_MAX_SPEED = 185.0  # Maximum cap to keep endgame fast yet fair
TOXIC_GRACE_PERIOD = 3.5  # Seconds before lava begins rising at start of game
TOXIC_PERIODIC_INTERVAL = 12.0  # Seconds between stepped periodic speed increases
TOXIC_PERIODIC_SPEED_STEP = 12.0  # Speed increase added at each periodic step
TOXIC_SPEED_ACCEL_HEIGHT = 0.025  # Speed bonus per 100m climbed
TOXIC_START_WORLD_Y = 1000.0  # Starts 450px below player starting position
TOXIC_WAVE_AMPLITUDE = 8.0
TOXIC_WAVE_SPEED = 3.5

# Power-ups
POWERUP_SIZE = 30
DURATION_SHIELD = 14.0
DURATION_SPRING = 11.0
DURATION_SLOWMO = 9.0
DURATION_MAGNET = 13.0
SLOWMO_SPEED_FACTOR = 0.45
MAGNET_RADIUS = 300.0
MAGNET_PULL_SPEED = 580.0

# Platforms
PLATFORM_DEFAULT_HEIGHT = 18
PLATFORM_MIN_WIDTH = 100
PLATFORM_MAX_WIDTH = 195
PLATFORM_VERTICAL_MIN_GAP = 80
PLATFORM_VERTICAL_MAX_GAP = 145  # Generous headroom compared to player jump height (~232px)
BREAKING_TIME = 0.85  # Ample time for player to react and jump before collapse
TEMPORARY_ACTIVE_TIME = 2.6
TEMPORARY_INACTIVE_TIME = 1.5

# Scoring
POINTS_PER_METER = 10  # 1 meter = 10 world pixels
POINTS_PER_COIN = 50
POINTS_PER_SECOND = 5

# Color Palette (RGB)
COLOR_BG_DEEP = (10, 14, 22)
COLOR_BG_MID = (18, 24, 38)
COLOR_BG_LIGHT = (28, 38, 56)
COLOR_GRID = (35, 48, 70)

COLOR_TOXIC = (57, 255, 60)
COLOR_TOXIC_BRIGHT = (140, 255, 120)
COLOR_TOXIC_DARK = (20, 95, 25)
COLOR_TOXIC_VAPOR = (65, 240, 90, 110)

COLOR_PLAYER = (245, 252, 255)
COLOR_PLAYER_CYAN = (0, 230, 255)
COLOR_PLAYER_EYES = (0, 255, 220)
COLOR_PLAYER_DARK = (45, 55, 75)

COLOR_PLATFORM_NORMAL = (85, 100, 118)
COLOR_PLATFORM_NORMAL_BORDER = (145, 165, 188)
COLOR_PLATFORM_MOVING = (40, 130, 210)
COLOR_PLATFORM_MOVING_BORDER = (100, 195, 255)
COLOR_PLATFORM_BREAKING = (195, 95, 45)
COLOR_PLATFORM_BREAKING_BORDER = (255, 145, 75)
COLOR_PLATFORM_BOUNCING = (225, 45, 125)
COLOR_PLATFORM_BOUNCING_BORDER = (255, 115, 185)
COLOR_PLATFORM_TEMPORARY = (140, 70, 220)
COLOR_PLATFORM_TEMPORARY_BORDER = (195, 135, 255)

COLOR_COIN = (255, 215, 20)
COLOR_COIN_EDGE = (255, 160, 0)
COLOR_COIN_GLOW = (255, 240, 120)

COLOR_SHIELD = (0, 220, 255)
COLOR_SPRING = (255, 110, 50)
COLOR_SLOWMO = (60, 245, 170)
COLOR_MAGNET = (215, 75, 255)

COLOR_WHITE = (255, 255, 255)
COLOR_MUTED = (165, 180, 200)
COLOR_PANEL_BG = (15, 20, 32, 225)
COLOR_PANEL_BORDER = (60, 80, 110)
COLOR_BTN_NORMAL = (30, 42, 62)
COLOR_BTN_HOVER = (48, 68, 100)
COLOR_BTN_ACTIVE = (20, 80, 140)
COLOR_DANGER = (255, 65, 80)

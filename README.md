# THE FLOOR IS FOLLOWING YOU

A fast-paced, modern 2D endless survival platformer built in Python 3 using Pygame.

You are trapped in an underground industrial labyrinth. Deep beneath your feet, a caustic, neon-green toxic liquid rises relentlessly from the subterranean abyss. Jump between floating steel girders, navigate hazards, grab golden coins, deploy experimental power-ups, and climb as high as possible before the rising toxic floor catches you.

---

## Game Overview

- **Title:** THE FLOOR IS FOLLOWING YOU
- **Genre:** 2D Endless Survival Platformer
- **Target Resolution:** 1280 × 720 (60 FPS)
- **Engine:** Pygame 2.6+
- **Platform:** Windows PC (Python 3.12 / 3.13)
- **Primary Mechanic:** Continuously accelerating rising toxic liquid floor with dynamic multi-frequency waves and proximity warning alerts.

---

## Key Features

### 1. Dynamic Platforming & Physics
- Responsive, momentum-based horizontal acceleration and deceleration with friction.
- Variable jump heights with dynamic jump cutting (short hops vs full leaps).
- Jump buffering and coyote time for ultra-forgiving, fluid control.
- Screen boundary clamping and velocity transfer when riding moving platforms.
- One-way platform detection: seamlessly jump up through platforms from below and land stably on top without tunneling.

### 2. Rising Toxic Liquid System
- Continuous upward rise that accelerates based on altitude climbed and survival duration.
- Procedural multi-wave liquid surface simulation.
- Emits buoyant toxic bubbles, luminous crest highlights, and vapor particles.
- Audio and visual proximity warnings trigger when the caustic liquid approaches critical range.

### 3. Procedural Platform Generation
- Mathematically bounded procedural generation guarantees every vertical and horizontal jump is reachable.
- Progressive difficulty scaling introduces narrower and more volatile platforms at higher altitudes:
  - **Normal Platforms:** Sturdy industrial steel beams with rivets and edge highlights.
  - **Moving Platforms:** Mechanized horizontal patrol platforms with chevron indicators.
  - **Breaking Platforms:** Cracked, crumbling hazard plates that fracture and collapse after contact.
  - **Bouncing Platforms:** High-tension pneumatic spring pads that fling the player skyward.
  - **Temporary Platforms:** Holographic forcefield barriers that phase on and off.

### 4. Collectibles & Tactical Power-Ups
- **Gold Coins:** Floating rotating coins with specular sheen and particle explosions (+50 pts & persistent wallet).
- **Shield:** Encases the player in a glowing kinetic sphere that absorbs one fatal liquid dip and propels them to safety.
- **Spring Boost:** Supercharges jump impulse by +35% for maximum vertical mobility.
- **Slow Motion:** Drops toxic liquid rise rate by 55% for precious breathing room.
- **Magnet:** Radiates an electromagnetic field drawing all nearby coins directly into the player.

### 5. Audiovisual Polish & Particle Engine
- High-performance particle engine handling toxic vapor, splashing bubbles, jump dust, crumbling rubble, and spark fountains.
- Parallax multi-layer industrial background with ventilation shafts, conduits, and ambient depth.
- Procedural audio synthesizer generating 16-bit PCM sound effects (jump, bounce, break, coin, powerup, warning, game over) and an atmospheric electronic soundtrack loop without requiring external binaries or downloads.
- Graceful silent audio fallback prevents crashes on headless or disabled audio devices.

### 6. Persistence & UI
- High score, lifetime coins, and stats automatically saved atomically to `data/save.json`.
- Settings menu with volume sliders, mute toggles, and fullscreen mode saved to `data/settings.json`.
- Complete interface including Main Menu, Interactive Tutorial, HUD with status indicators, Pause Screen, and Game Over scoreboard.

---

## Keyboard Controls

| Action | Primary Key | Alternate Key |
| :--- | :--- | :--- |
| **Move Left** | `A` | `Left Arrow` |
| **Move Right** | `D` | `Right Arrow` |
| **Jump / Play** | `Space` | `Up Arrow` / `W` |
| **Pause / Resume** | `ESC` | — |
| **Restart (Game Over)** | `R` | `Space` / `Enter` |

---

## Project Structure

```
the_floor_is_following_you/
├── main.py                  # Game entry point and 60 FPS master loop
├── config.py                # Global physics, gameplay constants, and palettes
├── requirements.txt         # Project dependencies
├── README.md                # Documentation and setup guide
│
├── game/                    # Core gameplay mechanics
│   ├── __init__.py
│   ├── game_manager.py      # State machine coordinator and renderer
│   ├── player.py            # Physics controller, animations, powerup state
│   ├── platform.py          # Platform types: Normal, Moving, Breaking, etc.
│   ├── platform_generator.py# Procedural generation with reachability solver
│   ├── toxic_floor.py       # Rising liquid mechanics and wave simulation
│   ├── camera.py            # Smooth vertical tracking and screen shake
│   ├── coin.py              # Collectible coins and magnet physics
│   ├── powerup.py           # Shield, Spring, Slow-mo, Magnet powerups
│   ├── collision.py         # One-way continuous collision detection
│   └── scoring.py           # Score, meters, and difficulty calculation
│
├── ui/                      # Visual interface modules
│   ├── __init__.py
│   ├── main_menu.py         # Main title screen and interactive tutorial modal
│   ├── pause_menu.py        # Pause overlay
│   ├── game_over.py         # Results summary and restart flow
│   ├── settings.py          # Audio sliders, mute toggles, fullscreen
│   ├── hud.py               # In-game score, height, timer, and powerup cards
│   └── buttons.py           # Animated UI buttons and volume sliders
│
├── systems/                 # Engine support systems
│   ├── __init__.py
│   ├── audio_manager.py     # Sound manager with procedural audio synth
│   ├── save_manager.py      # Atomic JSON save/load system
│   ├── particle_system.py   # Multi-emitter particle effects
│   └── asset_manager.py     # Procedural sprite generator and font manager
│
├── assets/                  # Game assets directory
│   ├── images/              # Custom sprite textures
│   ├── sounds/              # Synthesized 16-bit WAV audio effects
│   ├── music/               # Ambient cyberpunk music loop
│   └── fonts/               # Typography fallbacks
│
├── data/                    # Persistent local data
│   ├── save.json            # High score, total coins, and stats
│   └── settings.json        # Audio volume and display preferences
│
└── tests/                   # Automated unit and integration test suite
    ├── __init__.py
    ├── test_player.py       # Physics, movement, and jump buffer tests
    ├── test_platforms.py    # Collision and special platform behaviors
    ├── test_toxic_floor.py  # Liquid rise rate and collision mechanics
    ├── test_scoring.py      # Score calculations and stage transitions
    └── test_gameplay_integration.py # Full playthrough integration tests
```

---

## Installation Instructions

1. Clone or copy the project directory to your Windows machine:
   ```bash
   cd the_floor_is_following_you
   ```

2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

---

## How to Run the Game

Launch the game using standard Python:
```bash
python main.py
```

---

## Running the Automated Test Suite

To run all unit and integration tests:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

All 23 unit and integration tests will execute and verify player movement, collision detection, procedural generation, audio fallbacks, saving, and the gameplay loop.

---

## Troubleshooting

- **Audio Device Not Detected:**
  The game features an automated silent fallback mode. If no audio output device is present or `pygame.mixer` fails to initialize, the game will automatically continue in silent mode without crashing.
- **Window Scaling / HiDPI Displays:**
  If your display scaling is set higher than 100%, toggle Fullscreen mode via the in-game Settings menu or adjust display scaling in Windows Settings.
- **Resetting Save Data:**
  To reset high scores and saved progress, simply delete `data/save.json`. It will be recreated with fresh default statistics upon next launch.


## Vercel Deployment

This repository includes a Vercel-compatible WSGI `app` in `main.py`, so Vercel can build the project without the `PYTHON_ENTRYPOINT_NOT_FOUND` error.

Run the desktop game locally with:

```bash
python main.py
```

Vercel can host the web endpoint, but a serverless Python function cannot open a desktop Pygame window. The deployed `/` page confirms the deployment is live.

"""
THE FLOOR IS FOLLOWING YOU

This module serves two purposes:
- Vercel imports the top-level ``app`` WSGI application.
- Desktop users can still run the Pygame game with ``python main.py``.
"""

import os
import sys
import time

# Vercel/Python entrypoint. A plain WSGI callable avoids requiring Flask
# just to host the deployment status page.
def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    if path == "/health":
        body = b'{"status":"ok","game":"The Floor Is Following You"}'
        content_type = "application/json; charset=utf-8"
    else:
        body = b"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Floor Is Following You</title>
<style>
body{margin:0;min-height:100vh;background:#07100d;color:#e8fff0;font-family:system-ui,sans-serif;display:grid;place-items:center}
main{max-width:760px;padding:40px;text-align:center}
h1{font-size:clamp(2rem,7vw,4rem);margin:.2em 0;color:#7dff72}
p{line-height:1.6;color:#b9c9bf}
.card{margin-top:24px;padding:24px;border:1px solid #274e39;border-radius:16px;background:#0c1b15}
code{color:#7dff72}
</style>
</head>
<body><main>
<h1>THE FLOOR IS FOLLOWING YOU</h1>
<p>A fast-paced 2D endless survival platformer built with Python and Pygame.</p>
<div class="card">
<strong>Vercel deployment is online.</strong>
<p>The desktop Pygame game runs with <code>python main.py</code>. Vercel hosts this web endpoint; it cannot run a desktop Pygame window directly.</p>
</div>
</main></body>
</html>"""
        content_type = "text/html; charset=utf-8"

    start_response("200 OK", [
        ("Content-Type", content_type),
        ("Content-Length", str(len(body))),
    ])
    return [body]

def run_game():
    """Start the original desktop Pygame game."""
    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

    import pygame
    import config
    from game.game_manager import GameManager

    pygame.init()
    pygame.font.init()
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.display.set_caption(config.TITLE)
    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
    )

    icon_surf = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.circle(icon_surf, config.COLOR_BG_DEEP, (16, 16), 15)
    pygame.draw.circle(icon_surf, config.COLOR_TOXIC_BRIGHT, (16, 16), 14, 2)
    pygame.draw.circle(icon_surf, config.COLOR_TOXIC, (16, 16), 6)
    pygame.display.set_icon(icon_surf)

    clock = pygame.time.Clock()
    game_manager = GameManager(screen, clock)
    last_time = time.perf_counter()

    while game_manager.running:
        current_time = time.perf_counter()
        dt = current_time - last_time
        last_time = current_time
        game_manager.handle_events()
        game_manager.update(dt)
        game_manager.draw()
        clock.tick(config.FPS)

    pygame.quit()

if __name__ == "__main__":
    run_game()

import gymnasium as gym
import minigrid
from minigrid.core.world_object import Door

# order from easiest to hardest
LEVELS = [
    "MiniGrid-KeyCorridorS3R1-v0",
    "MiniGrid-KeyCorridorS3R2-v0",
    "MiniGrid-KeyCorridorS3R3-v0",
    "MiniGrid-KeyCorridorS4R3-v0",
    "MiniGrid-KeyCorridorS5R3-v0",
    "MiniGrid-KeyCorridorS6R3-v0",
]

# Hold-out seeds for evaluation DONT TEST WITH THESE!!!!!
EVAL_SEEDS = list(range(1_000_000, 1_000_000))

def make_env(level, render_mode=None):
    return gym.make(level, render_mode=render_mode)

def find_locked_door(env):
    """Locked doors arent stored so have to scan the gird for them"""
    grid = env.unwrapped.grid
    for obj in grid.grid:
        if isinstance(onj, Door) and obj.is_locked:
            return obj
    raise RuntimeError("No locked door found - call after reset()")
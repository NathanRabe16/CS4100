"""Evaluation harness for all agents"""
import pandas as pd
from minigrid.core.world_object import Key
from envs import make_env, find_locked_door

def run_episode(env, agent, seed):
    obs, _ = env.reset(seed=seed)
    agent.reset()
    door = find_locked_door(env)

    total_reward = 0.0
    steps = 0
    got_key = False
    opened_door = False
    done = False

    while not done:
        action = agent.take_action(obs)
        obs, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        steps += 1
        done = terminated or truncated

        if isinstance(env.unwrapped.carrying, Key):
            got_key = True
        if door.is_open:
            opened_door = True

    return {
        "seed": seed,
        "success": total_reward > 0,
        "return": total_reward,
        "length": steps,
        "got_key": got_key,
        "opened_door": opened_door,
    }

def evaluate(agent, level, seeds):
    env = make_env(level)
    rows = [run_episode(env, agent, s) for s in seeds]
    env.close()
    df = pd.DataFrame(rows)
    df.insert(0, "level", level)
    return df
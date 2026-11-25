"""Evaluate the random agent on the six levels across the hold-out seeds."""
from pathlib import Path

import pandas as pd

from agents import RandomAgent
from envs import EVAL_SEEDS, LEVELS
from evaluation import evaluate

Path("results").mkdir(exist_ok=True)

frames = []
for level in LEVELS:
    agent = RandomAgent(seed=0)
    df = evaluate(agent, level, EVAL_SEEDS)
    frames.append(df)
    print(f"{level}: success={df.success.mean():.0%}  "
        f"return={df['return'].mean():.3f}  length={df.length.mean():.0f}  "
        f"got_key={df.got_key.mean():.0%}  opened_door={df.opened_door.mean():.0%}")

results = pd.concat(frames)
results.to_csv("results/random_agent.csv", index=False)

summary = results.groupby("level", sort=False)[
    ["success", "return", "length", "got_key", "opened_door"]].mean()
print("\n", summary.round(3))
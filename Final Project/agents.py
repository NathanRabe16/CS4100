"""Shared interface for agents"""
import numpy as np


class RandomAgent:
    """Picks one action randomly"""

    def __init__(self, n_actions=7, seed=0):
        self.n_actions = n_actions
        self.rng = np.random.default_rng(seed)

    def reset(self):
        pass #no memory need

    def take_action(self, obs):
        return int(self.rng.integers(self.n_actions))
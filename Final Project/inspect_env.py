"""Save pictures of a few layouts per level and print basic env facts."""
from pathlib import Path
import matplotlib.pyplot as plt
from envs import LEVELS, make_env

out = Path("figures/layouts")
out.mkdir(parents=True, exist_ok=True)

for level in LEVELS:
    env = make_env(level, render_mode="rgb_array")
    obs, _ = env.reset(seed=0)
    u = env.unwrapped
    print(f"{level}: grid {u.width}x{u.height}, max_steps={u.max_steps}, "
        f"actions={env.action_space.n}, image={obs['image'].shape}, "
        f"mission='{obs['mission']}'")

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for ax, seed in zip(axes, [0, 1, 2]):
        env.reset(seed=seed)
        ax.imshow(env.render())
        ax.set_title(f"seed {seed}")
        ax.axis("off")
    fig.suptitle(level)
    fig.savefig(out / f"{level}.png", bbox_inches="tight")
    plt.close(fig)
    env.close()

print(f"Saved layout images to {out}/")
import numpy as np
import matplotlib.pyplot as plt

num_flips = 1000
num_rolls = 1000

coin_flips = np.random.randint(0, 2, num_flips)

heads = np.count_nonzero(coin_flips == 1)
tails = np.count_nonzero(coin_flips == 0)

dice_rolls = np.random.randint(1, 7, num_rolls)

dice_counts = np.bincount(dice_rolls)[1:]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(['Heads', 'Tails'], [heads, tails], color=['gold', 'lightblue'], edgecolor='black')
plt.title("Coin Flip Simulation (1000 flips)")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.bar(np.arange(1, 7), dice_counts, color='lightgreen', edgecolor='black')
plt.title("Dice Roll Simulation (1000 rolls)")
plt.xlabel("Dice Face")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

print("---- Simulation Results ----")
print(f"Heads: {heads}")
print(f"Tails: {tails}")
print("Dice Rolls Frequency:", dice_counts)

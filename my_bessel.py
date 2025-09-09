import matplotlib.pyplot as plt
import pandas as pd

files = ["bessel0.dat", "bessel3.dat", "bessel5.dat", "bessel8.dat"]
orders = [0, 3, 5, 8]

# dictionary to store DataFrames
df_dict = {}

for file, order in zip(files, orders):
    # read the file into a DataFrame
    df = pd.read_csv(
        file,
        skiprows=2,
        sep=r"\s+",
        names=["x", "down", "up"]
    )
    
    df_dict[order] = df

    
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, order in zip(axes, orders):
    df = df_dict[order]
    
    ax.plot(df["x"], df["down"], label="down", lw=2)
    ax.plot(df["x"], df["up"],   label="up",   lw=2, linestyle="--")
    
    ax.axhline(0, color="grey", lw=1, linestyle="-") # just darkens y=0 line
    ax.set_title(f"$J_{order}(x)$", fontsize=14)
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    ax.legend(fontsize=10)
    ax.minorticks_on()  # enable minor ticks
    ax.set_xlabel("x")
    ax.set_ylabel(f"$J_{order}(x)$")

fig.suptitle("Up vs down methods", fontsize=16)
plt.subplots_adjust(hspace=0.3)  # increase vertical spacing
plt.tight_layout()
plt.savefig("bessel_plots.png", dpi=300)
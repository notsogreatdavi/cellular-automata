import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation, PillowWriter

# Configurações do Grid
GRID_SIZE = 100
FIRE_PROB = 0.6
STEPS = 200
WIND_DIRECTION = "E"

# Estados das células
EMPTY = 0
TREE = 1
FIRE = 2 

cmap = ListedColormap(["black", "green", "red"])

def initialize_grid(size):
    grid = np.random.choice([EMPTY, TREE], size=(size, size), p=[0.2, 0.8])
    grid[size // 2, size // 2] = FIRE
    return grid

def wind_adjusted_prob(x, y, i, j, fire_prob, wind_direction):
    if wind_direction == "S" and x < i:
        return fire_prob * 1.5
    elif wind_direction == "N" and x > i:  
        return fire_prob * 1.5
    elif wind_direction == "W" and y > j:
        return fire_prob * 1.5
    elif wind_direction == "E" and y < j:  
        return fire_prob * 1.5
    else:
        return fire_prob

def update_grid(grid, fire_prob, wind_direction):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == FIRE:
                new_grid[i, j] = EMPTY
            elif grid[i, j] == TREE:
                neighbors = [
                    (x, y)
                    for x, y in [
                        (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
                    ]
                    if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]
                ]
                for x, y in neighbors:
                    if grid[x, y] == FIRE:
                        prob = wind_adjusted_prob(x, y, i, j, fire_prob, wind_direction)
                        if np.random.random() < prob:
                            new_grid[i, j] = FIRE
                            break
    return new_grid

def add_wind_arrows(ax, wind_direction):
    if wind_direction == "N":
        U, V = np.zeros((GRID_SIZE, GRID_SIZE)), np.ones((GRID_SIZE, GRID_SIZE))
    elif wind_direction == "S":
        U, V = np.zeros((GRID_SIZE, GRID_SIZE)), -np.ones((GRID_SIZE, GRID_SIZE))
    elif wind_direction == "E":
        U, V = np.ones((GRID_SIZE, GRID_SIZE)), np.zeros((GRID_SIZE, GRID_SIZE))
    elif wind_direction == "W":
        U, V = -np.ones((GRID_SIZE, GRID_SIZE)), np.zeros((GRID_SIZE, GRID_SIZE))
    else:
        U, V = np.zeros((GRID_SIZE, GRID_SIZE)), np.zeros((GRID_SIZE, GRID_SIZE))
    
    spacing = 25
    x, y = np.meshgrid(np.arange(0, GRID_SIZE, spacing), np.arange(0, GRID_SIZE, spacing))
    u, v = U[::spacing, ::spacing], V[::spacing, ::spacing]
    ax.quiver(x+10, y+10, u, v, color="blue", scale=20)
    
def update_animation(frame, img, fire_prob, wind_direction, ax):
    global current_grid
    current_grid = update_grid(current_grid, fire_prob, wind_direction)
    img.set_array(current_grid)
    if np.count_nonzero(current_grid == FIRE) == 0:
        ani.event_source.stop()
    return [img]

# Grid e animação
current_grid = initialize_grid(GRID_SIZE)
fig, ax = plt.subplots(figsize=(10, 10))
ax.axis("off")
img = ax.imshow(current_grid, cmap=cmap, interpolation="nearest")
add_wind_arrows(ax, WIND_DIRECTION)
ani = FuncAnimation(
    fig, update_animation, frames=STEPS,
    fargs=(img, FIRE_PROB, WIND_DIRECTION, ax), interval=100, blit=False
)
writer = PillowWriter(fps=10)
ani.save("images/fire_simulation_with_wind.gif", writer=writer, dpi=100)
print("GIF salvo como 'fire_simulation_with_wind.gif'.")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation, PillowWriter

# Configurações do Grid
GRID_SIZE = 150
FIRE_PROB = 0.6
STEPS = 100 
WIND_DIRECTION = "S" 

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
    if wind_direction == "N" and x < i:  
        return fire_prob * 1.5
    elif wind_direction == "S" and x > i:  
        return fire_prob * 1.5
    elif wind_direction == "E" and y > j:  
        return fire_prob * 1.5
    elif wind_direction == "W" and y < j:  
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

# animação
def update_animation(frame, img, fire_prob, wind_direction):
    global current_grid
    current_grid = update_grid(current_grid, fire_prob, wind_direction)
    img.set_array(current_grid)
    if np.count_nonzero(current_grid == FIRE) == 0:
        ani.event_source.stop()
    return [img]

# Grid e gif
current_grid = initialize_grid(GRID_SIZE)
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis("off")
img = ax.imshow(current_grid, cmap=cmap, interpolation="nearest")
ani = FuncAnimation(fig, update_animation, frames=STEPS, fargs=(img, FIRE_PROB, WIND_DIRECTION), interval=300, blit=True)
writer = PillowWriter(fps=3)
ani.save("images/fire_simulation_with_wind.gif", writer=writer, dpi=100)
print("GIF salvo como 'fire_simulation_with_wind.gif'.")

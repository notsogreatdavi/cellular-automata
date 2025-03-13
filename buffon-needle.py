import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros do experimento
needle_length = 1
line_spacing = 1  # Espaçamento reduzido entre as faixas
num_needles = 0
cross_count = 0
gravity = 0.1  # Simulação da gravidade
bounce_damping = 0.1  # Redução da velocidade no ricochete

needles = []
division_results = []  # Armazena os resultados das divisões para plotar no círculo

# Criando a figura e subplots
fig = plt.figure(figsize=(10, 6))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1])

# Subplot para o círculo
ax_circle = fig.add_subplot(gs[0])
ax_circle.set_aspect('equal')
ax_circle.axis('off')

# Subplot para a simulação 3D
ax_simulation = fig.add_subplot(gs[1], projection="3d")
ax_simulation.set_xlim(-5, 5)
ax_simulation.set_ylim(-5, 5)
ax_simulation.set_zlim(0, 10)
ax_simulation.set_xticks([])
ax_simulation.set_yticks([])
ax_simulation.set_zticks([])

# Desenhar o círculo representando π
circle = plt.Circle((0, 0), 1, color='lightgrey', alpha=0.5)
ax_circle.add_patch(circle)

# Criar o chão em perspectiva 3D com menor espaçamento entre as faixas
for i in np.arange(-5, 6, line_spacing):
    ax_simulation.plot([i, i], [-5, 5], [0, 0], color="black", linewidth=2)

# Função para verificar cruzamento com linhas divisórias
def cruza_divisoria(x1, y1, x2, y2, largura_faixa):
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    # Calcula o coeficiente angular da linha do graveto (m)
    if x2 - x1 != 0:
        m = (y2 - y1) / (x2 - x1)
    else:
        m = float('inf')  # Agulha vertical

    # Verifica as linhas divisórias entre x1 e x2
    divisorias = range(int(x1 // largura_faixa) + 1, int(x2 // largura_faixa) + 1)

    # Testa cada linha divisória
    for k in divisorias:
        x_div = k * largura_faixa  # Posição da linha divisória

        # Se for vertical, cruza todas as divisórias entre x1 e x2
        if m == float('inf'):
            return True

        # Calcula o ponto de interseção da agulha com a linha divisória
        y_interseccao = m * (x_div - x1) + y1

        # Se a interseção estiver entre y1 e y2, a agulha cruzou a linha
        if min(y1, y2) <= y_interseccao <= max(y1, y2):
            return True

    return False

# Classe da Agulha com Física
class Needle:
    def __init__(self, x_center, y_center, z_start, theta):
        self.x_center = x_center
        self.y_center = y_center
        self.z = z_start
        self.velocity = 0

        # Calcula as extremidades da agulha no plano XY
        self.x1 = x_center + (needle_length / 2) * np.cos(theta)
        self.x2 = x_center - (needle_length / 2) * np.cos(theta)
        self.y1 = y_center + (needle_length / 2) * np.sin(theta)
        self.y2 = y_center - (needle_length / 2) * np.sin(theta)

        # Verifica se cruzou alguma divisória usando a nova lógica
        self.cross = cruza_divisoria(self.x1, self.y1, self.x2, self.y2, line_spacing)
        self.color = "gray"

        # Desenha a agulha
        self.needle_line, = ax_simulation.plot([self.x1, self.x2], [self.y1, self.y2], [self.z, self.z], color=self.color, lw=2)

    def update(self):
        # Simulação da queda com gravidade
        if self.z > 0:
            self.velocity -= gravity
            self.z += self.velocity
            if self.z <= 0:
                self.z = 0
                self.velocity = -self.velocity * bounce_damping
                self.color = "red" if self.cross else "blue"
                self.needle_line.set_color(self.color)

        self.needle_line.set_data([self.x1, self.x2], [self.y1, self.y2])
        self.needle_line.set_3d_properties([self.z, self.z])

# Função de animação para lançamento das agulhas
def update(frame):
    global num_needles, cross_count

    # Gerar posição e ângulo aleatórios para a agulha
    x_center = np.random.uniform(-5, 5)
    y_center = np.random.uniform(-5, 5)
    z_start = np.random.uniform(8, 12)
    theta = np.random.uniform(0, np.pi)

    # Criar uma nova agulha com física
    new_needle = Needle(x_center, y_center, z_start, theta)
    needles.append(new_needle)

    # Atualizar contadores
    num_needles += 1
    cross_count += new_needle.cross

    # Estimativa de pi (ou aproximação pela proporção)
    division_result = num_needles * 2 / cross_count if cross_count > 0 else 0
    division_results.append(division_result)

    # Atualizar título
    ax_simulation.set_title(f"Needles Dropped = {num_needles}\n"
                            f"Needles Crossing = {cross_count}\n"
                            f"{num_needles} * 2 ÷ {cross_count} = {division_result:.4f}",
                            loc="center", fontsize=10)

    # Atualizar pontos no círculo
    ax_circle.cla()
    ax_circle.add_patch(circle)
    ax_circle.axis('off')

    # Plotar os pontos ao redor do círculo e conectar com uma linha
    x_points = []
    y_points = []
    for i, result in enumerate(division_results):
        angle = 2 * np.pi * i / len(division_results)
        x = np.cos(angle) * 1
        y = np.sin(angle) * 1
        x_points.append(x)
        y_points.append(y)
        ax_circle.scatter(x, y, color='red', s=10)

    # Desenhar a linha conectando os pontos
    ax_circle.plot(x_points, y_points, color='blue', linewidth=1)

    # Mostrar a quantidade de agulhas jogadas no último ponto
    if division_results:
        ax_circle.text(x_points[-1], y_points[-1], f"{num_needles}", fontsize=12, ha='right')

    # Acelerar a jogada das agulhas
    ani_main.event_source.interval = max(100, 800 - frame * 10)

# Função para animar a queda das agulhas
def animate_needles(i):
    for needle in needles:
        needle.update()

# Criar animação principal (lançamento das agulhas)
ani_main = animation.FuncAnimation(fig, update, interval=800)

# Animação secundária (queda das agulhas)
ani_fall = animation.FuncAnimation(fig, animate_needles, frames=10, interval=50, repeat=True)

plt.show()

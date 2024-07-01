import pygame
import serial
import math
import threading

# Inicializa a porta serial
try:
    myPort = serial.Serial("COM3", 115200, timeout=1)
except Exception as e:
    print(f"Erro ao abrir a porta serial: {e}")
    exit()

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela
width, height = 1300, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Radar")

# Define as cores
green = (26, 153, 146)
red = (97, 237, 132)
black = (0, 0, 0)
semi_transparent_black = (0, 0, 0, 4)  # Cor preta semi-transparente

# Carrega a fonte
font = pygame.font.Font(None, 40)

iAngle = 0
iDistance = 0

def read_serial_thread():
    global iAngle, iDistance
    while True:
        try:
            data = myPort.readline().decode('ascii').strip()
            if data:
                angle, distance = data.split(',')
                iAngle = int(angle)
                iDistance = int(distance)
        except Exception as e:
            print(f"Erro na leitura da porta serial: {e}")

def draw_radar():
    center_x, center_y = width // 2, int(0.926 * height)
    pygame.draw.arc(screen, green, (center_x - int(0.9375 * width // 2), center_y - int(0.9375 * width // 2), int(0.9375 * width), int(0.9375 * width)), math.pi, 2 * math.pi, 2)
    pygame.draw.arc(screen, green, (center_x - int(0.7300 * width // 2), center_y - int(0.7300 * width // 2), int(0.7300 * width), int(0.7300 * width)), math.pi, 2 * math.pi, 2)
    pygame.draw.arc(screen, green, (center_x - int(0.5210 * width // 2), center_y - int(0.5210 * width // 2), int(0.5210 * width), int(0.5210 * width)), math.pi, 2 * math.pi, 2)
    pygame.draw.arc(screen, green, (center_x - int(0.3130 * width // 2), center_y - int(0.3130 * width // 2), int(0.3130 * width), int(0.3130 * width)), math.pi, 2 * math.pi, 2)
    for angle in range(30, 151, 30):
        x = int(center_x + (width // 2) * math.cos(math.radians(angle)))
        y = int(center_y - (width // 2) * math.sin(math.radians(angle)))
        pygame.draw.line(screen, green, (center_x, center_y), (x, y), 2)
    pygame.draw.line(screen, green, (0, center_y), (width, center_y), 2)

def draw_object():
    center_x, center_y = width // 2, int(0.926 * height)
    pixs_distance = int(iDistance * 0.020835 * height)
    if iDistance < 40 and iDistance != 0:
        cos_a = math.cos(math.radians(iAngle))
        sin_a = math.sin(math.radians(iAngle))
        x1 = center_x + int(pixs_distance * cos_a)
        y1 = center_y - int(pixs_distance * sin_a)
        x2 = center_x + int(0.495 * width * cos_a)
        y2 = center_y - int(0.495 * width * sin_a)
        pygame.draw.line(screen, red, (x1, y1), (x2, y2), 9)

def draw_line():
    center_x, center_y = width // 2, int(0.926 * height)
    angle = math.radians(iAngle)
    x = int(center_x + 0.88 * height * math.cos(angle))
    y = int(center_y - 0.88 * height * math.sin(angle))
    pygame.draw.line(screen, (132, 184, 171), (center_x, center_y), (x, y), 3)

def draw_text():
    screen.fill(black, (0, int(0.9352 * height), width, height))

    object_text = font.render(f"Object: {'Out of Range' if iDistance > 40 else 'In Range'}", True, green)
    screen.blit(object_text, (int(0.125 * width), int(0.9723 * height)))

    angle_text = font.render(f"Angle: {iAngle} °", True, green)
    screen.blit(angle_text, (int(0.52 * width), int(0.9723 * height)))

    distance_label_text = font.render("Distance: ", True, green)
    screen.blit(distance_label_text, (int(0.71 * width), int(0.9723 * height)))

    if iDistance < 40:
        distance_value_text = font.render(f"{iDistance} cm", True, green)
        screen.blit(distance_value_text, (int(0.82 * width), int(0.9723 * height)))

# Thread para leitura serial
serial_thread = threading.Thread(target=read_serial_thread, daemon=True)
serial_thread.start()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Preencher a tela com uma cor semi-transparente (necessita de uma superfície adicional)
    overlay = pygame.Surface((width, int(0.935 * height)), pygame.SRCALPHA)
    overlay.fill(semi_transparent_black)
    screen.blit(overlay, (0, 0))

    draw_radar()
    draw_line()
    draw_object()
    draw_text()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()

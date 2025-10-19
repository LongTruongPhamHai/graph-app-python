from styles import *

import pygame

pygame.init()

screen = pygame.display.set_mode((1400, 700))

form = pygame.Rect(-1, -1, 983, 50)

pos_box = pygame.Rect(form.right - 1, -1, 420, 50)
algorithm_box = pygame.Rect(1, 50, 199, 549)
graph_box = pygame.Rect(algorithm_box.right, 50, 780, 549)
point_list_box = pygame.Rect(graph_box.right, 49, 420, 551)
result_box = pygame.Rect(-1, graph_box.bottom + 1, 1400, 100)

input_1 = pygame.Rect(form.left + 105, form.top + 9, 100, 30)
input_2 = pygame.Rect(input_1.right + 110, form.top + 9, 100, 30)
input_3 = pygame.Rect(input_2.right + 110, form.top + 9, 100, 30)

cancel_btn = pygame.Rect(form.right - 75, input_2.top, 70, 30)
submit_btn = pygame.Rect(cancel_btn.left - 75, input_2.top, 70, 30)
reset_btn = pygame.Rect(graph_box.right - 59, graph_box.top - 2, 60, 30)
change_btn = pygame.Rect(reset_btn.left - 129, graph_box.top - 2, 125, 30)
clear_btn = pygame.Rect(change_btn.left - 64, graph_box.top - 2, 60, 30)


def draw_textbox(rect, content):
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)
    screen.blit(TEXT.render(content, True, BLACK), (rect.left + 10, rect.top + 7))


breadth_fs_btn = pygame.Rect(algorithm_box.left + 5, algorithm_box.top + 40, 180, 30)
b_a_b_s_btn = pygame.Rect(algorithm_box.left + 5, breadth_fs_btn.top + 40, 180, 30)
hill_s_btn = pygame.Rect(algorithm_box.left + 5, b_a_b_s_btn.top + 40, 180, 30)

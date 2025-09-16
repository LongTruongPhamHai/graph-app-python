from styles import *

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 600))

form = pygame.Rect(-1, -1, 783, 50)

pos_box = pygame.Rect(form.right - 1, -1, 220, 50)
graph_box = pygame.Rect(1, 50, 780, 549)
point_list_box = pygame.Rect(graph_box.right, 49, 220, 551)

input_1 = pygame.Rect(form.left + 105, form.top + 9, 100, 30)
input_2 = pygame.Rect(input_1.right + 110, form.top + 9, 100, 30)
input_3 = pygame.Rect(input_2.right + 110, form.top + 9, 100, 30)

cancel_btn = pygame.Rect(form.right - 75, input_2.top, 70, 30)
submit_btn = pygame.Rect(cancel_btn.left - 75, input_2.top, 70, 30)
reset_btn = pygame.Rect(graph_box.right - 59, graph_box.top - 2, 60, 30)
change_btn = pygame.Rect(reset_btn.left - 129, graph_box.top - 2, 125, 30)


def draw_textbox(rect, content):
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)
    screen.blit(TEXT.render(content, True, BLACK), (rect.left + 10, rect.top + 7))

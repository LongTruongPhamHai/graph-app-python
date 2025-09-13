from styles import *
from elements import *
from draws import *
from features import *
import config

import pygame

pygame.init()

pygame.display.set_caption("Vẽ đồ thị")


draw_form()
draw_pos_box(config.mode, config.input_pos, 0, 0)
draw_graph_box(config.mode)
draw_point_list_box()

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():

        mx, my = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION and input_pos == 0:
            draw_pos_box(mode, input_pos, mx, my)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_btn.collidepoint(mx, my):
                point_list.clear()
                line_list.clear()
                reset_form(
                    point_name,
                    point_value,
                    input_pos,
                    show_form,
                    start_point,
                    end_point,
                )
                remake_graph(point_list, line_list, mode)
                draw_form(
                    False,
                    mode,
                    point_name,
                    point_value,
                    start_point,
                    end_point,
                )

            if change_btn.collidepoint(mx, my):
                mode = 1 if mode == 0 else 0
                reset_form(
                    point_name,
                    point_value,
                    input_pos,
                    show_form,
                    start_point,
                    end_point,
                )
                remake_graph(point_list, line_list, mode)
                draw_form(
                    False,
                    mode,
                    point_name,
                    point_value,
                    start_point,
                    end_point,
                )

            elif not show_form and graph_box.collidepoint(mx, my):
                show_form, input_pos = True, 1
                current_point = (mx, my)

                if mode == 0:
                    pygame.draw.circle(screen, RED, current_point, 10)
                    draw_pos_box(mode, input_pos, 1000, 1000)
                    show_form = True
                    draw_form(
                        show_form, mode, point_name, point_value, start_point, end_point
                    )

                elif mode == 1:
                    current_point = find_point(mx, my, point_list)
                    if current_point != ():
                        draw_pos_box(mode, input_pos, 1000, 1000)
                        show_form = True
                        draw_form(
                            False,
                            mode,
                            point_name,
                            point_value,
                            start_point,
                            end_point,
                        )

    draw_form(show_form, mode, point_name, point_value, start_point, end_point)

    pygame.display.flip()

pygame.quit()

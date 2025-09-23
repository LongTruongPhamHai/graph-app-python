from styles import *
from elements import *
from draws import *
from features import *
from algorithms import *
import config

import pygame

pygame.init()

pygame.display.set_caption("Vẽ đồ thị")


draw_form()
draw_pos_box(0, 0)
draw_algorithm_box()
draw_graph_box()
draw_point_list_box()
draw_result_box()

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():

        mx, my = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION and config.input_pos == 0:
            draw_pos_box(mx, my)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_btn.collidepoint(mx, my):
                config.point_list.clear()
                config.line_list.clear()
                reset_form()
                remake_graph()
                draw_form()

            elif change_btn.collidepoint(mx, my):
                config.mode = 1 if config.mode == 0 else 0
                reset_form()
                remake_graph()
                draw_form()

            elif cancel_btn.collidepoint(mx, my):
                config.show_form = False
                reset_form()
                remake_graph()
                draw_form()

            elif breadth_fs_btn.collidepoint(mx, my):
                config.show_form = True
                config.input_pos = 1
                config.mode = 2
                draw_pos_box(1000, 1000)
                draw_form()

            elif submit_btn.collidepoint(mx, my):
                if config.mode == 0:
                    save_point()
                elif config.mode == 1:
                    save_line()
                elif config.mode == 2:
                    breadth_first_search(config.start, config.finish)

                config.show_form = False
                reset_form()
                draw_form()
                remake_graph()
                draw_pos_box(mx, my)

            elif (
                not config.show_form
                and graph_box.collidepoint(mx, my)
                and config.mode == 0
            ):
                config.current_point = (mx, my)

                pygame.draw.circle(screen, RED, config.current_point, 10)
                config.show_form = True
                config.input_pos = 1
                draw_pos_box(1000, 1000)
                draw_form()

            elif graph_box.collidepoint(mx, my) and config.mode == 1:
                current_point = find_point(mx, my)
                if current_point:
                    if not config.start_point:
                        config.start_point = current_point
                        mark_start_point()
                        config.input_pos = 2
                    elif not config.end_point:
                        config.end_point = current_point
                        mark_end_point()
                        config.input_pos = 3

                    draw_pos_box(1000, 1000)
                    config.show_form = True
                    draw_form()

            elif config.show_form:
                if input_1.collidepoint(mx, my):
                    config.input_pos = 1
                    draw_pos_box(1000, 1000)

                elif input_2.collidepoint(mx, my):
                    config.input_pos = 2
                    draw_pos_box(1000, 1000)

        if event.type == pygame.KEYDOWN and config.show_form:
            if config.mode == 0:
                if config.input_pos == 1:
                    if event.unicode.isalpha() and len(config.point_name) < 3:
                        config.point_name += event.unicode.upper()

                    if event.key == pygame.K_BACKSPACE:
                        config.point_name = config.point_name[:-1]

                elif config.input_pos == 2:
                    if event.unicode.isdigit() and len(config.point_value) < 5:
                        config.point_value += event.unicode

                    if event.key == pygame.K_BACKSPACE:
                        config.point_value = config.point_value[:-1]

            elif config.mode == 1 and config.input_pos == 3:
                if event.unicode.isdigit() and len(config.line_value) < 5:
                    config.line_value += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    config.line_value = config.line_value[:-1]

            elif config.mode == 2:
                if config.input_pos == 1:
                    if event.unicode.isalpha() and len(config.start) < 3:
                        config.start += event.unicode.upper()

                    if event.key == pygame.K_BACKSPACE:
                        config.start = config.start[:-1]

                elif config.input_pos == 2:
                    if event.unicode.isalpha() and len(config.finish) < 3:
                        config.finish += event.unicode.upper()

                    if event.key == pygame.K_BACKSPACE:
                        config.finish = config.finish[:-1]

            if event.key == pygame.K_RETURN:
                if config.mode == 0:
                    save_point()
                elif config.mode == 1:
                    save_line()
                elif config.mode == 2:
                    breadth_first_search(config.start, config.finish)

                config.show_form = False
                reset_form()
                draw_form()
                remake_graph()
                draw_pos_box(mx, my)

            if event.key == pygame.K_TAB and (config.mode == 0 or config.mode == 2):
                config.input_pos = 1 if config.input_pos == 2 else 2
                draw_pos_box(1000, 1000)

            if event.key == pygame.K_ESCAPE:
                reset_form()
                remake_graph()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                draw_pos_box(mouse_x, mouse_y)

    draw_form()
    print_point_list()

    pygame.display.flip()

pygame.quit()

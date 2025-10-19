from styles import *
from elements import *
import config

import pygame

pygame.init()

screen.fill(WHITE)


def draw_form():
    pygame.draw.rect(screen, MEDIUM_GRAY, form)
    pygame.draw.rect(screen, BLACK, form, 1)

    if not config.show_form:
        screen.blit(
            TITLE.render("Click on Graph Box to draw!", True, BLACK),
            (form.left + 15, form.top + 10),
        )
        return

    elif config.mode == 0:
        draw_point_form()

    elif config.mode == 1:
        draw_line_form()

    elif config.mode >= 2:
        draw_search_form()


def draw_pos_box(mouse_x, mouse_y):
    msg = ""

    if (mouse_x, mouse_y) == (1000, 1000):
        if config.mode == 0:
            msg = "Enter point name" if config.input_pos == 1 else "Enter point value"
        elif config.mode == 1:
            if config.input_pos == 1:
                msg = "Enter start point"
            elif config.input_pos == 2:
                msg = "Enter end point"
            elif config.input_pos == 3:
                msg = "Enter line value"

        elif config.mode >= 2:
            msg = "Enter start point" if config.input_pos == 1 else "Enter finish point"

    elif graph_box.collidepoint(mouse_x, mouse_y):
        msg = f"Mouse position: {mouse_x}, {mouse_y}"

    else:
        msg = "Mouse position: Outside"

    pygame.draw.rect(screen, LIGHT_GRAY, pos_box)
    pygame.draw.rect(screen, BLACK, pos_box, 1)
    screen.blit(TEXT.render(msg, True, BLACK), (pos_box.left + 10, pos_box.top + 15))


def draw_algorithm_box():
    pygame.draw.rect(screen, LIGHT_GRAY, algorithm_box)

    screen.blit(
        TITLE.render("ALGORITHMS", True, BLACK),
        (algorithm_box.left + 3, algorithm_box.top + 5),
    )

    pygame.draw.line(
        screen,
        BLACK,
        (algorithm_box.right - 2, algorithm_box.top),
        (algorithm_box.right - 2, algorithm_box.bottom),
        1,
    )

    pygame.draw.rect(screen, WHITE, breadth_fs_btn)
    pygame.draw.rect(screen, BLACK, breadth_fs_btn, 1)
    screen.blit(
        TEXT.render("Breadth FS", True, BLACK),
        (breadth_fs_btn.left + 5, breadth_fs_btn.top + 5),
    )

    pygame.draw.rect(screen, WHITE, b_a_b_s_btn)
    pygame.draw.rect(screen, BLACK, b_a_b_s_btn, 1)
    screen.blit(
        TEXT.render("B&B Search", True, BLACK),
        (b_a_b_s_btn.left + 5, b_a_b_s_btn.top + 5),
    )

    pygame.draw.rect(screen, WHITE, hill_s_btn)
    pygame.draw.rect(screen, BLACK, hill_s_btn, 1)
    screen.blit(
        TEXT.render("Hill Climbing Search", True, BLACK),
        (hill_s_btn.left + 5, hill_s_btn.top + 5),
    )


def draw_graph_box():
    pygame.draw.rect(screen, WHITE, graph_box)

    label = pygame.Rect(graph_box.left - 2, graph_box.top - 2, 100, 30)
    pygame.draw.rect(screen, WHITE, label)
    pygame.draw.rect(screen, BLACK, label, 1)
    screen.blit(TEXT.render("Graph Box", True, BLACK), (label.left + 5, label.top + 5))

    mode_box = pygame.Rect(label.right + 5, graph_box.top - 2, 100, 30)
    pygame.draw.rect(screen, WHITE, mode_box)
    pygame.draw.rect(screen, BLACK, mode_box, 1)
    mode_TEXT = "Draw point" if config.mode == 0 else "Draw line"
    screen.blit(
        TEXT.render(mode_TEXT, True, BLACK),
        (mode_box.left + 5, mode_box.top + 5),
    )

    pygame.draw.rect(screen, WHITE, change_btn)
    pygame.draw.rect(screen, BLACK, change_btn, 1)
    screen.blit(
        TEXT.render("Change mode", True, BLACK),
        (change_btn.left + 5, change_btn.top + 5),
    )

    pygame.draw.rect(screen, WHITE, reset_btn)
    pygame.draw.rect(screen, BLACK, reset_btn, 1)
    screen.blit(
        TEXT.render("Reset", True, BLACK), (reset_btn.left + 5, reset_btn.top + 5)
    )

    pygame.draw.rect(screen, WHITE, clear_btn)
    pygame.draw.rect(screen, BLACK, clear_btn, 1)
    screen.blit(
        TEXT.render("Clear", True, BLACK), (clear_btn.left + 5, clear_btn.top + 5)
    )


def draw_point_list_box():
    pygame.draw.rect(screen, DARK_GRAY, point_list_box)
    pygame.draw.line(
        screen,
        BLACK,
        point_list_box.topleft,
        point_list_box.bottomleft,
        1,
    )
    screen.blit(
        TITLE.render("POINT LIST:", True, BLACK),
        (point_list_box.left + 5, point_list_box.top + 10),
    )


def draw_point_form():
    screen.blit(TITLE.render("Name:", True, BLACK), (form.left + 15, form.top + 10))
    screen.blit(
        TITLE.render("Value:", True, BLACK), (input_1.left + 115, form.top + 10)
    )

    draw_textbox(input_1, config.point_name)
    draw_textbox(input_2, config.point_value)

    if config.point_name.isalpha() and config.point_value.isdigit():
        pygame.draw.rect(screen, WHITE, submit_btn)
        pygame.draw.rect(screen, BLACK, submit_btn, 1)
        screen.blit(
            TEXT.render("Save", True, BLACK), (submit_btn.left + 15, submit_btn.top + 7)
        )
    else:
        pygame.draw.rect(screen, MEDIUM_GRAY, submit_btn)

    pygame.draw.rect(screen, WHITE, cancel_btn)
    pygame.draw.rect(screen, BLACK, cancel_btn, 1)
    screen.blit(
        TEXT.render("Cancel", True, BLACK), (cancel_btn.left + 5, cancel_btn.top + 7)
    )


def draw_line_form():
    if config.start_point:
        screen.blit(
            TITLE.render("Start:", True, BLACK), (form.left + 15, form.top + 10)
        )
        draw_textbox(input_1, config.start_point["Name"])

    if config.end_point:
        screen.blit(
            TITLE.render("End:", True, BLACK), (input_1.right + 15, form.top + 10)
        )
        draw_textbox(input_2, config.end_point["Name"])

    if config.start_point and config.end_point:
        screen.blit(
            TITLE.render("Value:", True, BLACK), (input_2.right + 15, form.top + 10)
        )
        draw_textbox(input_3, config.line_value)

    if config.start_point and config.end_point and config.line_value:
        pygame.draw.rect(screen, WHITE, submit_btn)
        pygame.draw.rect(screen, BLACK, submit_btn, 1)
        screen.blit(
            TEXT.render("Save", True, BLACK), (submit_btn.left + 15, submit_btn.top + 7)
        )
    else:
        pygame.draw.rect(screen, MEDIUM_GRAY, submit_btn)

    pygame.draw.rect(screen, WHITE, cancel_btn)
    pygame.draw.rect(screen, BLACK, cancel_btn, 1)
    screen.blit(
        TEXT.render("Cancel", True, BLACK), (cancel_btn.left + 5, cancel_btn.top + 7)
    )


def draw_search_form():
    screen.blit(TITLE.render("Start:", True, BLACK), (form.left + 15, form.top + 10))
    screen.blit(
        TITLE.render("Finish:", True, BLACK), (input_1.left + 115, form.top + 10)
    )

    draw_textbox(input_1, config.start)
    draw_textbox(input_2, config.finish)

    if config.start.isalpha() and config.finish.isalpha():
        pygame.draw.rect(screen, WHITE, submit_btn)
        pygame.draw.rect(screen, BLACK, submit_btn, 1)
        screen.blit(
            TEXT.render("Search", True, BLACK),
            (submit_btn.left + 5, submit_btn.top + 7),
        )
    else:
        pygame.draw.rect(screen, MEDIUM_GRAY, submit_btn)

    pygame.draw.rect(screen, WHITE, cancel_btn)
    pygame.draw.rect(screen, BLACK, cancel_btn, 1)
    screen.blit(
        TEXT.render("Cancel", True, BLACK), (cancel_btn.left + 5, cancel_btn.top + 7)
    )


def draw_result_box():
    pygame.draw.rect(screen, WHITE, result_box)

    label = pygame.Rect(result_box.left - 2, result_box.top, 100, 30)
    pygame.draw.rect(screen, WHITE, label)
    pygame.draw.rect(screen, BLACK, label, 1)
    screen.blit(TEXT.render("Result", True, BLACK), (label.left + 5, label.top + 5))

    pygame.draw.line(
        screen,
        BLACK,
        result_box.topleft,
        result_box.topright,
        1,
    )

    # mode_box = pygame.Rect(label.right + 5, graph_box.top - 2, 100, 30)
    # pygame.draw.rect(screen, WHITE, mode_box)
    # pygame.draw.rect(screen, BLACK, mode_box, 1)
    # mode_TEXT = "Draw point" if config.mode == 0 else "Draw line"
    # screen.blit(
    #     TEXT.render(mode_TEXT, True, BLACK),
    #     (mode_box.left + 5, mode_box.top + 5),
    # )

    # pygame.draw.rect(screen, WHITE, change_btn)
    # pygame.draw.rect(screen, BLACK, change_btn, 1)
    # screen.blit(
    #     TEXT.render("Change mode", True, BLACK),
    #     (change_btn.left + 5, change_btn.top + 5),
    # )

    # pygame.draw.rect(screen, WHITE, reset_btn)
    # pygame.draw.rect(screen, BLACK, reset_btn, 1)
    # screen.blit(
    #     TEXT.render("Reset", True, BLACK), (reset_btn.left + 5, reset_btn.top + 5)
    # )

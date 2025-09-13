from styles import *
from elements import *
from draws import *
from features import *


def remake_graph():
    draw_graph_box()

    for p in config.point_list:
        mark_point(p["Name"], p["Position"], p["Value"])

    for l in config.line_list:
        draw_line(l["Start"]["Position"], l["End"]["Position"])


def reset_form():
    config.point_name = ""
    config.point_value = ""
    config.input_pos = 0
    config.show_form = False
    config.start_point = {}
    config.end_point = {}


def save_point():

    if config.point_name.isalpha() and config.point_value.isdigit():
        config.point_list.append(
            {
                "Name": config.point_name,
                "Position": config.current_point,
                "Value": config.point_value,
            }
        )
        mark_point(config.point_name, config.current_point, config.point_value)
        reset_form()


def save_line():
    if config.start_point != {} and config.end_point != {}:
        draw_line(config.start_point["Position"], config.end_point["Position"])
        config.line_list.append({"Start": config.start_point, "End": config.end_point})
        reset_form()
        remake_graph()


def find_point(x, y):
    for point in config.point_list:
        px, py = point["Position"]
        if px - 10 <= x <= px + 10 and py - 10 <= y <= py + 10:
            return (px, py)

    return ()

    # global start_point, end_point, input_pos

    # draw_form()

    # for point in point_list:
    #     px, py = point["Position"]
    #     if px - 10 <= x <= px + 10 and py - 10 <= y <= py + 10:
    #         if start_point == {}:
    #             input_pos = 1
    #             pygame.draw.circle(screen, YELLOW, point["Position"], 10)
    #             pygame.draw.circle(screen, BLACK, point["Position"], 10, 1)
    #             start_point = point

    #         else:
    #             input_pos = 2
    #             pygame.draw.circle(screen, BLUE, point["Position"], 10)
    #             pygame.draw.circle(screen, BLACK, point["Position"], 10, 1)
    #             end_point = point

    #         draw_line_form()


def print_point_list():
    draw_point_list_box()

    y_offset = 40
    for p in config.point_list:
        result = f"{p['Name']}{p['Value']}"
        screen.blit(
            TEXT.render(result, True, BLACK),
            (point_list_box.left + 10, point_list_box.top + y_offset),
        )
        y_offset += 20


def mark_point(name, pos, value):
    pygame.draw.circle(screen, RED, pos, 10)
    screen.blit(TEXT.render(name + value, True, BLACK), (pos[0] - 5, pos[1] - 30))


def draw_line(start, end):
    pygame.draw.line(
        screen,
        BLACK,
        start,
        end,
        1,
    )

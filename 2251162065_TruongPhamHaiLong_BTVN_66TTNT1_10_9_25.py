import pygame

pygame.init()

WHITE, LIGHT_GRAY, MEDIUM_GRAY, DARK_GRAY, BLACK, RED, YELLOW, BLUE = (
    (255, 255, 255),
    (230, 230, 230),
    (200, 200, 200),
    (170, 170, 170),
    (0, 0, 0),
    (255, 0, 0),
    (255, 255, 0),
    (0, 0, 255),
)

title = pygame.font.Font(None, 40)
text = pygame.font.Font(None, 25)

pygame.display.set_caption("Vẽ đồ thị")
screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)

form = pygame.Rect(-1, -1, 583, 50)

pos_box = pygame.Rect(581, -1, 220, 50)
point_list_box = pygame.Rect(581, 49, 220, 551)
graph_box = pygame.Rect(1, 50, 580, 549)

input_1 = pygame.Rect(form.left + 105, form.top + 9, 100, 30)
input_2 = pygame.Rect(input_1.right + 110, form.top + 9, 100, 30)

cancel_btn = pygame.Rect(form.right - 75, input_2.top, 70, 30)
submit_btn = pygame.Rect(cancel_btn.left - 75, input_2.top, 70, 30)
reset_btn = pygame.Rect(graph_box.right - 59, graph_box.top - 2, 60, 30)
change_btn = pygame.Rect(reset_btn.left - 129, graph_box.top - 2, 125, 30)


show_form, point_list, line_list = False, [], []
point_name, point_value, input_pos, mode, current_point = "", "", 0, 0, ()
start_point, end_point = {}, {}


def reset_form():
    global point_name, point_value, input_pos, show_form, start_point, end_point

    point_name, point_value, input_pos, show_form = "", "", 0, False

    start_point, end_point = {}, {}


def save_point():
    global point_name, point_value, show_form, input_pos, start_point, end_point

    if point_name.isalpha() and point_value.isdigit():
        point_list.append(
            {"Name": point_name, "Position": current_point, "Value": point_value}
        )
        mark_point(point_name, current_point, point_value)
        reset_form()


def save_line():
    draw_line(start_point["Position"], end_point["Position"])
    line_list.append({"Start": start_point, "End": end_point})
    reset_form()
    remake_graph()


def find_point(x, y):
    global start_point, end_point, input_pos

    draw_form()

    for point in point_list:
        px, py = point["Position"]
        if px - 10 <= x <= px + 10 and py - 10 <= y <= py + 10:
            if start_point == {}:
                input_pos = 1
                pygame.draw.circle(screen, YELLOW, point["Position"], 10)
                pygame.draw.circle(screen, BLACK, point["Position"], 10, 1)
                start_point = point

            else:
                input_pos = 2
                pygame.draw.circle(screen, BLUE, point["Position"], 10)
                pygame.draw.circle(screen, BLACK, point["Position"], 10, 1)
                end_point = point

            draw_line_form()


def draw_pos_box(mouse_x, mouse_y):
    if (mouse_x, mouse_y) == (1000, 1000):
        if mode == 0:
            msg = "Enter point name" if input_pos == 1 else "Enter point value"

        if mode == 1:
            msg = "Enter start point" if input_pos == 1 else "Enter end point"

    elif graph_box.collidepoint(mouse_x, mouse_y):
        msg = f"Mouse position: {mouse_x}, {mouse_y}"

    else:
        msg = "Mouse position: Outside"

    pygame.draw.rect(screen, LIGHT_GRAY, pos_box)
    pygame.draw.rect(screen, BLACK, pos_box, 1)
    screen.blit(text.render(msg, True, BLACK), (pos_box.left + 10, pos_box.top + 15))


def draw_point_list_box():
    pygame.draw.rect(screen, DARK_GRAY, point_list_box)
    pygame.draw.line(
        screen,
        BLACK,
        point_list_box.topleft,
        (point_list_box.left, point_list_box.bottom),
        1,
    )
    screen.blit(
        title.render("POINT LIST:", True, BLACK),
        (point_list_box.left + 5, point_list_box.top + 10),
    )


def print_point_list():
    draw_point_list_box()

    y_offset = 40
    for p in point_list:
        result = f"{p['Name']}{p['Value']}"
        screen.blit(
            text.render(result, True, BLACK),
            (point_list_box.left + 10, point_list_box.top + y_offset),
        )
        y_offset += 20


def draw_textbox(rect, content):
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)
    screen.blit(text.render(content, True, BLACK), (rect.left + 10, rect.top + 7))


def draw_form():
    pygame.draw.rect(screen, MEDIUM_GRAY, form)
    pygame.draw.rect(screen, BLACK, form, 1)

    if not show_form:
        screen.blit(
            title.render("Click on Graph Box to draw!", True, BLACK),
            (form.left + 15, form.top + 10),
        )
        return

    elif show_form and mode == 0:
        draw_point_form()

    elif show_form and mode == 1:
        draw_line_form()


def draw_point_form():
    screen.blit(title.render("Name:", True, BLACK), (form.left + 15, form.top + 10))
    screen.blit(
        title.render("Value:", True, BLACK), (input_1.left + 115, form.top + 10)
    )
    draw_textbox(input_1, point_name)
    draw_textbox(input_2, point_value)

    if point_name.isalpha() and point_value.isdigit():
        pygame.draw.rect(screen, WHITE, submit_btn)
        pygame.draw.rect(screen, BLACK, submit_btn, 1)
        screen.blit(
            text.render("Save", True, BLACK), (submit_btn.left + 15, submit_btn.top + 7)
        )
    else:
        pygame.draw.rect(screen, MEDIUM_GRAY, submit_btn)

    pygame.draw.rect(screen, WHITE, cancel_btn)
    pygame.draw.rect(screen, BLACK, cancel_btn, 1)
    screen.blit(
        text.render("Cancel", True, BLACK), (cancel_btn.left + 5, cancel_btn.top + 7)
    )


def draw_line_form():
    screen.blit(title.render("Start:", True, BLACK), (form.left + 15, form.top + 10))
    screen.blit(title.render("End:", True, BLACK), (input_1.left + 115, form.top + 10))

    if start_point != {}:
        draw_textbox(input_1, start_point["Name"])

    if end_point != {}:
        draw_textbox(input_2, end_point["Name"])

    if start_point != {} and end_point != {}:
        pygame.draw.rect(screen, WHITE, submit_btn)
        pygame.draw.rect(screen, BLACK, submit_btn, 1)
        screen.blit(
            text.render("Save", True, BLACK), (submit_btn.left + 15, submit_btn.top + 7)
        )

    else:
        pygame.draw.rect(screen, MEDIUM_GRAY, submit_btn)

    pygame.draw.rect(screen, WHITE, cancel_btn)
    pygame.draw.rect(screen, BLACK, cancel_btn, 1)
    screen.blit(
        text.render("Cancel", True, BLACK), (cancel_btn.left + 5, cancel_btn.top + 7)
    )


def draw_graph_box():
    pygame.draw.rect(screen, WHITE, graph_box)

    label = pygame.Rect(graph_box.left - 2, graph_box.top - 2, 100, 30)
    pygame.draw.rect(screen, WHITE, label)
    pygame.draw.rect(screen, BLACK, label, 1)
    screen.blit(text.render("Graph Box", True, BLACK), (label.left + 5, label.top + 5))

    mode_box = pygame.Rect(label.right + 5, graph_box.top - 2, 100, 30)
    pygame.draw.rect(screen, WHITE, mode_box)
    pygame.draw.rect(screen, BLACK, mode_box, 1)
    mode_text = "Draw point" if mode == 0 else "Draw line"
    screen.blit(
        text.render(mode_text, True, BLACK),
        (mode_box.left + 5, mode_box.top + 5),
    )

    pygame.draw.rect(screen, WHITE, change_btn)
    pygame.draw.rect(screen, BLACK, change_btn, 1)
    screen.blit(
        text.render("Change mode", True, BLACK),
        (change_btn.left + 5, change_btn.top + 5),
    )

    pygame.draw.rect(screen, WHITE, reset_btn)
    pygame.draw.rect(screen, BLACK, reset_btn, 1)
    screen.blit(
        text.render("Reset", True, BLACK), (reset_btn.left + 5, reset_btn.top + 5)
    )


def mark_point(name, pos, value):
    pygame.draw.circle(screen, RED, pos, 10)
    screen.blit(text.render(name + value, True, BLACK), (pos[0] - 5, pos[1] - 30))


def draw_line(start, end):
    pygame.draw.line(
        screen,
        BLACK,
        start,
        end,
        1,
    )


def remake_graph():
    draw_graph_box()

    for p in point_list:
        mark_point(p["Name"], p["Position"], p["Value"])

    for l in line_list:
        draw_line(l["Start"]["Position"], l["End"]["Position"])


draw_form()
draw_pos_box(0, 0)
draw_point_list_box()
draw_graph_box()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION and input_pos == 0:
            draw_pos_box(mouse_x, mouse_y)

        if event.type == pygame.MOUSEBUTTONDOWN:

            if reset_btn.collidepoint(mouse_x, mouse_y):
                point_list.clear()
                line_list.clear()
                reset_form()
                remake_graph()

            elif change_btn.collidepoint(mouse_x, mouse_y):
                mode = 1 if mode == 0 else 0
                reset_form()
                remake_graph()

            elif (
                not show_form and graph_box.collidepoint(mouse_x, mouse_y) and mode == 0
            ):
                show_form, input_pos = True, 1
                current_point = (mouse_x, mouse_y)
                pygame.draw.circle(screen, RED, current_point, 10)
                draw_pos_box(1000, 1000)

            elif (
                mode == 1
                and (start_point == {} or end_point == {})
                and len(point_list) > 0
            ):
                find_point(mouse_x, mouse_y)
                draw_pos_box(1000, 1000)
                show_form = True
                draw_form()

            elif show_form:
                if input_1.collidepoint(mouse_x, mouse_y):
                    input_pos = 1
                    draw_pos_box(1000, 1000)

                if input_2.collidepoint(mouse_x, mouse_y):
                    input_pos = 2
                    draw_pos_box(1000, 1000)

                if cancel_btn.collidepoint(mouse_x, mouse_y):
                    reset_form()
                    remake_graph()
                    draw_pos_box(mouse_x, mouse_y)

                if submit_btn.collidepoint(mouse_x, mouse_y):
                    if mode == 0:
                        save_point()
                    elif mode == 1:
                        save_line()

        if event.type == pygame.KEYDOWN and show_form:
            if input_pos == 1:
                if event.unicode.isalpha() and len(point_name) < 3:
                    point_name += event.unicode.upper()

                if event.key == pygame.K_BACKSPACE:
                    point_name = point_name[:-1]

            elif input_pos == 2:
                if event.unicode.isdigit() and len(point_value) < 5:
                    point_value += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    point_value = point_value[:-1]

            if event.key == pygame.K_RETURN:
                if mode == 0:
                    save_point()
                elif mode == 1:
                    save_line()

            if event.key == pygame.K_TAB:
                input_pos = 1 if input_pos == 2 else 2
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

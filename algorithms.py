import config
from features import *


def find_route(start, finish, history):
    route = [finish["Name"]]
    current = finish

    while current["Name"] != start["Name"]:
        for name in history:
            p = get_point(name)
            if current["Name"] in p["Neighbor"]:
                current = p
                route.insert(0, current["Name"])
                break
    return route


def breadth_first_search(start, finish):
    print("\nBREADTH FIRST SEARCH")

    if start == finish:
        return print_result("Error")

    start_p, finish_p = get_point(start), get_point(finish)

    if not start_p or not finish_p:
        return print_result("Error")

    print(f"START: {start_p['Name']}")
    print(f"FINISH: {finish_p['Name']}\n")

    open_list, history = [start_p], []
    step = 1

    while open_list:
        print(f"INDEX: {step}")
        current = open_list.pop(0)
        history.append(current["Name"])

        print(f"Current: {current}")
        print(f"OPEN: {open_list}")

        if current["Name"] == finish_p["Name"]:
            print("Search success")
            break

        for n in current["Neighbor"]:
            next_p = get_point(n)
            if next_p:
                open_list.append(next_p)

        step += 1
        print()

    else:
        return print_result("Search failed")

    route = find_route(start_p, finish_p, history)
    result = f"HISTORY: {history}; ROUTE: {' -> '.join(route)}"

    print(result)
    print_result(result)

    print_point_list()
    reset_form()
    remake_graph()

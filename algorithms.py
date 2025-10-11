import config
import copy
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


def bab_find_route(start, finish, history):
    route = [finish["Name"]]
    current = finish

    while current["Name"] != start["Name"]:
        route.insert(0, current["Parent"])
        current = get_point(current["Parent"])
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


def branch_and_bound(start, finish):
    print("\nBRANCH AND BOUND SEARCH")

    if start == finish:
        return print_result("Error")

    start_p, finish_p = get_point(start), get_point(finish)

    if not start_p or not finish_p:
        return print_result("Error")

    print(f"START: {start_p['Name']}")
    print(f"FINISH: {finish_p['Name']}\n")

    start_p["G"] = 0
    open_list, history, routes = [start_p], [], []
    step, min = 1, -1

    while open_list:
        print(f"INDEX: {step}")
        current = open_list.pop(0)
        history.append(current["Name"])
        print("MIN: " + str(min))

        L_list = []

        print(f"Current: {current}")
        # print(f"L:")
        # for p in L_list:
        #     print(p)
        print(f"OPEN:")
        for p in open_list:
            print(p)
        print(f"HISTORY: {history}")

        if current["Name"] == finish_p["Name"]:
            min = current["G"]
            print("Search success")
            print(f"New MIN: {min}")

        if min != -1 and current["F"] > min:
            print(f"\nRemove {current["Name"]} from OPEN\n")

        else:
            for n in current["Neighbor"]:
                next_p = get_point(n)

                if next_p and (
                    next_p["Name"] == finish_p["Name"]
                    or next_p["Name"] != start_p["Name"]
                ):
                    g_new = get_line_value(current["Name"], next_p["Name"])

                    if next_p not in open_list:
                        next_p["Parent"] = current["Name"]
                        next_p["G"] = int(current["G"]) + g_new
                        next_p["F"] = int(next_p["G"]) + next_p["Value"]
                        L_list.append(next_p)

                    else:
                        tmp = copy.deepcopy(next_p)

                        tmp["G"] = int(current["G"] + g_new)
                        tmp["F"] = int(tmp["G"]) + tmp["Value"]

                        print(f"OLD: {next_p}")
                        print(f"NEW: {tmp}")

                        if tmp["F"] <= next_p["F"]:
                            open_list.remove(next_p)
                            tmp["Parent"] = current["Name"]
                            L_list.append(tmp)

            L_list.sort(key=lambda d: d["F"])

            print(f"\nL:")
            for p in L_list:
                print(p)
            open_list = L_list + open_list

        print(f"OPEN:")
        for p in open_list:
            print(p)

        print("MIN: " + str(min))
        step += 1

        print()
    else:
        print("\nDone")

    route = bab_find_route(start_p, finish_p, history)
    result = f"HISTORY: {history}; ROUTE: {' -> '.join(route)}; MIN: {min}"

    print(result)
    print_result(result)

    print_point_list()
    reset_form()
    remake_graph()


def branch_and_bound_nhap(start, finish):

    # config.point_list = [
    #     {"Name": "A", "Position": (504, 137), "Value": 0, "Neighbor": ["D", "F"]},
    #     {"Name": "D", "Position": (401, 249), "Value": 0, "Neighbor": ["H", "E"]},
    #     {"Name": "H", "Position": (330, 358), "Value": 0, "Neighbor": ["C", "K"]},
    #     {"Name": "C", "Position": (261, 210), "Value": 0, "Neighbor": []},
    #     {
    #         "Name": "E",
    #         "Position": (567, 251),
    #         "Value": 0,
    #         "Neighbor": ["A", "K", "I"],
    #     },
    #     {"Name": "F", "Position": (682, 155), "Value": 0, "Neighbor": ["G", "E"]},
    #     {"Name": "G", "Position": (850, 146), "Value": 0, "Neighbor": []},
    #     {
    #         "Name": "I",
    #         "Position": (702, 357),
    #         "Value": 0,
    #         "Neighbor": ["K", "F", "B"],
    #     },
    #     {"Name": "K", "Position": (530, 362), "Value": 0, "Neighbor": ["B"]},
    #     {"Name": "B", "Position": (613, 459), "Value": 0, "Neighbor": []},
    # ]

    # config.line_list = [
    #     {"Start": "A", "End": "D", "Value": 7},
    #     {"Start": "D", "End": "H", "Value": 8},
    #     {"Start": "H", "End": "C", "Value": 3},
    #     {"Start": "A", "End": "F", "Value": 20},
    #     {"Start": "F", "End": "G", "Value": 4},
    #     {"Start": "F", "End": "E", "Value": 2},
    #     {"Start": "E", "End": "A", "Value": 13},
    #     {"Start": "D", "End": "E", "Value": 4},
    #     {"Start": "E", "End": "K", "Value": 4},
    #     {"Start": "H", "End": "K", "Value": 2},
    #     {"Start": "I", "End": "K", "Value": 9},
    #     {"Start": "I", "End": "F", "Value": 6},
    #     {"Start": "E", "End": "I", "Value": 3},
    #     {"Start": "I", "End": "B", "Value": 5},
    #     {"Start": "K", "End": "B", "Value": 2},
    # ]

    if start == finish:
        return print_result("Error")

    start_p, finish_p = get_point(start), get_point(finish)

    if not start_p or not finish_p:
        return print_result("Error")

    print(f"START: {start_p['Name']}")
    print(f"FINISH: {finish_p['Name']}\n")

    start_p["G"] = 0
    open_list, history, routes = [start_p], [], []
    step, min = 1, -1

    while open_list:
        print(f"INDEX: {step}")
        current = open_list.pop(0)
        history.append(current["Name"])
        print("MIN: " + str(min))

        L_list = []

        print(f"Current: {current}")
        print(f"L:")
        for p in L_list:
            print(p)
        print(f"OPEN:")
        for p in open_list:
            print(p)
        print(f"HISTORY: {history}")

        if current["Name"] == finish_p["Name"]:
            min = current["G"]
            print("Search success")
            print(f"New MIN: {min}")

        if min != -1 and current["F"] > min:
            print(f"\nRemove {current["Name"]} from OPEN\n")

        else:
            for n in current["Neighbor"]:
                next_p = get_point(n)

                if next_p and (
                    next_p["Name"] == finish_p["Name"] or next_p["Name"] not in history
                ):
                    g_new = get_line_value(current["Name"], next_p["Name"])

                    if next_p not in open_list:
                        next_p["Parent"] = current["Name"]
                        next_p["G"] = int(current["G"]) + g_new
                        next_p["F"] = int(next_p["G"]) + next_p["Value"]
                        L_list.append(next_p)

                    else:
                        tmp = copy.deepcopy(next_p)

                        tmp["G"] = int(current["G"] + g_new)
                        tmp["F"] = int(tmp["G"]) + tmp["Value"]

                        print(f"OLD: {next_p}")
                        print(f"NEW: {tmp}")

                        if tmp["F"] <= next_p["F"]:
                            open_list.remove(next_p)
                            tmp["Parent"] = current["Name"]
                            L_list.append(tmp)

            L_list.sort(key=lambda d: d["F"])

            print(f"\nL:")
            for p in L_list:
                print(p)
            open_list = L_list + open_list

        print(f"OPEN:")
        for p in open_list:
            print(p)

        print("MIN: " + str(min))
        step += 1

        print()
    else:
        print("\nDone")

    route = bab_find_route(start_p, finish_p, history)
    result = f"HISTORY: {history}; ROUTE: {' -> '.join(route)}; MIN: {min}"

    print(result)
    print_result(result)


branch_and_bound_nhap("A", "B")

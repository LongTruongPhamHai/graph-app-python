show_form, point_list, line_list = False, [], []
point_name, point_value, input_pos, mode, current_point, line_value = (
    "",
    "",
    0,
    0,
    None,
    "",
)
start_point, end_point = None, None
start, finish = "", ""

# point_list = [
#     {"Name": "A", "Position": (376, 130), "Value": 14, "Neighbor": ["D", "F"]},
#     {"Name": "F", "Position": (583, 172), "Value": 7, "Neighbor": ["G", "E"]},
#     {"Name": "G", "Position": (795, 199), "Value": 12, "Neighbor": []},
#     {"Name": "D", "Position": (322, 251), "Value": 6, "Neighbor": ["H", "E"]},
#     {"Name": "H", "Position": (307, 384), "Value": 10, "Neighbor": ["C", "K"]},
#     {"Name": "C", "Position": (238, 295), "Value": 15, "Neighbor": []},
#     {"Name": "E", "Position": (481, 265), "Value": 8, "Neighbor": ["A", "K", "I"]},
#     {"Name": "K", "Position": (483, 399), "Value": 2, "Neighbor": ["B"]},
#     {"Name": "I", "Position": (696, 387), "Value": 4, "Neighbor": ["K", "F", "B"]},
#     {"Name": "B", "Position": (603, 484), "Value": 0, "Neighbor": []},
# ]

# line_list = [
#     {"Start": "A", "End": "D", "Value": 7},
#     {"Start": "D", "End": "H", "Value": 8},
#     {"Start": "H", "End": "C", "Value": 6},
#     {"Start": "D", "End": "E", "Value": 4},
#     {"Start": "E", "End": "A", "Value": 13},
#     {"Start": "A", "End": "F", "Value": 20},
#     {"Start": "F", "End": "G", "Value": 4},
#     {"Start": "F", "End": "E", "Value": 9},
#     {"Start": "E", "End": "I", "Value": 3},
#     {"Start": "I", "End": "F", "Value": 6},
#     {"Start": "I", "End": "B", "Value": 5},
#     {"Start": "I", "End": "K", "Value": 9},
#     {"Start": "H", "End": "K", "Value": 5},
#     {"Start": "K", "End": "B", "Value": 6},
#     {"Start": "E", "End": "K", "Value": 4},
# ]

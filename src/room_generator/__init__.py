from collections import deque
import random
from typing import Optional


def build_room(name: str) -> dict:
    return {
        'room': name,
    }


def build_rooms(room_names: deque, rooms: list):
    if len(room_names) <= 0:
        return rooms
    else:
        next_room = room_names.popleft()
        rooms.append(build_room(next_room))
        return build_rooms(room_names, rooms)


def add_things_to_rooms(rooms: list, things: list) -> list:
    if len(rooms) > 0:
        for i in range(0, len(rooms)):
            if i < len(things):
                if isinstance(things[i], list):
                    rooms[i]['things'] = things[i]
                elif isinstance(things[i], str):
                    rooms[i]['things'] = [things[i]]
                else:
                    rooms[i]['things'] = []
            else:
                rooms[i]['things'] = []
    return rooms


def connect_rooms(rooms: list) -> list:
    n_rooms = len(rooms)
    if n_rooms > 0:
        for i in range(0, n_rooms):
            j = (2 * i) + 1
            rooms[i]['exits'] = []
            if j < n_rooms:
                rooms[i]['exits'].append({'south': rooms[j]['room']})
            if (j + 1) < n_rooms:
                rooms[i]['exits'].append({'east': rooms[j + 1]['room']})
    return rooms


def generate(room_names: list[str], thing_names: list) -> list:
    if len(room_names) <= 0:
        return []
    else:
        room_names_queue = deque(room_names)
        rooms = build_rooms(room_names_queue, [])
    rooms_with_things = add_things_to_rooms(rooms, thing_names)
    connected_rooms = connect_rooms(rooms_with_things)
    return connected_rooms


def room_to_inform7(room):
    code = [f'\n{room["room"]} is a room.']
    if room['things'] is not None:
        for thing in room['things']:
            code.append(f'{thing} is a thing in {room["room"]}.')
    if room['exits'] is not None:
        for x in room['exits']:
            for _, (key, value) in enumerate(x.items()):
                code.append(f'{value} is {key} of {room["room"]}.')
    return str('\n').join(code)


def to_inform7(rooms: list) -> str:
    accumulator = [
        '['
        + '\n  Generated rooms'
        + '\n  Jim Tyhurst'
        + '\n  Generator code: https://github.com/jimtyhurst/room-generator'
        '\n]'
    ]
    for room in rooms:
        accumulator.append(room_to_inform7(room))
    return '\n'.join(accumulator)


def find_room(room_name: str, rooms: list) -> Optional[dict]:
    the_room = None
    index = 0
    while the_room is None and index < len(rooms):
        if room_name == rooms[index]['room']:
            the_room = rooms[index]
        index += 1
    return the_room


def testable_path(rooms: list) -> list:
    accumulator = []
    if len(rooms) > 0:
        room_name = rooms[0]['room']
        while room_name is not None:
            room = find_room(room_name, rooms)
            if room is None:
                room_name = None
            else:
                if room['exits'] is None:
                    room_name = None
                else:
                    qty_exits = len(room['exits'])
                    if qty_exits < 1:
                        room_name = None
                    else:
                        exit_index = random.randint(0, qty_exits - 1)
                        direction = list(
                            enumerate(room['exits'][exit_index].keys())
                        )[0][1]
                        room_name = list(
                            enumerate(room['exits'][exit_index].values())
                        )[0][1]
                        accumulator.append(direction)
    return accumulator


def path_to_inform7(path: list[str]) -> str:
    return '[Generated test]\nTest path with ' + '"' + ' / '.join(path) + '"'

from collections import deque


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
            rooms[i]['exits'] = []
            if (i + 1) < n_rooms:
                rooms[i]['exits'].append({'sw': rooms[i + 1]['room']})
            if (i + 2) < n_rooms:
                rooms[i]['exits'].append({'se': rooms[i + 2]['room']})
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

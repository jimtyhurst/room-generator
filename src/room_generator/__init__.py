from collections import deque


def build_room(name: str) -> dict:
    return {
        'room': name,
    }


def build_rooms(room_names, rooms):
    if len(room_names) <= 0:
        return rooms
    else:
        next_room = room_names.popleft()
        rooms.append(build_room(next_room))
        return build_rooms(room_names, rooms)


def add_things_to_rooms(rooms, things):
    if len(rooms) > 0:
        for i in range(0, len(rooms)):
            if i < len(things):
                rooms[i]['things'] = [things[i]]
            else:
                rooms[i]['things'] = []
    return rooms


def generate(room_names, thing_names):
    if len(room_names) <= 0:
        return []
    else:
        names_queue = deque(room_names)
        rooms = build_rooms(names_queue, [])
    rooms = add_things_to_rooms(rooms, thing_names)
    return rooms

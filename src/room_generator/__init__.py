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


def generate(room_names):
    if len(room_names) <= 0:
        return []
    else:
        names_queue = deque(room_names)
        return build_rooms(names_queue, [])

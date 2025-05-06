import room_generator

ROOM_NAMES = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
THINGS = ['cat', 'dog', 'key', 'painting', 'phone']


def test_generate_empty_list():
    assert room_generator.generate([], []) == []


def test_generate_1_room():
    assert room_generator.generate(['Portland'], []) == [
        {'room': 'Portland', 'things': []},
    ]


def test_generate_2_rooms():
    assert room_generator.generate(['Portland', 'Corvallis'], []) == [
        {'room': 'Portland', 'things': []},
        {'room': 'Corvallis', 'things': []},
    ]


def test_generate_rooms_with_things():
    assert room_generator.generate(ROOM_NAMES, THINGS) == [
        {'room': 'New York City', 'things': ['cat']},
        {'room': 'Los Angeles', 'things': ['dog']},
        {'room': 'Chicago', 'things': ['key']},
        {'room': 'Houston', 'things': ['painting']},
        {'room': 'Phoenix', 'things': ['phone']},
    ]


def test_1_item_add_things_to_rooms():
    expected_room = 'kitchen'
    expected_thing = 'kitchen table'
    expected_rooms = [room_generator.build_room(expected_room)]
    expected_things = [expected_thing]
    rooms_with_things = room_generator.add_things_to_rooms(
        expected_rooms, expected_things
    )
    assert rooms_with_things == [
        {'room': expected_room, 'things': [expected_thing]}
    ]


def test_2_rooms_add_things_to_rooms():
    expected_room_1 = 'kitchen'
    expected_thing_1 = 'kitchen table'
    expected_room_2 = 'living room'
    expected_thing_2 = 'book'
    expected_rooms = [
        room_generator.build_room(expected_room_1),
        room_generator.build_room(expected_room_2),
    ]
    expected_things = [expected_thing_1, expected_thing_2]
    rooms_with_things = room_generator.add_things_to_rooms(
        expected_rooms, expected_things
    )
    assert rooms_with_things == [
        {'room': expected_room_1, 'things': [expected_thing_1]},
        {'room': expected_room_2, 'things': [expected_thing_2]},
    ]

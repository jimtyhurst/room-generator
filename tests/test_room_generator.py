import room_generator

ROOM_NAMES = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
THING_NAMES = ['cat', 'dog', ['key', 'lockbox'], 'painting', 'phone']


def test_generate_empty_list():
    assert room_generator.generate([], ['paintbrush']) == []


def test_generate_1_room():
    assert room_generator.generate(['Portland'], []) == [
        {'room': 'Portland', 'things': [], 'exits': []},
    ]


def test_generate_2_rooms():
    assert room_generator.generate(['Portland', 'Corvallis'], []) == [
        {
            'room': 'Portland',
            'things': [],
            'exits': [{'south': 'Corvallis'}],
        },
        {'room': 'Corvallis', 'things': [], 'exits': []},
    ]


def test_generate_multiple_rooms():
    rooms = room_generator.generate(ROOM_NAMES, THING_NAMES)
    assert len(rooms) == 5
    assert rooms[0] == {
        'room': ROOM_NAMES[0],
        'things': [THING_NAMES[0]],
        'exits': [{'south': ROOM_NAMES[1]}, {'east': ROOM_NAMES[2]}],
    }
    assert rooms[1] == {
        'room': ROOM_NAMES[1],
        'things': [THING_NAMES[1]],
        'exits': [{'south': ROOM_NAMES[3]}, {'east': ROOM_NAMES[4]}],
    }
    assert rooms[4] == {
        'room': ROOM_NAMES[4],
        'things': [THING_NAMES[4]],
        'exits': [],
    }


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


def test_to_inform7_empty_list():
    code = room_generator.to_inform7([])
    assert code == '[Generated rooms]'


def test_to_inform7_one_room():
    code = room_generator.to_inform7(
        room_generator.generate(ROOM_NAMES[2:3], THING_NAMES[2:3])
    )
    assert (
        code
        == '[Generated rooms]\n'
        + '\nChicago is a room.'
        + '\nkey is a thing in Chicago.'
        + '\nlockbox is a thing in Chicago.'
    )


def test_to_inform7_two_rooms_with_room_connections():
    code = room_generator.to_inform7(
        room_generator.generate(ROOM_NAMES[2:4], THING_NAMES[2:4])
    )
    assert (
        code
        == '[Generated rooms]\n'
        + '\nChicago is a room.'
        + '\nkey is a thing in Chicago.'
        + '\nlockbox is a thing in Chicago.'
        + '\nHouston is south of Chicago.'
        + '\n\nHouston is a room.'
        + '\npainting is a thing in Houston.'
    )


def test_testable_path_empty_list():
    path = room_generator.testable_path([])
    assert path == []


def test_testable_path_one_room():
    path = room_generator.testable_path(
        [{'room': 'Houston', 'things': ['painting'], 'exits': []}]
    )
    assert path == []


def test_testable_path_two_rooms():
    path = room_generator.testable_path(
        [
            {
                'room': 'Chicago',
                'things': ['key', 'lockbox'],
                'exits': [{'east': 'New York City'}],
            },
            {'room': 'New York City', 'things': ['cat'], 'exits': []},
        ]
    )
    assert path == ['east']

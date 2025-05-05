import room_generator

ROOM_NAMES = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# THINGS = ["cat", "dog", "key", "painting", "phone"]


def test_generate_empty_list():
    assert room_generator.generate([]) == []


def test_generate_1_room():
    assert room_generator.generate(["Portland"]) == [
        {"room": "Portland"},
    ]


def test_generate_2_rooms():
    assert room_generator.generate(["Portland", "Corvallis"]) == [
        {"room": "Portland"},
        {"room": "Corvallis"},
    ]


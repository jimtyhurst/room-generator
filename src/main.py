import room_generator


ROOM_NAMES = [
    'Entry Hall',
    'Living Room',
    'Family Room',
    'Dining Room',
    'Kitchen',
    'Master Bedroom',
    'Master Bathroom',
    'Childs Bedroom',
    'Hall Bathroom',
    'Home Office',
]
THING_NAMES = [
    'a coat rack',
    ['a cat', 'a sofa', 'some lamps'],
    'a dog',
    ['a dining table'],
    ['a kitchen table', 'a wok'],
    ['a kingsize bed', 'a dresser'],
    ['a razor', 'a hair brush'],
    ['a painting', 'a phone'],
    'a hand towel',
    ['a key', 'a lockbox'],
]


def generate(room_names, thing_names):
    rooms = room_generator.generate(ROOM_NAMES, THING_NAMES)
    code_snippet = room_generator.to_inform7(rooms)
    return code_snippet


if __name__ == '__main__':
    print(generate(ROOM_NAMES, THING_NAMES))

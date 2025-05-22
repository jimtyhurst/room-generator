import room_generator


ROOM_NAMES = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
THING_NAMES = ['cat', 'dog', ['key', 'lockbox'], 'painting', 'phone']


def generate(room_names, thing_names):
    rooms = room_generator.generate(ROOM_NAMES, THING_NAMES)
    code_snippet = room_generator.to_inform7(rooms)
    return code_snippet


if __name__ == '__main__':
    print(generate(ROOM_NAMES, THING_NAMES))

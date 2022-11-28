import random as rd

# Example Grammar rules
rules = {
    "S": [
        ["The", "N", "V"]
    ],
    "N": [
        ["Adj", "cat"],
        ["Adj", "dog"],
        ["Adj", "tiger"],
        ["Adj", "mouse"],
        ["Adj", "penguin"],
        ["Adj", "fish"],
        ["Adj", "bird"],
        ["Adj", "snake"],
        ["Adj", "lizard"],
        ["Adj", "frog"],
        ["Adj", "turtle"],
        ["Adj", "bear"],
        ["Adj", "lion"],
        ["Adj", "wolf"],
    ],
    "V": [
        ["meows"],
        ["barks"],
        ["moos"],
        ["sings"],
        ["dances"],
        ["jumps"],
        ["runs"],
        ["swims"],
        ["flies"],
        ["hops"],
        ["yawns"],
        ["eats grass."]
    ],
    "Adj": [
        ["Stinky"],
        ["Giant"],
        ["Blue"],
        ["Spooky"],
        ["Hungry"],
        ["Sleepy"],
        ["Cute"],
        ["Fat"],
        ["Small"],
        ["Freeky"]
    ]
}

def generate_items(items):
    for item in items:
        if isinstance(item, list):
            for subitem in generate_items(item):
                yield subitem
        else:
            yield item


def expansion(start):
    for element in start:
        if element in rules:
            loc = start.index(element)
            start[loc] = rd.choice(rules[element])
        result = [item for item in generate_items(start)]

    for item in result:
        if not isinstance(item, list):
            if item in rules:
                result = expansion(result)

    return result


def to_string(result):
    return ' '.join(result)


def generate():
    out = to_string(expansion(["S"]))
    print(out)
    return out

if __name__ == "__main__":
    generate()

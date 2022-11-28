import random as rd
import partitura as pt
import partitura.performance as perf

# Example Grammar rules
rules = {
    "S": [
        {
            "id": None,
            "midi_pitch": 60,
            "note_on": (0),
            "note_off": (120),
            "track": 0,
            "channel": 0,
            "velocity": 60}, "N"],
    "N": []
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


def generate():
    notes = expansion(["S"])
    performance = perf.PerformedPart(notes, ppq=120)
    pt.save_performance_midi(performance, "test.mid")
    return performance

if __name__ == "__main__":
    generate()

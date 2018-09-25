def chunks(iterable, size, overlap=0):
    for x in range(0, len(iterable), size):
        yield iterable[x:x + size + overlap]


def flatten(sections):
    for section in sections:
        yield from section.transitions()
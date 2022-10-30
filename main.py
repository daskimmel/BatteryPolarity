from random import randint

POSITIVE = "P"
NEGATIVE = "N"

CHECK_OPPOSITE = "-?-?"
CHECK_ADJACENT = "--??"


def battery_polarity():
    batteries = [NEGATIVE, POSITIVE, NEGATIVE, NEGATIVE]

    spin(batteries)

    if is_solved(batteries):
        print("Solved")
        return

    # Step 1: peek adjacent - change both to p and check
    peek_els = CHECK_ADJACENT
    checked_batteries = peek(batteries, peek_els)

    first_peek_index = find_nth(peek_els, "?", 1)
    second_peek_index = find_nth(peek_els, "?", 2)
    batteries[first_peek_index] = POSITIVE
    batteries[second_peek_index] = POSITIVE

    if is_solved(batteries):
        print("Solved")
        return

    checked_batteries = [None, None]
    spin(batteries)

    # Step 2: peek opposite - change both to p and check

    peek_els = CHECK_OPPOSITE
    checked_batteries = peek(batteries, peek_els)
    first_peek_index = find_nth(peek_els, "?", 1)
    second_peek_index = find_nth(peek_els, "?", 2)

    if checked_batteries[0] == NEGATIVE:
        batteries[first_peek_index] = POSITIVE
    elif checked_batteries[1] == NEGATIVE:
        batteries[second_peek_index] = POSITIVE

    if is_solved(batteries):
        print("Solved")
        return

    checked_batteries = [None, None]
    spin(batteries)

    # Step 3: peek opposite - if either are n, change to p, else if both p change 1 to n

    peek_els = CHECK_OPPOSITE
    checked_batteries = peek(batteries, peek_els)
    first_peek_index = find_nth(peek_els, "?", 1)
    second_peek_index = find_nth(peek_els, "?", 2)

    if checked_batteries[0] == NEGATIVE:
        batteries[first_peek_index] = POSITIVE

    elif checked_batteries[1] == NEGATIVE:
        batteries[second_peek_index] = POSITIVE

    elif checked_batteries[0] == POSITIVE and checked_batteries[1] == POSITIVE:
        batteries[second_peek_index] = NEGATIVE

    if is_solved(batteries):
        print("Solved")
        return

    checked_batteries = [None, None]
    spin(batteries)

    # Step 4: peek adjacent -  flip both

    peek_els = CHECK_ADJACENT
    checked_batteries = peek(batteries, peek_els)
    first_peek_index = find_nth(peek_els, "?", 1)
    second_peek_index = find_nth(peek_els, "?", 2)

    if checked_batteries[0] == NEGATIVE:
        batteries[first_peek_index] = POSITIVE
    else:
        batteries[first_peek_index] = NEGATIVE

    if checked_batteries[1] == NEGATIVE:
        batteries[second_peek_index] = POSITIVE
    else:
        batteries[second_peek_index] = NEGATIVE


    if is_solved(batteries):
        print("Solved")
        return

    checked_batteries = [None, None]
    spin(batteries)

    # Step 5: peek opposite - if n change both

    peek_els = CHECK_OPPOSITE
    checked_batteries = peek(batteries, peek_els)
    first_peek_index = find_nth(peek_els, "?", 1)
    second_peek_index = find_nth(peek_els, "?", 2)

    if checked_batteries[0] == NEGATIVE:
        batteries[first_peek_index] = POSITIVE

    if checked_batteries[1] == NEGATIVE:
        batteries[second_peek_index] = POSITIVE

    if is_solved(batteries):
        print("Solved")
        return
    else:
        print("Fail")


def spin(batteries):
    spin_num = randint(100, 1000)
    i = 0

    while i < spin_num:
        end_el = batteries.pop()
        batteries.insert(0, end_el)
        i += 1


def peek(batteries, peek_els):
    first_peek_index = find_nth(peek_els, "?", 1)
    second_peek_index = find_nth(peek_els, "?", 2)
    return [batteries[first_peek_index], batteries[second_peek_index]]


def change_battery(batteries, battery_index):
    if batteries[battery_index] == POSITIVE:
        batteries[battery_index] = NEGATIVE
    else:
        batteries[battery_index] = POSITIVE


def is_solved(batteries):
    return are_all_same(batteries)


def are_all_same(batteries):
    return len(set(batteries)) == 1


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


if __name__ == '__main__':
    i = 0
    while i < 10:
        battery_polarity()
        i += 1


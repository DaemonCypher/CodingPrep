def solution(A):
    events = []
    for i, radius in enumerate(A):
        events.append((i - radius, 'start'))
        events.append((i + radius, 'end'))

    events.sort(key=lambda x: (x[0], x[1] == 'end'))  # Sort by position; end events first if positions are equal

    intersect_count = 0
    active_discs = 0

    for _, event_type in events:
        if event_type == 'start':
            intersect_count += active_discs
            active_discs += 1
        else:
            active_discs -= 1

        if intersect_count > 10000000:
            return -1

    return intersect_count

# Chatgpt
# 100%

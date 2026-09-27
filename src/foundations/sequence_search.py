from __future__ import annotations

from collections.abc import Sequence


def linear_search(values: Sequence[int], key: int) -> int | None:
    """Return the index of key using the original project's plain linear scan."""
    for index, value in enumerate(values):
        if value == key:
            return index
    return None


def linear_sentinel_search(values: Sequence[int], key: int) -> int | None:
    """Linear search with a sentinel value appended to avoid a bounds check per step."""
    if not values:
        return None
    items = list(values)
    last = items[-1]
    items[-1] = key
    index = 0
    while items[index] != key:
        index += 1
    items[-1] = last
    if index < len(items) - 1 or last == key:
        return index
    return None


def binary_search(values: Sequence[int], key: int) -> int | None:
    """Return the index of key in a sorted sequence, or None if missing."""
    left = 0
    right = len(values) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if values[mid] < key:
            left = mid + 1
        elif values[mid] > key:
            right = mid - 1
        else:
            return mid
    return None


def exponential_search(values: Sequence[int], key: int) -> int | None:
    """Find key in a sorted sequence by growing a range exponentially, then binary searching it."""
    if not values:
        return None
    if values[0] == key:
        return 0
    bound = 1
    while bound < len(values) and values[bound] < key:
        bound *= 2
    left = bound // 2
    right = min(bound, len(values) - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if values[mid] < key:
            left = mid + 1
        elif values[mid] > key:
            right = mid - 1
        else:
            return mid
    return None


def interpolation_search(values: Sequence[int], key: int) -> int | None:
    """Interpolation search for sorted, near-uniform integer sequences."""
    if not values:
        return None
    left = 0
    right = len(values) - 1
    while left <= right and values[left] <= key <= values[right]:
        if values[left] == values[right]:
            return left if values[left] == key else None
        pos = left + ((key - values[left]) * (right - left)) // (values[right] - values[left])
        if values[pos] < key:
            left = pos + 1
        elif values[pos] > key:
            right = pos - 1
        else:
            return pos
    return None

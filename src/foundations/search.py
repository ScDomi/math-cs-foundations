from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import heapq
from typing import Callable, Hashable, Iterable, TypeVar

T = TypeVar("T", bound=Hashable)


@dataclass(frozen=True)
class SearchResult:
    path: list[T]
    visited: int
    cost: float = 0.0


def reconstruct_path(came_from: dict[T, T | None], goal: T) -> list[T]:
    path = [goal]
    while came_from[path[-1]] is not None:
        path.append(came_from[path[-1]])
    path.reverse()
    return path


def breadth_first_search(start: T, is_goal: Callable[[T], bool], neighbors: Callable[[T], Iterable[T]]) -> SearchResult | None:
    queue = deque([start])
    came_from: dict[T, T | None] = {start: None}
    while queue:
        node = queue.popleft()
        if is_goal(node):
            return SearchResult(reconstruct_path(came_from, node), len(came_from), len(reconstruct_path(came_from, node)) - 1)
        for nxt in neighbors(node):
            if nxt not in came_from:
                came_from[nxt] = node
                queue.append(nxt)
    return None


def depth_first_search(start: T, is_goal: Callable[[T], bool], neighbors: Callable[[T], Iterable[T]]) -> SearchResult | None:
    stack = [start]
    came_from: dict[T, T | None] = {start: None}
    while stack:
        node = stack.pop()
        if is_goal(node):
            return SearchResult(reconstruct_path(came_from, node), len(came_from), len(reconstruct_path(came_from, node)) - 1)
        for nxt in neighbors(node):
            if nxt not in came_from:
                came_from[nxt] = node
                stack.append(nxt)
    return None


def dijkstra(start: T, is_goal: Callable[[T], bool], neighbors: Callable[[T], Iterable[tuple[T, float]]]) -> SearchResult | None:
    frontier: list[tuple[float, int, T]] = [(0.0, 0, start)]
    came_from: dict[T, T | None] = {start: None}
    cost_so_far: dict[T, float] = {start: 0.0}
    counter = 0
    while frontier:
        cost, _, node = heapq.heappop(frontier)
        if cost != cost_so_far[node]:
            continue
        if is_goal(node):
            return SearchResult(reconstruct_path(came_from, node), len(came_from), cost)
        for nxt, step_cost in neighbors(node):
            new_cost = cost + step_cost
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                came_from[nxt] = node
                counter += 1
                heapq.heappush(frontier, (new_cost, counter, nxt))
    return None


def astar(start: T, is_goal: Callable[[T], bool], neighbors: Callable[[T], Iterable[tuple[T, float]]], heuristic: Callable[[T], float]) -> SearchResult | None:
    frontier: list[tuple[float, int, T]] = [(heuristic(start), 0, start)]
    came_from: dict[T, T | None] = {start: None}
    cost_so_far: dict[T, float] = {start: 0.0}
    counter = 0
    while frontier:
        _, _, node = heapq.heappop(frontier)
        if is_goal(node):
            return SearchResult(reconstruct_path(came_from, node), len(came_from), cost_so_far[node])
        for nxt, step_cost in neighbors(node):
            new_cost = cost_so_far[node] + step_cost
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                came_from[nxt] = node
                counter += 1
                heapq.heappush(frontier, (new_cost + heuristic(nxt), counter, nxt))
    return None

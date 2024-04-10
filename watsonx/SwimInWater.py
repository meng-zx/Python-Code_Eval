from collections import deque


def can_swim(grid, t, n):
    # Directions: up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return False


def swim_in_water(grid):
    n = len(grid)
    left, right = grid[0][0], n * n - 1

    while left < right:
        mid = (left + right) // 2
        if can_swim(grid, mid, n):
            right = mid
        else:
            left = mid + 1

    return left

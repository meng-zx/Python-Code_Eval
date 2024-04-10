from collections import deque




def swim_in_water(grid):
    n = len(grid)
    queue = deque([(0, 0, 0)])
    seen = {(0, 0)}
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        r, c, time = queue.popleft()
        if r == n - 1 and c == n - 1:
            return time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                seen.add((nr, nc))
                if grid[nr][nc] <= time:
                    queue.append((nr, nc, time))

        queue.append((r, c, time + 1))

    return -1

from collections import deque



def swim_in_water(grid):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(i, j, time):
        return 0 <= i < n and 0 <= j < n and grid[i][j] <= time

    def bfs(start_time):
        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == n - 1 and j == n - 1:
                    return start_time

                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if is_valid(x, y, start_time):
                        if not visited[x][y]:
                            visited[x][y] = True
                            queue.append((x, y))

            start_time += 1

        return -1

    left, right = max(grid[0][0], grid[-1][-1]), n ** 2 - 1

    while left < right:
        mid = (left + right) // 2
        if bfs(mid) != -1:
            right = mid
        else:
            left = mid + 1

    return left

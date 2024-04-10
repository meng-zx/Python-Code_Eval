


def swim_in_water(grid):
    def min_time_to_reach_bottom_right(grid):
        # Initialize the time array with size n*n
        time = [0] * len(grid)

        # Compute the minimum time to reach the bottom right corner from every other cell
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if i == j:
                    time[i][j] = 0  # No need to swim to the same cell
                else:
                    # If the current cell has a lower elevation, we can reach it immediately
                    if grid[i][j] <= time[i - 1][j] + time[i - 1][j - 1]:
                        time[i][j] = time[i - 1][j] + time[i - 1][j - 1]
                    else:
                        # Otherwise, we need to wait for the water to rise to the current cell's elevation
                        time[i][j] = max(time[i - 1][j] + 4, time[i - 1][j - 1] + 4)

        # The minimum time to reach the bottom right corner is stored in time[len(grid)-1][len(grid)-1]
        return time[len(grid) - 1][len(grid) - 1]

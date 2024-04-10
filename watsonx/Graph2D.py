def longestIncreasingPath(matrix):
    # Initialize start and end points
    start = (0, 0)
    end = (m - 1, n - 1)

    # Initialize current path length to 0
    current_length = 0

    # Iterate through the rows and columns of the matrix
    for i in range(m):
        for j in range(n):
            # If the current cell is not the start or end point, and it has not been visited before, update the current path length and mark it as visited
            if (i, j) != start and (i, j) != end and matrix[i][j] < matrix[current_length][current_direction]:
                current_length += 1
                matrix[i][j] = matrix[current_length][current_direction]
                start = (i, j)

    # Return the length of the longest increasing path
    return current_length
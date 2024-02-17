def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])

    # Search horizontally
    for i in range(rows):
        for j in range(cols - len(word) + 1):
            if grid[i][j:j+len(word)] == list(word):
                # Highlight the found word in the grid
                for k in range(len(word)):
                    grid[i][j + k] = grid[i][j + k].upper()
                return grid

    # Search vertically
    for i in range(rows - len(word) + 1):
        for j in range(cols):
            if [grid[i + k][j] for k in range(len(word))] == list(word):
                # Highlight the found word in the grid
                for k in range(len(word)):
                    grid[i + k][j] = grid[i + k][j].upper()
                return grid

    # Search diagonally (top-left to bottom-right)
    for i in range(rows - len(word) + 1):
        for j in range(cols - len(word) + 1):
            if [grid[i + k][j + k] for k in range(len(word))] == list(word):
                # Highlight the found word in the grid
                for k in range(len(word)):
                    grid[i + k][j + k] = grid[i + k][j + k].upper()
                return grid

    # Search diagonally (bottom-left to top-right)
    for i in range(len(word) - 1, rows):
        for j in range(cols - len(word) + 1):
            if [grid[i - k][j + k] for k in range(len(word))] == list(word):
                # Highlight the found word in the grid
                for k in range(len(word)):
                    grid[i - k][j + k] = grid[i - k][j + k].upper()
                return grid

    return grid

def solve_word_search(grid, words):
    for word in words:
        result_grid = search_word([row[:] for row in grid], word)
        if any(word.isupper() for row in result_grid for word in row):
            print(f"Found '{word}':")
            print_grid(result_grid)
        else:
            print(f"Word '{word}' not found")

if __name__ == "__main__":
    num_rows = int(input("Enter the number of rows: "))
    print("Enter your word search grid (one row at a time, separated by spaces):")
    word_search_grid = [list(input().split()) for _ in range(num_rows)]

    print("Enter the words to search (separated by spaces):")
    words_to_search = input().split()

    print("\nWord Search Grid:")
    print_grid(word_search_grid)

    print("Searching for words:")
    solve_word_search(word_search_grid, words_to_search)
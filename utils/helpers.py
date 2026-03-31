def get_user_maze():
    print("\n--- Custom Maze Input ---")

    rows = int(input("Number of rows (e.g., 3): "))
    cols = int(input("Number of columns (e.g., 3): "))

    print("\nEnter the maze row by row:")
    print("Use 0 = open path, 1 = wall")
    print("You can enter like: 0 0 1  OR  001\n")

    maze = []

    for i in range(rows):
        while True:
            inp = input(f"Row {i+1}: ").strip()

            try:
                if " " in inp:
                    row = list(map(int, inp.split()))
                else:
                    row = [int(ch) for ch in inp]

                if len(row) != cols:
                    raise ValueError

                maze.append(row)
                break

            except:
                print(f"Invalid row. Enter exactly {cols} values (0 or 1).")

    # START INPUT
    print("\nEnter START position")
    print("Format: row col  (example: 0 0)")

    while True:
        try:
            start = tuple(map(int, input("Start: ").split()))
            if len(start) != 2:
                raise ValueError
            break
        except:
            print("Invalid input. Example: 0 0")

    # END INPUT
    print("\nEnter END position")
    print("Format: row col  (example: 2 2)")

    while True:
        try:
            end = tuple(map(int, input("End: ").split()))
            if len(end) != 2:
                raise ValueError
            break
        except:
            print("Invalid input. Example: 2 2")

    return maze, start, end

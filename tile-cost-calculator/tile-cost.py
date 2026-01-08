# Find Cost of Tile to Cover W x H Floor
# This program calculates the total cost of tiles
# needed to cover a floor based on width, height, and tile cost.

def calculate_tile_cost(width, height, cost_per_unit):
    area = width * height
    total_cost = area * cost_per_unit
    return area, total_cost


def main():
    try:
        width = float(input("Enter the width of the floor: "))
        height = float(input("Enter the height of the floor: "))
        cost_per_unit = float(input("Enter the cost per square unit: "))

        if width <= 0 or height <= 0 or cost_per_unit <= 0:
            print("All values must be greater than zero.")
            return

        area, total_cost = calculate_tile_cost(width, height, cost_per_unit)

        print(f"\nFloor area: {area:.2f} square units")
        print(f"Total tile cost: ${total_cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()

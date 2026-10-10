def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    bin_line = lines[0]
    meal_line = lines[1]

    bins = []

    for part in bin_line.split("|"):
        bins.append(part.split())

    ingredient_to_bin = {}
    for bin_index, ingredients in enumerate(bins):
        for ingredient in ingredients:
            ingredient_to_bin[ingredient] = bin_index

    bowls = [bowl.split() for bowl in meal_line.split(";")]

    same_bin = 0
    wrong_start = 0
    undersized_bowls = 0

    last_ingredient = None

    for i, bowl in enumerate(bowls):

        if len(bowl) < 3:
            undersized_bowls += 1

        if i > 0:
            if len(bowl) == 0 or bowl[0] != last_ingredient:
                wrong_start += 1

        for j in range(len(bowl) - 1):
            if ingredient_to_bin[bowl[j]] == ingredient_to_bin[bowl[j + 1]]:
                same_bin += 1

        
        last_ingredient = bowl[-1]

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"{same_bin} {wrong_start} {undersized_bowls}\n")

if __name__ == "__main__":
    main()
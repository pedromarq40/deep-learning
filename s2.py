def count_k4_walks(i, j, L):
    if L == 0:
        if i == j:return 1
        else: return 0
    if L % 2 == 0: sign = 1
    else: sign =-1
    if i == j:
        return (3 ** L + 3 * sign) // 4
    else:
        return (3 ** L - sign) // 4


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    bin_line = lines[0]
    q = int(lines[1].strip())
    query_lines = lines[2:2 + q]

    bins = []
    
    for part in bin_line.split("|"):
        bins.append(part.split())

    ingredient_to_bin = {}
    for bin_index, ingredients in enumerate(bins):
        for ingredient in ingredients:
            ingredient_to_bin[ingredient] = bin_index

    answers = []
    for line in query_lines:
        start, end, k_str = line.split()
        k = int(k_str)

        if k == 1:
            answers.append(1 if start == end else 0)
            continue

        bs = ingredient_to_bin[start]
        be = ingredient_to_bin[end]

        L = k - 1  
        walks = count_k4_walks(bs, be, L)

        total = walks * (3 ** (k - 2))
        answers.append(total)

    with open("output.txt", "w", encoding="utf-8") as f:
        out = []
        for a in answers:
            out.append(str(a))
        f.write(" ".join(out) + "\n")


if __name__ == "__main__":
    main()
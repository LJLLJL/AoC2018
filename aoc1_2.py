import aoc1

def iterate_freqs(list):
    seen = {}
    dupls = []
    shifts = list
    length = len(list)
    i = 0
    freq = 0
    counter = 0
    restarts = 0

    while not dupls:

        if counter > 1000000:
            print("Too many loops")
            break

        if i > length -1:
            i = 0
            restarts += 1
            print("Restarting for ", restarts, " time.")

        shift = shifts[i]
        freq = freq + shift
        if freq not in seen:
            seen[freq] = 1
            i += 1
            counter += 1
        else:
            dupls.append(freq)
            break
    return dupls


def main():
    input = aoc1.read_file("aoc1_input.txt")
    first_dupl = iterate_freqs(input)
    print(first_dupl)

if __name__ == "__main__":
    main()


def read_file(filename):
    f = open(filename, 'r')
    x = f.readlines()
    x = [int(i) for i in x]
    f.close()
    return x


def calc_freq(list):
    freq_list = [0]
    for i in range(len(list)):
        freq = freq_list[i] + list[i]
        freq_list.append(freq)

    return freq_list

def find_duplicates(list):
    seen = {}
    dupls = []
    for x in list:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupls.append(x)
            seen[x] += 1

def sum_list(list):
    return sum(list)


def main():
    input = read_file('aoc1_input.txt')
    print(input)
    freq = sum_list(input)
    print(freq)

    cumul_freq = calc_freq(input)
    print(cumul_freq)

    duplicates = find_duplicates(cumul_freq)
    print(duplicates) # no duplicates on the first iteration, need to just iterate through the inputs over again. Maybe just use while or similar to get the freq shift and just iterate

if __name__ == "__main__":
    main()
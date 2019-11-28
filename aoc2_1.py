import re
import string

def read_input(file):
    f = open(file, 'r')
    x = f.readlines()
    f.close()
    return x

def alph_list():
    return list(string.ascii_lowercase)

def match_line(line):
    alphs = alph_list()
    twos = []
    threes = []
    for i in alphs:
        count = len(re.findall(i, line))
        #print(i, " ", count)
        if count == 2:
            twos.append(i)
        elif count == 3:
            threes.append(i)
    return [twos, threes]

def main():
    letters = alph_list()
    print(letters)
    input = read_input("aoc2_input.txt")
    print(input)
    count_twos = 0
    count_threes = 0
    for a in input:
        matches = match_line(a)
        print(matches)
        if matches[0]:
            count_twos += 1

        if matches[1]:
            count_threes += 1
    print("Twos: ", count_twos, ". Threes: ", count_threes)
    print("Checksum: ", count_twos*count_threes)

if __name__ == "__main__":
    main()
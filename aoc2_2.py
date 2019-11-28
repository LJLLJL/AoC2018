import string
import re

def read_input(file):
    f = open(file, 'r')
    x = f.readlines()
    f.close()
    return x


def split_str(string):
    return [x for x in string]


def regexp_mask(string, i):
    list = split_str(string)
    list[i] = "."
    sep = ""
    return sep.join(list)

def maine():
    input = read_input("aoc2_input.txt")
    inp_list = split_str(input[0].rstrip())
    print(inp_list)
    mask = regexp_mask(inp_list, 0)
    print(mask)
    pattern = re.compile(mask)
    print(pattern)
    if pattern.search(input[1]):
        print("mäts")

def main():
    input = read_input("aoc2_input.txt")
    #print(input)
    #print(len(input[1]))
    match_count = 0
    for i in range(0,len(input)-1):
        inp_list = split_str(input[i].rstrip())
        #print(inp_list)

        for j in range(0,len(inp_list)):
            mask = regexp_mask(inp_list,j)
            #print(mask)
            pattern = re.compile(mask)
            for k in range(0,len(inp_list)-1):
                if k == i:
                    print("")
                else:
                    if pattern.search(input[k]):
                        print("Match: Text is ", input[k], ", pattern is: ", input[i], "k is ", k, ", i is ", i)
                        match_count += 1
    print(match_count)
    #if pattern.search(test_str):
    #    print("mätsää")

if __name__ == "__main__":
    main()
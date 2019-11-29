import numpy as np

def read_input(file):
    f = open(file, 'r')
    x = f.readlines()
    f.close()
    return x

def split_data(inp_row):
    #extract starting points and widths
    split = inp_row.split()
    start = split[2].split(",")
    start[1] = start[1][:-1]
    area = split[3].split("x")
    return [start,area]

def set_canvas(input):
    w_max = 0
    h_max = 0
    for i in input:
        data = split_data(i)
        w_temp = int(data[0][0]) + int(data[1][0])
        h_temp = int(data[0][1]) + int(data[1][1])

        if w_temp > w_max:
            w_max = w_temp

        if h_temp > h_max:
            h_max = h_temp
    print(w_max, h_max)
    canvas = np.zeros((w_max,h_max))
    return canvas
    #find max width and height
    #return array of correct size

def fill_canvas(input, canvas):
    #loop through input
    for i in input:
        canvas[0,0] +=1
    #increment each used
    print(canvas)

def main():
    input = read_input("aoc3_input.txt")
    print(input)
    print(split_data(input[0]))
    canvas = set_canvas(input)
    print(canvas)
    fill_canvas(input,canvas)

if __name__ == "__main__":
    main()
def create_trace(moves):
    trace = [(0,0)]
    for move in moves:
        direction = move[0]
        match direction:
            case "N":                
                for i in range(int(move[1:])):
                    x = trace[-1][0]
                    y = trace[-1][1]+1
                    trace.append((x,y))
            case "E":
                for i in range(int(move[1:])):
                    x = trace[-1][0]+1
                    y = trace[-1][1]
                    trace.append((x,y))
            case "S":
                for i in range(int(move[1:])):
                    x = trace[-1][0]
                    y = trace[-1][1]-1
                    trace.append((x,y))
            case "W":
                for i in range(int(move[1:])):
                    x = trace[-1][0]-1
                    y = trace[-1][1]
                    trace.append((x,y))
    return trace

with open("doc/junior/2026/2026CCCJuniorTestData/j4/data/j4.04.04.in", "r") as file:
    # content = file.read()
    # print(content)

    m = file.readline().strip()
    s = []
    while True:
        line = file.readline()
        s.append(line.strip())
        if not line:
            break
s.pop(len(s)-1)
print(m, s)


# m = int(input("Number of movements taken by the snail: "))
# s = []
# for i in range(int(m)):
#     s.append(input("Direction (N, E, S, or W) followed by number of moves: "))
# print(m, s)
# print(s[2][0])

trace = create_trace(s)
print(trace)

t = len(trace)-len(set(trace))
print(t)
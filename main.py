class Node:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "" + str(self.x) + " " + str(self.y)
    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


def go():
    start = Node(0, 0)
    end = Node(3, 3)
    list = []
    innerList = []
    for _ in range(4):
        for _ in range(4):
            x = input()
            innerList.append(x)
        list.append(innerList)
        innerList = []

    print(list)
    parent = {start: None}
    level = {start: 0}
    frontier = [start]
    f = 1
    flag = False
    while frontier:
        next = []
        temp =[]
        for item in frontier:
            temp = construct_nodes(item, len(list) - 1, len(list[0]) - 1)
            for value in temp:
                if value not in level and list[value.x][value.y] == '1':
                    level[value] = f
                    parent[value] = item
                    next.append(value)
                if value == end:
                    flag = True
                    break

        if flag :
            break
        frontier = next
        f += 1
    print(level[end])
    print("the path :")
    shortest_path(parent,start,end)

def shortest_path(parent, src, dest):
    if src == dest:
        return
    else:
        shortest_path(parent, src, parent[dest])
        print(dest)


def construct_nodes(edge, rows, cols):
    list = []
    x = edge.x
    y = edge.y
    if valid(x - 1, y, rows, cols):   list.append(Node(x - 1, y))
    if valid(x + 1, y, rows, cols):   list.append(Node(x + 1, y))
    if valid(x, y + 1, rows, cols):   list.append(Node(x, y + 1))
    if valid(x, y - 1, rows, cols):   list.append(Node(x, y - 1))
    return list


def valid(x, y, rows, cols):
    return (x <= rows) and (x > -1) and (y <= cols) and (y > -1)


if __name__ == '__main__':
    go()

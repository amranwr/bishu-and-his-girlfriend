
def dfs():
    x= int(input())
    v = []
    adj= dict()
    for i in range(1,x+1):
        adj[i] =[]
        v.append(i)
    for _ in range(x-1):
        data = input()
        temp = data.split(' ')
        adj[int(temp[0])].append(int(temp[1]))
    count  = int(input())
    q = {}
    for _ in range(count):
        temp = int(input())
        q[temp] = False

    parent={}
    for s in v :
        if s not in parent:
            parent[s] = None
            dfsVisit(q,parent , adj , s)

    min_dist =1000000000
    hold = 1
    for key , value in q.items():
        if value == True:
            if key - 1 < min_dist:
                hold = key
                min_dist = key -1

    print(hold)
def dfsVisit(q,parent,adj,s):
    for v in adj[s]:
        if v not in parent:
            if v in q :
                q[v]= True
            parent[v] = s
            dfsVisit(q,parent,adj,v)


if __name__ == '__main__':
    dfs()

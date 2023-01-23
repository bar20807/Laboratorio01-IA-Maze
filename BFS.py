#Algoritmo BFS para solucionar el laberinto
def BFS(m):
    start = (m.row, m.cols)
    frontier = [start]
    visited =  [start]
    bfsPath = {}
    while len(frontier)>0:
        currCell = frontier.pop(0)
        if currCell==(1,1):
            break
        for n in m.neighbors(currCell):
            if n not in visited:
                frontier.append(n)
                visited.append(n)
                bfsPath[n] = currCell
    fwdPath={}
    currCell = (1,1)
    while currCell != start:
        fwdPath[currCell] = bfsPath[currCell]
        currCell = bfsPath[currCell]
    return fwdPath



from collections import defaultdict, deque


class shortestPath:
    def __init__(self, lis, nodes):
        self.lis = lis
        self.graph = defaultdict(list)
        self.nodes = nodes
        self.__buildGraph()

    def __buildGraph(self):
        for node in self.lis:
            self.graph[node[0]].append(node[1])
            self.graph[node[1]].append(node[0])

    def bfs(self, dest: int, src: int):
        # Create a queue
        parent = defaultdict(int)
        q = deque()

        # maintain a list of visited node
        visited = [False for i in range(self.nodes)]

        # initialize with the start point
        q.append(src)
        visited[src] = True

        # check while dest isn't reached or the queue is empty
        while q:
            nd = q.popleft()
            if nd == dest:
                path = [nd]
                while nd != src:
                    nd = parent[nd]
                    path.append(nd)

                return path

            # relax the edge
            for neighbour in self.graph[nd]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    parent[neighbour] = nd
                    visited[neighbour] = True
        return False

    def dfs(self, dest: int, src: int):
        stack = [src]

        visited = [False for i in range(self.nodes)]
        visited[src] = True

        parent = defaultdict(int)

        while stack:
            nd = stack.pop()
            if nd == dest:
                path = [nd]
                while nd != src:
                    nd = parent[nd]
                    path.append(nd)

                return path

            for neighbour in self.graph[nd]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    parent[neighbour] = nd
                    visited[neighbour] = True

        return False


path = shortestPath([(9, 11), (12, 10), (10, 11), (4, 5), (5, 6), (2, 1), (1, 3), (4, 7), (4, 8), (5, 8),
                    (5, 9), (6, 9), (2, 12), (12, 3), (0, 1), (0, 5), (1, 4), (7, 8), (7, 11), (8, 11), (12, 7), (3, 7)], 13)

p = path.dfs(dest=12, src=0)
print(p)

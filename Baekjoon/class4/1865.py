import sys
input = sys.stdin.readline
INF = int(1e9)

TC = int(input())

def bf(roads):
    dist = [0 for _ in range(N+1)]
    for i in range(N):
        for (s, e), t in roads.items():
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == N-1:
                    return True
    return False

for _ in range(TC):
    N, M, W = map(int, input().split())
    roads = dict()

    for i in range(M+W):
        S, E, T = map(int, input().split())
        if i < M:
            roads[(S, E)] = min(roads.get((S,E), INF), T)
            roads[(E, S)] = min(roads.get((E,S), INF), T)
        else:
            roads[(S, E)] = min(roads.get((S,E), INF), -T)

    print("YES" if bf(roads) else "NO")
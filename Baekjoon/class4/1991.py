# import sys
# input = sys.stdin.readline

# def init_visited():
#     global visited
#     for idx in range(len(visited)):
#         visited[idx] = False

# def preorder(node):
#     print(node, end = '')
#     visited[ord(node) - ord('A')] = True

#     for n_node in graph[node]:
#         if n_node == '.' or visited[ord(n_node) - ord('A')]:
#             continue
#         preorder(n_node)

# def inorder(node):
#     visited[ord(node) - ord('A')] = True

#     l_node, r_node = graph[node]
#     if l_node == '.' or visited[ord(l_node) - ord('A')]:
#         pass
#     else:
#         inorder(l_node)
        
#     print(node, end = '')
    
#     if r_node == '.' or visited[ord(r_node) - ord('A')]:
#         pass
#     else:
#         inorder(r_node)

# def postorder(node):
#     visited[ord(node) - ord('A')] = True

#     for n_node in graph[node]:
#         if n_node == '.' or visited[ord(n_node) - ord('A')]:
#             continue
#         postorder(n_node)
#     print(node, end = '')

# N = int(input())
# visited = [False] * N
# graph = dict()

# for _ in range(N):
#     node, left, right = map(str, input().split())
#     graph[node] = (left, right)

# preorder('A')
# print()

# init_visited()
# inorder('A')
# print()

# init_visited()
# postorder('A')

import sys
input = sys.stdin.readline

def preorder(node):
    if node == '.':
        return
    print(node, end = '')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end = '')
    inorder(graph[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end = '')

N = int(input())
graph = dict()

for _ in range(N):
    node, left, right = map(str, input().split())
    graph[node] = (left, right)

preorder('A')
print()

inorder('A')
print()

postorder('A')
from collections import defaultdict

def solution(n, wires):
    answer = n
    graph = defaultdict(list)
    for w1, w2 in wires:
        graph[w1].append(w2)
        graph[w2].append(w1)
    
    def dfs(node, visited, skip):
        visited.add(node)
        size = 1
        for g in graph[node]:
            if g in skip:
                continue
            if g not in visited:
                size += dfs(g, visited, skip)
        return size
            
    for w1, w2 in wires:
        visited = set()
        subtree_size = dfs(w1, visited, (w1, w2))
        answer = min(answer, abs(subtree_size - (n-subtree_size)))
        
    return answer

# defaultdict로 코드 간결하게 함
# 변수명 알아보기 쉽게 변경
# 하나의 서브트리만 구하고 다른 서브트리는 n에서 뺌
# remove, append 하지 않고 skip으로 넘겨서 시간 복잡도 줄임

# def solution(n, wires):
#     answer = len(wires)
#     wire_dict = {}
    
#     def dfs(arr, arr_s):
#         for a in arr:
#             if a in arr_s:
#                 continue
#             arr_s.add(a)
#             arr_s.update(dfs(wire_dict[a], arr_s))
#         return arr_s
    
#     for w1, w2 in wires:
#         if w1 not in wire_dict:
#             wire_dict[w1] = [w2]
#         else:
#             wire_dict[w1].append(w2)
        
#         if w2 not in wire_dict:
#             wire_dict[w2] = [w1]
#         else:
#             wire_dict[w2].append(w1)
            
#     for w1, w2 in wires:
#         wire_dict[w1].remove(w2)
#         wire_dict[w2].remove(w1)
        
#         w1_set = {w1}
#         w2_set = {w2}
        
#         w1_set.update(dfs(wire_dict[w1], {w1}))   
#         w2_set.update(dfs(wire_dict[w2], {w2}))
            
#         wire_dict[w1].append(w2)
#         wire_dict[w2].append(w1)
        
#         answer = min(answer, abs(len(w1_set)-len(w2_set)))
        
#     return answer
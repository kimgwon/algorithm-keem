def solution(cacheSize, cities):
    CACHE_HIT = 1
    CACHE_MISS = 5
    
    cache = {}
    answer = 0
    
    for idx, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            cache[city] = idx
            answer += CACHE_HIT
        else:
            if len(cache) >= cacheSize > 0:
                removeCity = sorted(list(cache.items()), key = lambda x: x[1])[0]
                del cache[removeCity[0]]
            if cacheSize > 0:
                cache[city] = idx
            answer += CACHE_MISS
            
    return answer
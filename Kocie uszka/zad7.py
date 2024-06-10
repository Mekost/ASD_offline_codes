# moja upiekszona by chatgpt
def maze(L):
    def is_valid(y, x):
        return 0 <= y < n and 0 <= x < n and L[y][x] == '.'
    
    def explore(y, x, direction):
        if not is_valid(y, x):
            return float('-inf')
        if direction == "down":
            if down_cache[y][x] == -1:
                down_cache[y][x] = max(explore(y, x - 1, "all"), explore(y + 1, x, "down")) + 1
            return down_cache[y][x]
        elif direction == "up":
            if up_cache[y][x] == -1:
                up_cache[y][x] = max(explore(y, x - 1, "all"), explore(y - 1, x, "up")) + 1
            return up_cache[y][x]
        elif direction == "all":
            return max(explore(y, x, "down"), explore(y, x, "up"))
    
    n = len(L)
    down_cache = [[-1] * n for _ in range(n)]
    up_cache = [[-1] * n for _ in range(n)]
    down_cache[0][0] = 0
    up_cache[0][0] = 0
    
    result = explore(n - 1, n - 1, "all")
    return result if result != float('-inf') else -1
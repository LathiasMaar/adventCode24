f = open ('Day19/input.txt','r')
input = f.read().strip().split('\n\n')
f.close()

def check_patterns(design, patterns):

    pattern_set = set(patterns)
    n = len(design)

    dp = [0] * (n + 1)
    dp[0] = 1 
    
    # Llenar la tabla DP
    for i in range(1, n + 1):
        for pattern in pattern_set:
            pattern_len = len(pattern)
            if i >= pattern_len and design[i - pattern_len:i] == pattern:
                dp[i] += dp[i - pattern_len]
    
    
    return dp[n]


patterns = input[0].split(', ')
designs = input[1].split()

cnt = 0
for design in designs:
    cnt += check_patterns(design, patterns)

print(cnt)
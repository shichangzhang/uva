t = int(input())

cache = {}
MOD = 998244353

def fastexp(exp):
    if exp in cache:
        return cache[exp]

    if exp == 0:
        return 1
    result = fastexp(exp//2)
    result = (result * result) % MOD
    result = (result * 2 ** (exp % 2)) % MOD

    cache[exp] = result

    return result

def add(a, b):
    return (a % MOD + b % MOD) % MOD

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    p_max_index = [0]
    q_max_index = [0]
    for i in range(1, n):
        p_max_index.append(p_max_index[i-1] if p[p_max_index[i-1]] > p[i] else i)
        q_max_index.append(q_max_index[i-1] if q[q_max_index[i-1]] > q[i] else i)

    r = []
    for i in range(n):
        max_p = p[p_max_index[i]]
        max_q = q[q_max_index[i]]
        
        result = 0
        if max_p > max_q:
            j = i - p_max_index[i]
            result = add(fastexp(max_p), fastexp(q[j]))
        elif max_p < max_q:
            j = i - q_max_index[i]
            result = add(fastexp(p[j]), fastexp(max_q))
        else:
            jp = i - p_max_index[i]
            jq = i - q_max_index[i]
            if q[jp] > p[jq]:
                result = add(fastexp(max_p), fastexp(q[jp]))
            else:
                result = add(fastexp(p[jq]), fastexp(max_q))

        r.append(result)
    print(*r)
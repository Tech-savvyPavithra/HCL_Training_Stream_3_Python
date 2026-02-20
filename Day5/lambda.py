def lam(names):
    ans = list(map(lambda x : x.strip().title(), names))
    return ans

names = ["  alpha Case  ", "Beta   unit", "gAmMa MODULE  "]
print(lam(names))


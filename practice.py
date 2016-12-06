def transform(name):
    p = ["코카콜라", "미에로 화이바", "핫식스", "새우깡", "누드 빼빼로"]
    for i in range(len(p)):
        if name == p[i]:
            return i
    return 5

print(transform("미에로 화이바"))

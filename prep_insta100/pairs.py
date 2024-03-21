def find_pairs(pairs):
    s = set()

    for (x, y) in pairs:
        if (y, x) in s or (x, y) in s:  
            print((x, y)) 
        else:
            s.add((x, y))  

pairs = [(6, 5), (7, 8), (9, 5), (8, 4), (8, 4)]
find_pairs(pairs)

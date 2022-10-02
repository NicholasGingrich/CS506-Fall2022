def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
     sum = 0
     for i in range(len(x)):
         sum += (abs(x[i] - y[i]))
     return sum


def jaccard_dist(x, y):
    same_ones = 0
    union_size = 0
    for i in range(len(x)):
        if x[i] == 1 or y[i] == 1: #if there is a 1 present add to our union size
            union_size += 1

        if x[i] == 1 and y[i] == 1:
            same_ones += 1 #increase the size of the intersection if they are the same word

    return same_ones/union_size 


def cosine_sim(x, y):
    return 2

# Feel free to add more

def sum_odd(integer):
    if integer <= 10:
        if integer % 2 != 0:
            return integer % 10
        return 0
    if integer % 2 != 0:
        return integer % 10 + sum_odd(integer // 10)
    return sum_odd(integer // 10)

def test_sum_odd(k):
    if k<10:
        if k%2 != 0:
            return k
        return 0
    
    return k%10 + sum_odd(k//10)

print(test_sum_odd(1235))
print(test_sum_odd(222))

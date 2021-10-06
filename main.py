def is_prime(n):
    '''
    Determina daca numarul este prim
    :param n: nr intreg
    :return: True daca n e prim si False altfel
    '''
    if (n < 2): return False
    for div in range(2, n // 2):
        if n % div == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2)==True
    assert is_prime(17) == True
    assert is_prime(-22) == False

test_is_prime()

def get_largest_prime_below(n):
    '''
    Găsește ultimul număr prim mai mic decât un număr dat
    :param n: nr intreg
    :return: cel mai mare număr prim mai mic decât n
    '''
    a=n-1
    while (a > 0):
        if is_prime(a):
            return a
        else : a=a-1

def test_get_largest_prime_below():
    assert get_largest_prime_below(20)==19
    assert get_largest_prime_below(10)==7
    print (get_largest_prime_below(20))
    print (get_largest_prime_below(34))

test_get_largest_prime_below()

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

def get_newton_sqrt(n,steps):
    '''
    :param n:numarul caruia ii calculam radicalul
    :param steps: numarul de pasi pentru calcularea radicalului
    :return: radicalul
    '''
    a=n
    x0=2;
    for i in range (steps):
        #x_(n+1)=0.5*(x_n+a/value)*0.5
        if i != 0 : n=(n+ a/n)*0.5
        else : n= (x0+a/x0)*0.5
    return float(n)

def test_get_newton_sqrt():
    assert get_newton_sqrt(4,2)==2
    assert get_newton_sqrt(9, 2)>3 and get_newton_sqrt(9, 2)<3.1
    assert get_newton_sqrt(15, 2)>3.9 and get_newton_sqrt(15, 2)<4
    print(get_newton_sqrt(9,2))
    print(get_newton_sqrt(15,2))

test_get_newton_sqrt()

def get_temp(temp: float, fromt: str, to: str) -> float:
    '''
    :param temp: Temperatura introdusa
    :param fromt: Scara in care este temperatura introdusa
    :param to: Scara in care vom converti temperatura introdusa
    :return: Temperatura convertita in scara ceruta
    '''
    if fromt == 'C':
        if to == 'K':
            return temp + 273.15
        elif to == 'F':
            return temp * 1.8 + 32
    elif fromt == 'K':
        if to == 'C':
            return temp - 273.15
        elif to == 'F':
            return (temp - 32) / 1.8 + 273.15
    elif fromt == 'F':
        if to == 'C':
            return (temp - 32) / 1.8
        elif to == 'K':
            return (temp - 32) * 5 / 9 + 273.15


def test_get_temp():
    assert (round(get_temp(300, 'K', 'C'), 2)) == 26.85
    assert (round(get_temp(16, 'C', 'F'), 2)) == 60.8
    assert (round(get_temp(45, 'F', 'K'), 2)) == 280.37

test_get_temp()







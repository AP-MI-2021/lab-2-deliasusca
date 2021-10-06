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
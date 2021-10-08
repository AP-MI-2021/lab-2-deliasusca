
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
            return temp*1.8 + 32
    elif fromt == 'K':
        if to == 'C':
            return temp - 273.15
        elif to == 'F':
            return (temp-32)/1.8 + 273.15
    elif fromt == 'F':
        if to == 'C':
            return (temp-32)/1.8
        elif to == 'K':
            return (temp-32)*5/9 + 273.15

def test_get_temp():
    assert (round(get_temp(300,'K','C'),2))==26.85
    assert (round(get_temp(16, 'C', 'F'), 2)) == 60.8
    assert (round(get_temp(45, 'F', 'K'), 2)) == 280.37
    
test_get_temp()






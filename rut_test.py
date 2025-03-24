from testt import validate  

def test_rut_correcto():
    rut_valido = "11111111-1"  
    assert validate(rut_valido) == True

def test_rut_incorrecto():
    rut_invalido = "11111111-0"  
    assert validate(rut_invalido) == False

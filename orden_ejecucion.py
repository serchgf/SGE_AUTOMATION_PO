import pytest

def run_test():
    # ORDEN DE EJECUCION PO NACIONAL DESDE CREAR 'PO SIN DSO' CON STATUS 'CONFIRMADA VALIDO' HASTA TENER UNA FACTURA CON 'STATUS RECIBIDO TOTAL'
    pytest.main(["-s","test_MTC_ASGE_001.py"])
    pytest.main(["-s", "test_MTC_ASGE_003.py"])
    pytest.main(["-s", "test_MTC_ASGE_006.py"])
    pytest.main(["-s", "test_MTC_ASGE_007.py"])
    pytest.main(["-s", "test_MTC_ASGE_008.py"])
    pytest.main(["-s", "test_MTC_ASGE_009.py"])

if __name__ =="__main__":
    run_test()
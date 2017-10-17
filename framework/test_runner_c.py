from Classes import Status
from runner import run
from test_data import tc1, c_source_code_add_two_numbers, c_source_code_add_two_numbers_compile_error


def test_c_add_two_numbers_code():
    out = run(c_source_code_add_two_numbers, "c", ["gcc", "-o", "program"], ["./program"], [tc1])
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status


def test_c_add_two_numbers_code_compile_error():
    out = run(c_source_code_add_two_numbers_compile_error, "c", ["gcc", "-o", "program"], ["./program"], [tc1])
    assert 1 == len(out)
    assert ": error: expected" in out[0].stderr
    assert "sum = a  b;" in out[0].stderr
    assert Status.COMPILE_ERROR == out[0].status

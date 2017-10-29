from Classes import Status
from runner import run
from test_data import tc1, cpp_source_code_add_two_numbers, c_source_code_add_two_numbers_compile_error


def test_c_add_two_numbers_code():
    out = run(cpp_source_code_add_two_numbers, "cpp", ["g++", "-o", "program"], ["./program"], [tc1])
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status


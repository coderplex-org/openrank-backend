from framework.Classes import Status
from framework.runner import run
from framework.test_data import tc1, python3_source_code_add_two_numbers, python2_source_code_add_two_numbers


def test_python3_add_two_numbers_code():
    out = run(python3_source_code_add_two_numbers, "py", None, ["python3", "Source.py"], [tc1])
    print(out)
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status


def test_python2_add_two_numbers_code():
    out = run(python2_source_code_add_two_numbers, "py", None, ["python2", "Source.py"], [tc1])
    print(out)
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status

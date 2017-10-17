from framework.Classes import Status
from framework.runner import run
from framework.test_data import tc1, cs_source_code_add_two_numbers


def test_cs_add_two_numbers_code():
    out = run(cs_source_code_add_two_numbers, "cs", ["mcs"], ["mono", "Program.exe"], [tc1])
    print(out)
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status



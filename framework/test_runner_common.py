from Classes import Status
from runner import run
from test_data import java_source_code_with_input, tc1, tc2, java_source_code_with_no_input


def test_with_no_input():
    out = run(java_source_code_with_no_input, "java", ["javac"], ["java", "Solution"])
    assert 1 == len(out), 'Only 1 output must exist'
    assert 'Hello World' == out[0].stdout
    assert Status.OK == out[0].status


def test_two_inputs():
    out = run(java_source_code_with_input, "java", ["javac"], ["java", "Solution"], [tc1, tc2])
    assert 2 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status
    assert '55' == out[1].stdout
    assert Status.OK == out[1].status


def test_with_incorrect_compile_command():
    out = run(java_source_code_with_no_input, "java", ["javacxyz"], ["java", "Solution"])
    assert 1 == len(out), 'Only 1 output must exist'
    assert 'No such file or directory' in out[0].stderr
    assert Status.ENV_CRASH == out[0].status


def test_with_incorrect_run_command():
    out = run(java_source_code_with_no_input, "java", ["javac"], ["javaxyz", "Solution"])
    assert 1 == len(out), 'Only 1 output must exist'
    assert 'No such file or directory' in out[0].stderr
    assert Status.ENV_CRASH == out[0].status

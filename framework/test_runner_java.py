from framework.Classes import Status
from framework.runner import run
from framework.test_data import java_source_code_with_exception, java_source_code_with_compile_error, java_source_code_with_input, tc1


def test_add_two_numbers_code():
    out = run(java_source_code_with_input, "java", ["javac"], ["java", "Solution"], [tc1])
    assert 1 == len(out)
    assert '57' == out[0].stdout
    assert Status.OK == out[0].status


def test_executable_java_code_with_runtime_exception():
    out = run(java_source_code_with_exception, "java", ["javac"], ["java", "Solution"])
    assert 1 == len(out)
    assert 'java.lang.RuntimeException' in out[0].stderr
    assert Status.RUNTIME_ERROR == out[0].status


def test_executable_java_code_with_compile_error():
    out = run(java_source_code_with_compile_error, "java", ["javac"], ["java", "Solution"])
    assert 1 == len(out)
    assert "error: ';' expected" in out[0].stderr
    assert Status.COMPILE_ERROR == out[0].status

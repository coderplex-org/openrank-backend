from framework.Classes import Status
from framework.runner import run
from data import java_source_code_with_exception, java_source_code_with_compile_error


def test_executable_java_code_with_runtime_exception():
    out = run(java_source_code_with_exception, "java", "javac", ["java", "Solution"])
    assert 1 == len(out)
    assert 'java.lang.RuntimeException' in out[0].output
    assert Status.RUNTIME_ERROR == out[0].status


def test_executable_java_code_with_compile_error():
    out = run(java_source_code_with_compile_error, "java", "javac", ["java", "Solution"])
    assert 1 == len(out)
    assert "error: ';' expected" in out[0].output
    assert Status.COMPILE_ERROR == out[0].status

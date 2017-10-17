import subprocess
import os
import uuid
import shutil

from framework.Classes import Output, Status, Testcase

default_test_case = Testcase()
default_test_case.timeout = 2
default_test_case.id = "1"
default_testcase_array = [default_test_case]


def run(source, source_extension, compile_commands, run_commands, test_cases=default_testcase_array):
    result = []
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)

    try:
        source_file_name = create_source_file(source, source_extension)
        out_compile = compile_source(compile_commands, source_file_name, result)
        execute_tests(run_commands, test_cases, out_compile, result)
    except Exception as e:
        out_exception = Output()
        result.append(out_exception)
        out_exception.status = Status.ENV_CRASH
        out_exception.stderr = str(e)
        print(os.sys.exc_info())

    os.chdir(current_directory)
    shutil.rmtree(temp_dir, True)

    return result


def execute_tests(run_command, test_cases, out_compile, result):
    if out_compile.status != Status.COMPILE_ERROR:
        for test_case in test_cases:
            out_test = Output()
            out_test.test_case_id = test_case.id

            if run_command:
                completed = subprocess.run(run_command,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           input=test_case.input.encode('utf-8'),
                                           timeout=test_case.timeout)
                out_test.stdout = completed.stdout.decode('utf-8').rstrip()
                out_test.stderr = completed.stderr.decode('utf-8').rstrip()

                if completed.returncode:
                    out_test.status = Status.RUNTIME_ERROR
                else:
                    out_test.status = Status.OK

                result.append(out_test)


def compile_source(compile_commands, source_file_name, result):
    out_compile = Output()
    if compile_commands:
        compile_commands.append(source_file_name)
        completed = subprocess.run(compile_commands,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        if completed.returncode:
            result.append(out_compile)
            out_compile.status = Status.COMPILE_ERROR
            out_compile.stdout = completed.stdout.decode('utf-8').rstrip()
            out_compile.stderr = completed.stderr.decode('utf-8').rstrip()
    else:
        out_compile.status = Status.OK

    return out_compile


def create_source_file(source, source_extension):
    source_file_name = "Source." + source_extension
    text_file = open(source_file_name, "w")
    text_file.write(source)
    text_file.close()
    return source_file_name



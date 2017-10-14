import subprocess
import os
import uuid
import shutil

from framework.Classes import Output, Status, Testcase


def run(source, source_extension, compile_command, run_command, test_cases):
    source_file_name = "Source." + source_extension
    result = []
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)

    try:
        text_file = open(source_file_name, "w")
        text_file.write(source)
        text_file.close()

        status = 0
        out_compile = Output()
        if compile_command:
            completed = subprocess.run([compile_command, source_file_name],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            if completed.returncode:
                result.append(out_compile)
                out_compile.status = Status.COMPILE_ERROR
                out_compile.output = completed.stdout.decode('utf-8') + completed.stderr.decode('utf-8')

        if not out_compile.status:
            for test_case in test_cases:
                out_test = Output()
                out_test.test_case_id = test_case.id
                result.append(out_test)
                if run_command:
                    completed = subprocess.run(run_command,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               input=test_case.input.encode('utf-8'),
                                               timeout=test_case.timeout)
                    out_test.output = completed.stdout.decode('utf-8') + completed.stderr.decode('utf-8')
                    out_test.output = out_test.output.rstrip()
                    if completed.returncode:
                        out_test.status = Status.RUNTIME_ERROR
                    else:
                        out_test.status = Status.OK

    except:
        out_exception = Output()
        result.append(out_exception)
        out_exception.status = Status.ENV_CRASH
        print(os.sys.exc_info())

    os.chdir(current_directory)
    shutil.rmtree(temp_dir, True)

    return result


source_code = """
                import java.util.*;
                
                class Solution{
                    public static void main(String... args) {
                        Scanner scan = new Scanner(System.in);
                        int sum = scan.nextInt() + scan.nextInt();
                        System.out.println(sum);
                    }
                }
             """

tc1 = Testcase()
tc1.id = "1"
tc1.input = "23 34"
tc1.timeout = 1

tc2 = Testcase()
tc2.id = "2"
tc2.input = "21 34"
tc2.timeout = 1

out = run(source_code, "java", "javac", ["java","Solution"], [tc1, tc2])
print(out)

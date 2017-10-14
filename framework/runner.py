import subprocess
import os
import uuid
import shutil

from framework.Classes import Output


def run(source, source_extension, compile_command, run_command, test_cases):
    source_file_name = "Source." + source_extension
    output = Output()
    current_directory = os.getcwd()
    temp_dir = uuid.uuid4().hex
    os.makedirs(temp_dir)
    os.chdir(temp_dir)
    text_file = open(source_file_name, "w")
    text_file.write(source)
    text_file.close()

    if compile_command:
        status = subprocess.call([compile_command, source_file_name])
        if status:
            output.status = "COMPILE_ERROR"
            output.custom = "XYZ"

    if not output.status and run_command:
        subprocess.call(run_command)

    os.chdir(current_directory)
    shutil.rmtree(temp_dir, True)

    return output


source_code = """class Solution{
                    public static void main(String... args) {
                        System.out.println("Hello Compiler");
                    }
                }"""

out = run(source_code, "java", "javac", ["java","Solution"], [])
print(out.output)
print(out.status)

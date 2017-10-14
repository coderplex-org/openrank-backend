from enum import Enum


class Status(Enum):
    IN_PROGRESS = 0
    OK = 1
    COMPILE_ERROR = 2
    RUNTIME_ERROR = 3
    TIMEOUT = 3
    ENV_CRASH = 4


class ProgrammingLanguage(Enum):
    C = "C"
    CPP = "C++"
    JAVA8 = "Java 8"
    PYTHON2 = "Python 2"
    PYTHON = "Python 3"
    RUBY = "Ruby"
    JAVASCRIPT = "Node.js"


class Submission:
    def __init__(self):
        self.source = ""
        self.programming_language = ""
        self.compile_command = []
        self.run_command = []
        self.test_cases_input = []


class Testcase:
    def __init__(self):
        self.id = ""
        self.input = ""
        self.file = ""
        self.timeout = 2


class Output:
    def __init__(self):
        self.test_case_id = ""
        self.memory = 0
        self.time = 0
        self.output = ""
        self.status = Status.IN_PROGRESS

    def __repr__(self):
        return self.output





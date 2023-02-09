from aoj.aoj import *
from aoj.base import *
from enum import Enum

class Language(Enum):
    """Programming languages"""
    Python3 = "Python3"
    C = "C"
    CPP = "C++"
    Java = "JAVA"

class Status(Enum):
    """Judge status"""
    CompileError = 0
    WrongAnswer = 1
    TimeLimitExceeded = 2
    MemoryLimitExceeded = 3
    Accepted = 4
    JudgeWaiting = 5
    OutputLimitExceeded = 6
    RuntimeError = 7
    PresentationError = 8
    JudgeRunning = 9

# Excluding: Accepted, JudgeWaiting, JudgeRunning
WA_STATUSES = [ Status.CompileError, Status.WrongAnswer, Status.TimeLimitExceeded,
            Status.MemoryLimitExceeded, Status.OutputLimitExceeded, Status.RuntimeError, Status.PresentationError ]

def get_status_str(status: int) -> str:
	if status == Status.CompileError:
		return "Compile Error"
	elif status == Status.WrongAnswer:
		return "Wrong Answer"
	elif status == Status.TimeLimitExceeded:
		return "Time Limit Exceeded"
	elif status == Status.MemoryLimitExceeded:
		return "Memory Limit Exceeded"
	elif status == Status.Accepted:
		return "Accepted"
	elif status == Status.JudgeWaiting:
		return "Judge Waiting"
	elif status == Status.OutputLimitExceeded:
		return "Output Limit Exceeded"
	elif status == Status.RuntimeError:
		return "Runtime Error"
	elif status == Status.PresentationError:
		return "Presentation Error"
	elif status == Status.JudgeRunning:
		return "Judge Running"
	else:
		raise ValueError

def get_short_status_str(status: int) -> str:
	if status == Status.CompileError:
		return "CE"
	elif status == Status.WrongAnswer:
		return "WA"
	elif status == Status.TimeLimitExceeded:
		return "TLE"
	elif status == Status.MemoryLimitExceeded:
		return "MLE"
	elif status == Status.Accepted:
		return "AC"
	elif status == Status.JudgeWaiting:
		return "JW"
	elif status == Status.OutputLimitExceeded:
		return "OLE"
	elif status == Status.RuntimeError:
		return "RE"
	elif status == Status.PresentationError:
		return "PE"
	elif status == Status.JudgeRunning:
		return "JR"
	else:
		raise ValueError

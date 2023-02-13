from enum import Enum
from typing import Union

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

__STR_MAP = {
    Status.CompileError: "Compile Error",
    Status.WrongAnswer: "Wrong Answer",
    Status.TimeLimitExceeded: "Time Limit Exceeded",
    Status.MemoryLimitExceeded: "Memory Limit Exceeded",
    Status.Accepted: "Accepted",
    Status.JudgeWaiting: "Judge Waiting",
    Status.OutputLimitExceeded: "Output Limit Exceeded",
    Status.RuntimeError: "Runtime Error",
    Status.PresentationError: "Presentation Error",
    Status.JudgeRunning: "Judge Running",
}

__SHORT_STR_MAP = {
    Status.CompileError: "CE",
    Status.WrongAnswer: "WA",
    Status.TimeLimitExceeded: "TLE",
    Status.MemoryLimitExceeded: "MLE",
    Status.Accepted: "AC",
    Status.JudgeWaiting: "JW",
    Status.OutputLimitExceeded: "OLE",
    Status.RuntimeError: "RE",
    Status.PresentationError: "PE",
    Status.JudgeRunning: "JR",
}

# Excluding: Accepted, JudgeWaiting, JudgeRunning
WA_STATUSES = [ Status.CompileError, Status.WrongAnswer, Status.TimeLimitExceeded,
            Status.MemoryLimitExceeded, Status.OutputLimitExceeded, Status.RuntimeError, Status.PresentationError ]

def get_status(status: int) -> Status:
    return Status(status)

def get_status_str(status: Union[Status, int]) -> str:
    if isinstance(status, int):
        status = get_status(status)
    return __STR_MAP[status]

def get_short_status_str(status: Union[Status, int]) -> str:
    if isinstance(status, int):
        status = get_status(status)
    return __SHORT_STR_MAP[status]

import os
from datetime import datetime, timezone, timedelta
from typing import List, Optional

#############
### Files ###
#############

def get_code_filepath(corpus_dir: str, judge_id: int) -> Optional[str]:
    """Get fullpath from judge_id"""
    # Greater than or equal to 6,800,000 is not yet available
    if (judge_id > 6800000):
        return None
    
    dirname = f"{judge_id//100000:03}"
    filename = f"{judge_id}.txt"
    filepath = os.path.join(corpus_dir, dirname, filename)

    if (not os.path.exists(filepath)):
        return None
    
    return filepath

def get_code(corpus_dir: str, judge_id: int) -> Optional[str]:
    """Get code from judge_id"""
    filepath = get_code_filepath(corpus_dir, judge_id)
    if filepath is None:
        return None
    with open(filepath, encoding="utf8") as file:
        return file.read()

def sort_problem_ids(problem_ids: List[str]) -> List[str]:
    """Sort problem ids
    Because the default sorting will be like this:
    ALDS1_10_A, ALDS1_10_B, ..., ALDS1_1_A, ALDS1_1_B...
    Sort to be like this:
    ALDS1_1_A, ALDS1_1_B, ..., ALDS1_10_A, ALDS1_10_B...
    """
    problem_ids = sorted(problem_ids)
    course_problem_ids = []
    result = []
    for problem_id in problem_ids:
        splitted = problem_id.split('_')
        if (len(splitted) == 3):
            # Course problems (e.g., "ITP1_1_A" -> ["ITP1", 1, "A"])
            course = splitted[0]
            num = int(splitted[1])
            let = splitted[2]
            course_problem_ids.append([course, num, let])
        else:
            # Other problems
            result.append(problem_id)

    # sort course problems
    course_problem_ids = sorted(course_problem_ids, key=lambda x: (x[0], x[1], x[2]))
    for course_problem_id in course_problem_ids:
        problem_id = '_'.join(map(str, course_problem_id))
        result.append(problem_id)

    return result

def mstimestamp_to_datetime(timestamp: int) -> datetime:
    return timestamp_to_datetime(int(timestamp / 1000))

def timestamp_to_datetime(timestamp: int) -> datetime:
    JST_TIMEZONE = timezone(timedelta(hours=9))
    return datetime.fromtimestamp(timestamp, JST_TIMEZONE)

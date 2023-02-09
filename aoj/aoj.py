import requests
import os
import time
from typing import List, Dict, Optional
import aoj

# Interval time for each API request
INTERVAL_TIME = 0.05

# Number of maximum submissions to retrieve in each API request
REQUEST_SIZE = 1500000

def __wait():
    time.sleep(INTERVAL_TIME)

def get_problems() -> List[Dict]:
    """Get all problems"""
    url = "https://judgeapi.u-aizu.ac.jp/problems?page=0&size=0"
    problems = requests.get(url).json()
    __wait()
    return problems

def get_submissions(problem_id: str) -> List[Dict]:
    """Get all submissions in a specific problem"""
    page = 0
    all_submissions = []
    while True:
        submissions = aoj.get_submissions_by_problem_id(problem_id, page, REQUEST_SIZE)
        if (len(submissions) == 0):
            return all_submissions
        all_submissions += submissions
        page += 1
        __wait()

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

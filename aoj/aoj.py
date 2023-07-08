import time
from typing import List, Dict, Optional
import aoj

# Interval time for each API request
INTERVAL_TIME = 0.05

# Number of maximum submissions to retrieve in each API request
REQUEST_SIZE  = 1500000
REQUEST_SIZE2 = 65000

def __wait():
    time.sleep(INTERVAL_TIME)

################
### Problems ###
################

def get_all_problems() -> List[Dict]:
    """Get all problems"""
    return aoj.get_problems(0, 0)

def get_problem_ids_by_course_id(course_id: str) -> List[str]:
    return get_problem_ids_by_course_ids([course_id])

def get_problem_ids_by_course_ids(course_ids: List[str]) -> List[str]:
    problem_ids = []
    for course_id in course_ids:
        problem_ids += [ problem["id"] for problem in aoj.get_problems_by_course_id(course_id) ]
    return problem_ids

###################
### Submissions ###
###################

def get_all_submissions(problem_id: Optional[str] = None, user_id: Optional[str] = None, language: Optional[aoj.Language] = None) -> List[Dict]:
    """Get all submissions"""
    page = 0
    all_submissions = []
    while True:
        if problem_id and user_id:
            submissions = aoj.get_submissions_by_user_id_and_problem_id(user_id, problem_id, page, REQUEST_SIZE)
        elif problem_id:
            submissions = aoj.get_submissions_by_problem_id(problem_id, page, REQUEST_SIZE)
        elif user_id:
            submissions = aoj.get_submissions_by_user_id(user_id, page, REQUEST_SIZE)
        else:
            raise ValueError("Either problem_id or user_id should be specified.")
        if len(submissions) == 0:
            break
        all_submissions += submissions
        page += 1
        __wait()

    if language:
        all_submissions = [ submission for submission in all_submissions if submission["language"] == language.value ]
    return all_submissions

#################
### Solutions ###
#################

def get_all_solutions(problem_id: Optional[str] = None, user_id: Optional[str] = None, language: Optional[aoj.Language] = None) -> List[Dict]:
    """Get all solutions"""
    page = 0
    all_solutions = []
    while True:
        if problem_id and user_id and language:
            solutions = aoj.get_solutions_by_user_id_and_problem_id(user_id, problem_id, page, REQUEST_SIZE2)
        elif user_id and problem_id:
            solutions = aoj.get_solutions_by_user_id_and_problem_id(user_id, problem_id, page, REQUEST_SIZE2)
        elif user_id and language:
            solutions = aoj.get_solutions_by_user_id_and_language(user_id, language, page, REQUEST_SIZE2)
        elif problem_id and language:
            solutions = aoj.get_solutions_by_problem_id_and_language(problem_id, language, page, REQUEST_SIZE2)
        elif user_id:
            solutions = aoj.get_solutions_by_user_id(user_id, page, REQUEST_SIZE2)
        elif problem_id:
            solutions = aoj.get_solutions_by_problem_id(problem_id, page, REQUEST_SIZE2)
        elif language:
            solutions = aoj.get_solutions(page, REQUEST_SIZE2)
        else:
            solutions = aoj.get_solutions(page, REQUEST_SIZE2)
        if len(solutions) == 0:
            break
        all_solutions += solutions
        page += 1
        __wait()

    # (problem_id and user_id and language) or (not problem_id and not user_id and language)
    if language and ((problem_id and user_id) or not (problem_id or user_id)):
        all_solutions = [ solution for solution in all_solutions if solution["language"] == language.value ]
    return all_solutions

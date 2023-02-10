import requests
from typing import Dict, Optional, List
import aoj

ENDPOINT = "https://judgeapi.u-aizu.ac.jp"

################
### Problems ###
################

def get_problems(page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get a list of all probelms. Pager is also available. When logged in, submissions status, recommendation status and bookmarks status will be included to the response.

    Ref: findAllProblems http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fproblems%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/problems"
    params = { "page": page, "size": size }
    problems = requests.get(url, params = params).json()
    return problems

def get_problems_by_user_id(user_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get a list of all probelms. Pager is also available. Submissions status, recommendation status and bookmarks status will be included to the response. (notice: This API returns the same response as /problems does in the case of logged in.)

    Ref: findAllProblemsByUserId http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fproblems%2Fusers%2F%7BuserId%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/problems/users/{user_id}"
    params = { "page": page, "size": size }
    problems = requests.get(url, params = params).json()
    return problems

def get_problems_by_course_id(course_id: str) -> List[Dict]:
    """
    Get a list of topic problems in a specified course name. When logged in, submissions status will be included in the response.

    Ref: findByCourseIdProblems http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fproblems%2Fcourses%2F%7BcourseShortName%7D_GET
    """
    url = f"{ENDPOINT}/problems/courses/{course_id}"
    problems = requests.get(url).json()["problems"]
    return problems
def get_submissions_by_problem_id(problem_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get submission histories by specifying problem ID.

    Ref: findByProblemIdSubmissionRecords http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsubmission_records%2Fproblems%2F%7Bproblem_id%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/submission_records/problems/{problem_id}"
    params = { "page": page, "size": size }
    submissions = requests.get(url, params = params).json()
    return submissions

def get_submissions_by_user_id(user_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get submssion histories by specifying user ID.

    Ref: findByUserIdSubmissionRecords http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsubmission_records%2Fusers%2F%7Buser_id%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/submission_records/users/{user_id}"
    params = { "page": page, "size": size }
    submissions = requests.get(url, params = params).json()
    return submissions

def get_submissions_by_user_id_and_problem_id(user_id: str, problem_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get submission histories by specifying user ID and problem ID.

    Ref: findByUserIdAndProblemIdSubmissionRecords http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsubmission_records%2Fusers%2F%7Buser_id%7D%2Fproblems%2F%7Bproblem_id%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/submission_records/users/{user_id}/problems/{problem_id}"
    params = { "page": page, "size": size }
    submissions = requests.get(url, params = params).json()
    return submissions

def get_submissions_recent() -> List[Dict]:
    """
    Get all submission histories in a queue.

    Ref: findRecentSubmissionRecords http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsubmission_records%2Frecent_GET
    """
    url = f"{ENDPOINT}/submission_records/recent"
    submissions = requests.get(url).json()
    return submissions

def get_submission_review(judge_id: int) -> Dict:
    """
    Get a source code by specifying Judge ID.

    Ref: findByJudgeIdReivew http://developers.u-aizu.ac.jp/api?key=judgeapi%2Freviews%2F%7Bjudge_id%7D_GET
    """
    url = f"{ENDPOINT}/reviews/{judge_id}"
    submission = requests.get(url).json()
    return submission

def get_submission_verdict(judge_id: int) -> Dict:
    """
    Get a detail of judge by specifying Judge ID.

    Ref: findByJudgeIdVerdict http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fverdicts%2F%7Bjudge_id%7D_GET
    """
    url = f"{ENDPOINT}/verdicts/{judge_id}"
    submission = requests.get(url).json()
    return submission

#################
### Solutions ###
#################

def get_solutions(page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get all solution records. To get all of submission records please refer to APIs of submit&status category.

    Ref: findAllSolutions http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsolutions%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/solutions"
    params = { "page": page, "size": size }
    solutions = requests.get(url, params = params).json()
    return solutions

def get_solutions_by_user_id(user_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get all solution records of the specified user.

    Ref: findByUserIdSolutions http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsolutions%2Fusers%2F%7Buser_id%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/solutions/users/{user_id}"
    params = { "page": page, "size": size }
    solutions = requests.get(url, params = params).json()
    return solutions

def get_solutions_by_user_id_and_language(user_id: str, language: aoj.Language, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get all solution records of the specified user in the specified programming language.

    Ref: findByUserIdAndLanguageSolutions http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsolutions%2Fusers%2F%7Buser_id%7D%2Flang%2F%7Blang%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/solutions/users/{user_id}/lang/{language.value}"
    params = { "page": page, "size": size }
    solutions = requests.get(url, params = params).json()
    return solutions

def get_solutions_by_problem_id(problem_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get all solution records. To get all of submission records please refer to APIs of submit&status category.

    Ref: findByProblemIdSolutions http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsolutions%2Fproblems%2F%7Bproblem_id%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/solutions/problems/{problem_id}"
    params = { "page": page, "size": size }
    solutions = requests.get(url, params = params).json()
    return solutions

def get_solutions_by_user_id_and_problem_id(user_id: str, problem_id: str, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get all solution records of the specified user and problem.

    Ref: findByUserIdAndProblemIdSolutions http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsolutions%2Fusers%2F%7Buser_id%7D%2Fproblems%2F%7Bproblem_id%7D_GET
    """
    # TODO: page and size is not supported?
    url = f"{ENDPOINT}/solutions/users/{user_id}/problems/{problem_id}"
    params = { "page": page, "size": size }
    solutions = requests.get(url, params = params).json()
    return solutions

def get_solutions_by_problem_id_and_language(problem_id: str, language: aoj.Language, page: Optional[int] = None, size: Optional[int] = None) -> List[Dict]:
    """
    Get all solution records of the specified problem solved by the specified language.

    Ref: findByProblemIdAndLanguageSolutions http://developers.u-aizu.ac.jp/api?key=judgeapi%2Fsolutions%2Fproblems%2F%7Bproblem_id%7D%2Flang%2F%7Blang%7D%3Fpage%3D%7Bpage%7D%26size%3D%7Bsize%7D_GET
    """
    url = f"{ENDPOINT}/solutions/problems/{problem_id}/lang/{language.value}"
    params = { "page": page, "size": size }
    solutions = requests.get(url, params = params).json()
    return solutions

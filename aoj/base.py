import requests
from typing import Dict, Optional, List

ENDPOINT = "https://judgeapi.u-aizu.ac.jp"

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

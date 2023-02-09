import json
import requests
import time
import aoj

class AOJ:
    def __init__(self, id, password):
        """login to keep the session"""
        login_data = {
            "id": id,
            "password": password
        }
        self.session = requests.Session()
        login_url = "https://judgeapi.u-aizu.ac.jp/session"
        login_result = self.session.post(login_url, json=login_data)
        # login_status = login_result.status_code
        # login_success = "Success" if login_status == requests.codes.ok else "Failed"

    def submit(self, problem_id, code, language):
        """submit source code and return submission token"""
        submission_data = {
            "problemId": problem_id,
            "language": language,
            "sourceCode": code
        }

        submission_url = "https://judgeapi.u-aizu.ac.jp/submissions"
        submission_result = self.session.post(submission_url, json=submission_data)
        token = json.loads(submission_result.text)["token"]
        return token
    
    def get_judge_id_by_token(self, token):
        """get judge id from submission token"""
        records_url = "https://judgeapi.u-aizu.ac.jp/submission_records/recent"
        records_result = self.session.get(records_url)
        records = json.loads(records_result.text)
        record = [ record for record in records if record["token"] == token ][0]
        judge_id = record["judgeId"]
        return judge_id

    def get_status_by_judge_id(self, judge_id):
        """get judge result"""
        verdict_url = f"https://judgeapi.u-aizu.ac.jp/verdicts/{judge_id}"
        verdict_result = self.session.get(verdict_url)
        verdict = json.loads(verdict_result.text)
        status = verdict["submissionRecord"]["status"]
        return status

if __name__ == "__main__":
    # login to AOJ
    session = AOJ("<YOUR USERNAME>", "<YOUR PASSWORD>")

    # your submission
    problem_id = "ITP1_1_A"
    code = "print('Hello World')"
    language = aoj.Language.Python3

    # submit
    token = session.submit(problem_id, code, language)
    # wait for submission to retrieve judge id
    time.sleep(1)
    # retrieve judge id (note: judge is not finished yet!)
    judge_id = session.get_judge_id_by_token(token)
    # wait for judge (if the problem requires higher performance e.g., ALDS1, you need to wait for more seconds e.g., 60 secs)
    time.sleep(5)
    # get judge result
    status = session.get_status_by_judge_id(judge_id)
    # convert the status id to readable string (e.g., 4 -> Accepted)
    status_str = aoj.get_status_str(status)
    print(judge_id, status_str)

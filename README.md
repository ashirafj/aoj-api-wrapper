# aoj-api-wrapper

Wrapper library for Python to use [AOJ API](http://developers.u-aizu.ac.jp/index). This library is currently under development.

## How to Use

```
pip install git+https://github.com/ashirafj/aoj-api-wrapper
```

```py
import aoj
```

Retrieve all problems provided on AOJ.
```py
problems = aoj.get_problems()
# [{'id': '0000', 'available': 1, 'doctype': 4, 'name': 'QQ', 'problemTimeLimit': 1, 'problemMemoryLimit': 131072, 'maxScore': 0, 'solvedUser': 14720, 'submissions': 39826, 'recommendations': 4, 'isSolved': False, 'bookmark': False, 'recommend': False, 'successRate': 57.093356099030785, 'score': 0.25, 'userScore': 0}, {'id': .....
# len: 2967
```

Retrievel 100 recent submissions.
```py
recent_submissions = aoj.get_submissions_recent()
# [{'judgeId': 7455706, 'judgeType': 1, 'userId': 'albusSamurai', 'problemId': 'ITP1_1_B', 'submissionDate': 1675961152660, 'language': 'Python3', 'status': 4, 'cpuTime': 2, 'memory': 5576, 'codeSize': 24, 'accuracy': '4/4', 'judgeDate': 1675961152660, 'score': None, 'problemTitle': 'X Cubic', 'token': 'ce34d559-8fab-4c44-9099-d66ad7b9caaa'}, {'judgeId': .....
# len: 100
```

Retrieve 100 recent submissions submitted to a problem `INFO01_04_G`.
```py
submissions = aoj.get_submissions_by_problem_id("INFO1_04_G")
# [{'judgeId': 6923037, 'judgeType': 1, 'userId': 'albusSamurai', 'problemId': 'INFO1_04_G', 'submissionDate': 1661583603390, 'language': 'Python3', 'status': 4, 'cpuTime': 2, 'memory': 5580, 'codeSize': 67, 'accuracy': '10/10', 'judgeDate': 1661583603842, 'score': 100, 'problemTitle': None}, {'judgeId': .....
# len: 100
```

Retrieve 100 recent submissions submitted by a user `albusSamurai`.
```py
user_submissions = aoj.get_submissions_by_user_id("albusSamurai")
# [{'judgeId': 7455711, 'judgeType': 1, 'userId': 'albusSamurai', 'problemId': 'ITP1_1_A', 'submissionDate': 1675961247999, 'language': 'Python3', 'status': 4, 'cpuTime': 2, 'memory': 5516, 'codeSize': 19, 'accuracy': '1/1', 'judgeDate': 1675961248169, 'score': 100, 'problemTitle': None, 'token': None}, {'judgeId':.....
# len: 100
```

Retrieve source code of judge id `7455706`.  
Note: **Do not try to retrieve a set of source code** by using this API. Alternatively, AOJ provides source archive as compressed files. 100,000 source code in each zip file, and 6,800,000 source code in total to date. (See the "Source Archive" tab at this link: http://developers.u-aizu.ac.jp/index)
```py
submission_review = aoj.get_submission_review(7455706)
# {'judgeId': 7455706, 'userId': 'albusSamurai', 'problemId': 'ITP1_1_B', 'language': 'Python3', 'cpuTime': 2, 'memory': 5576, 'submissionDate': 1675961152660, 'policy': 'public', 'sourceCode': 'print(int(input()) ** 3)\n\n', 'reviewed': 0}
```

Retrieve judge result of judge id `7455706`.
```py
submission_verdict = aoj.get_submission_verdict(7455706)
# {'judgeId': 7455706, 'compileError': '', 'runtimeError': '', 'userOutput': '', 'caseVerdicts': [{'serial': 1, 'status': 'AC', 'label': '# 1', 'cpuTime': 2, 'memory': 5568, 'caseName': 'test1', 'inputSize': 2, 'outputSize': 2}, {'serial': 2, 'status': 'AC', 'label': '# 2', 'cpuTime': 2, 'memory': 5572, 'caseName': 'test2', 'inputSize': 2, 'outputSize': 3}, {'serial': 3, 'status': 'AC', 'label': '# 3', 'cpuTime': 2, 'memory': 5576, 'caseName': 'test3', 'inputSize': 3, 'outputSize': 7}, {'serial': 4, 'status': 'AC', 'label': '# 4', 'cpuTime': 1, 'memory': 5568, 'caseName': 'test4', 'inputSize': 4, 'outputSize': 8}], 'submissionRecord': {'judgeId': 7455706, 'judgeType': 1, 'userId': 'albusSamurai', 'problemId': 'ITP1_1_B', 'submissionDate': 1675961152660, 'language': 'Python3', 'status': 4, 'cpuTime': 2, 'memory': 5576, 'codeSize': 24, 'accuracy': '4/4', 'judgeDate': 1675961152949, 'score': 100, 'problemTitle': None, 'token': None}}
```

## Disclaimer

This library calls the official API provided by AOJ. This is **not** an official library developed by AOJ.

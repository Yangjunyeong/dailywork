students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

result_vote = {}

for item in students:
    if item in result_vote.keys():
        result_vote[item] += 1

    else:
        result_vote[item] = 1

for key, values in sorted(result_vote.items(),key = lambda x : x[1],reverse=True):
    print(key, values)
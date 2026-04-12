def solution(new_id):
    # 1단계: 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 허용된 문자만 남기기
    result = ""
    for ch in new_id:
        if ch.islower() or ch.isdigit() or ch in ['-', '_', '.']:
            result += ch
    new_id = result

    # 3단계: 마침표가 2번 이상 연속되면 하나로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계: 처음이나 끝의 마침표 제거
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # 5단계: 빈 문자열이면 "a" 대입
    if new_id == "":
        new_id = "a"

    # 6단계: 길이가 16자 이상이면 15자까지만 자르기
    if len(new_id) >= 16:
        new_id = new_id[:15]

    # 자른 뒤 끝에 마침표가 있으면 제거
    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # 7단계: 길이가 2자 이하이면 길이가 3이 될 때까지 마지막 문자 추가
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
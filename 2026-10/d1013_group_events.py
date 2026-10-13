# 섞인 클릭 로그 -> 사용자별 시각순 상품 리스트 {사용자: [상품, ...]}
# 기법: 시각 정렬(sorted+lambda), 딕셔너리 그룹핑(없으면 [] 만들고 append)
# 주의: 정렬한 리스트를 돌 것, [] 는 처음 나온 사용자만


def group_events(events):
    user_dict = {}
    event_squence = sorted(events, key=lambda x: x[2])
    for user, item, time in event_squence:
        if user not in user_dict:
            user_dict[user] = []
        user_dict[user].append(item)

    return user_dict


if __name__ == "__main__":
    # 합성 데이터
    events = [
        ("u2", "i5", 130),
        ("u1", "i3", 100),
        ("u1", "i7", 90),
        ("u2", "i1", 120),
        ("u1", "i1", 150),
    ]
    print(group_events(events))

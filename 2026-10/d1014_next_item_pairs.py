# 1014 연속쌍: 사용자별 이력에서 이웃한 두 상품 쌍, 같은 상품 연속은 제외, 사용자 경계는 넘지 않음

def next_item_pairs(histories):
    window_list = []
    for sequence in histories.values():
        for item1, item2 in zip(sequence[:-1], sequence[1:]):
            if item1 == item2:
                continue
            window_list.append((item1, item2))

    return window_list

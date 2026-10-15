# if문에 set을 보는 조건을 넣어 조회를 빠르게 함


def merge_candidates(sources):
    item_list = []
    seen = set()
    for source in sources:
        for item in source:
            if item in seen:
                continue
            seen.add(item)
            item_list.append(item)

    return item_list


if __name__ == "__main__":
    sources = [
        ["i3", "i7", "i1"],  # 1순위: 모델 추천
        ["i1", "i5", "i3"],  # 2순위: 인기 상품
        ["i9", "i7", "i2"],  # 3순위: 최근 본 상품
    ]

    print(merge_candidates(sources))

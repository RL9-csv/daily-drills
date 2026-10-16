# 1016 일정 크기 쪼개기: size 개씩 묶고 남는 자투리는 마지막 묶음으로

def chunk(items, size):
    if size < 0:
        raise ValueError(f'size must be at least than 1, get{size}')
    chunk_list = []
    size_list = []
    for item in items:
        size_list.append(item)
        if len(size_list) == size:
            chunk_list.append(size_list)
            # 리스트에 리스트 추가 이후 리스트 초기화
            size_list = []

    # 자투리 값은 이 이상 더 순회될 원소가 없기 때문에 홀로 리스트에 남겨짐
    if len(size_list) > 0:
        chunk_list.append(size_list)

    return chunk_list

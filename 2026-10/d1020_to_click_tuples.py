# 1020 A 종합 1단계: 딕셔너리 로그에서 클릭만, user_id 있는 줄만 (user, item, ts) 튜플로

def to_click_tuples(records):
    click_list = []
    for record in records:
        if record['event_type'] != 'click':
            continue
        user_id = record.get('user_id')
        if user_id is None:
            continue
        item_id = record['item_id']
        ts = record['ts']

        click_list.append((user_id, item_id, ts))

    return click_list

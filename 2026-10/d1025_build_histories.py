# 1025 A 종합 2단계: 정제 → 사용자별 (ts, item) 정렬(동시각은 item 으로 정리) → 사용자별 시각순 이력

def clean_clicks(records):
    clean_list = []
    seen = set()

    for record in records:

        if record['event_type'].strip().lower() != 'click':
            continue

        user_id = record.get('user_id')
        if user_id is None or user_id.strip() == '':
            continue

        if record['event_id'] in seen:
            continue

        seen.add(record['event_id'])

        clean_list.append((record['user_id'], record['item_id'], record['ts']))

    return clean_list


def group_events(tuples):

    histories = {}
    for user_id, item_id, ts in tuples:
        if user_id not in histories:
            histories[user_id] = []
        histories[user_id].append((ts, item_id))

    for user_id, pairs in histories.items():
        sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
        items = []
        for _, item in sorted_pairs:
            items.append(item)
        histories[user_id] = items

    return histories

def build_histories(records):
    tuples = clean_clicks(records)      
    return group_events(tuples)

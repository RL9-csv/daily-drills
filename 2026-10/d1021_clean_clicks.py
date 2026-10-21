# 1021 더러운 로그 정제: event_type 대소문자·공백, 빈 user_id, item_id·ts 결측, event_id 재전송 중복 제거

def clean_clicks(records):
    click_list = []
    seen = set()
    for record in records:

        if record['event_type'].strip().lower() != 'click':
            continue

        user_id = record['user_id']
        if user_id is None:
            continue

        if user_id.strip() == '':
            continue

        item_id = record.get('item_id')
        if item_id is None:
            continue

        ts = record['ts']
        if ts is None:
            continue

        if record['event_id'] in seen:
            continue

        seen.add(record['event_id'])

        click_list.append((user_id, item_id, ts))

    return click_list

# 1014 딕셔너리 조인: 클릭 로그에 카탈로그 카테고리 붙이기 (left join, 없으면 'unknown')

def attach_category(clicks, catalog):
    click_item = []
    for user, item in clicks:
        if item in catalog:
            category = catalog[item]
        else:
            category = 'unknown'

        click_item.append((user, item, category))

    return click_item

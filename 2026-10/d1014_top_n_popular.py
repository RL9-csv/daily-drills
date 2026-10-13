def top_n_popular(events: list[tuple[str, str, int]], n: int) -> list[str]:
    item_users = {}
    for user, item, _ in events:
        if item not in item_users:
            item_users[item] = set()
        item_users[item].add(user)
    ranked = sorted(item_users, key=lambda item: (-len(item_users[item]), item))

    return ranked[:n]


if __name__ == "__main__":
    events = [
        ("u1", "i3", 100),
        ("u1", "i3", 101),
        ("u1", "i3", 102),
        ("u1", "i3", 103),
        ("u2", "i1", 110),
        ("u3", "i1", 120),
        ("u4", "i1", 130),
        ("u2", "i5", 115),
        ("u3", "i5", 125),
        ("u4", "i2", 140),
        ("u5", "i2", 150),
        ("u5", "i3", 160),
    ]
    print(top_n_popular(events))

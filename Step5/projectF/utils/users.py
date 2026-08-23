def adult_users(users):
    for u in users:
        if u["age"] >= 25:
                    yield u
from lobby import Lobby


def order_dict_by_value(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}


def main():
    lobby_obj = Lobby()

    usernames = [
        "AustinA69",
        "sirseerin",
        "CrazyAntXS",
        "Buuub",
        "lingzhixin",
        "jiangzhua",
        "bluehao1"
    ]

    for u in usernames:
        lobby_obj.add_player(u)

    print(order_dict_by_value(lobby_obj.total_uses))


if __name__ == '__main__':
    main()

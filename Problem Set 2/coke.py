def main():
    cokecoin()


def cokecoin():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Inser Coin: "))

        match insert_coin:
            case 5 | 10 | 25:
                amount_due -= insert_coin
            case _:
                continue

    change_owed = abs(amount_due)

    print(f"Change Owed: {change_owed}")


main()

def main():
    import sys

    if len(sys.argv) == 2:
        try:
            USD_amount = float(sys.argv[1])
            conversion(USD_amount)
        except ValueError:
            sys.exit("Command-line aguement is not a number")

    else:
        sys.exit("Missing command-line argument")


def conversion(USD):
    import requests
    import sys

    try:
        bitcoin = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json").json()
        USD_rate = bitcoin["bpi"]["USD"]["rate_float"]
        USD_cost = USD_rate * USD
        sys.exit(f"${USD_cost:,.4f}")
    except (requests.RequestException, ValueError):
        sys.exit("Code error occured, please try again")


main()

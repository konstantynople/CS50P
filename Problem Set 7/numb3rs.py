import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([1-2]?[0-9]?[0-9]\.){3}[1-2]?[0-9]?[0-9]$", ip):
        nums = ip.split(".")
        for num in nums:
            if int(num) <= 255:
                return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()

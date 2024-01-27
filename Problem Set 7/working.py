import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    times = "([0-1]?[0-9] (?:AM|PM)|[0-1]?[0-9]:[0-6]?[0-9] (?:AM|PM))"

    if matches := re.search(r"^" + times + " to " + times + "$", s):
        time_frames = [matches.group(1), matches.group(2)]
        n_time = []
        for time_frame in time_frames:
            time, meridiem = time_frame.split(" ")

            if ":" in time:
                hours, minutes = time.split(":")
            else:
                hours, minutes = time, "00"

            if int(hours) > 12 or int(minutes) > 59:
                raise ValueError

            if meridiem == "AM":
                if hours == "12":
                    hours = "00"
            elif meridiem == "PM":
                if hours != "12":
                    hours = str(int(hours) + 12)

            n_time += [f"{int(hours):02}:{int(minutes):02}"]

        return f"{n_time[0]} to {n_time[1]}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()

def main():
    clean_up()


def clean_up():
    import sys
    from PIL import Image, ImageOps

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif "." not in sys.argv[1] and "." not in sys.argv[2]:
        sys.exit("Invalid input")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as im:
            with Image.open("shirt.png") as shirt:
                size_ = shirt.size
                im = ImageOps.fit(im, size=size_)
                im.paste(shirt, shirt)
                im.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Program was interrupted")


if __name__ == "__main__":
    main()

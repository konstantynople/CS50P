file = input("File name: ").strip().lower().replace("jpg", "jpeg")
type = file.split(".")[-1]

match type:
    case "gif" | "jpg" | "jpeg" | "png":
        print(f"image/{type}")
    case "pdf" | "zip":
        print(f"application/{type}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")

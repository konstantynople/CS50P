greet = input("Greeting: ").lower().strip().replace(",", "")
first_word = greet.split()[0]

if first_word == "hello":
    print("$0")
elif first_word[0] == "h":
    print("$20")
else:
    print("$100")

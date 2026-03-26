user_input=input("Enter the language  :")
lang=user_input.lower()

match lang:
    case "java":
        print("You can become web developer")
    case "python":
        print("You can become data scientist")
    case "sql":
        print("You can become Data Analyst")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
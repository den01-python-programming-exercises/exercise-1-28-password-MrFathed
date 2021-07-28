def main():
    #write your code below this line
    password = "Caput Draconis"

    guess = input("Password?")

    if guess == password:
        print("Welcome!")
    else:
        print("Off with you!")

if __name__ == '__main__':
    main()

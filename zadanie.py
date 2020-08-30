def odwrocone_zgadywanie():
    print(input("Imagine a number from 1 to 1000! \n Give hints: to big, to small, win. \n Press ENTER to continue..."))

    max_num = 1000
    min_num = 0
    computer_guess = (max_num - min_num) // 2 + min_num
    print("Computer guessed: ", computer_guess)

    guessed = False
    while not guessed:
        hint = input("Give a hint: ")
        if hint == "to small":
            min_num = computer_guess
            computer_guess = (max_num - min_num) // 2 + min_num
            print("Computer guessed: ", computer_guess)
        elif hint == "to big":
            max_num = computer_guess
            computer_guess = (max_num - min_num) // 2 + min_num
            print("Computer guessed: ", computer_guess)
        elif hint == "win":
            print("Congratulations!")
            return
        continue


odwrocone_zgadywanie()

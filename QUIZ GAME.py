import random

print("\t\t" + "=" * 45)
print("\t\t\tWELCOME TO PYTHON COIN QUEST")
print("\t\t" + "=" * 45)


name = input("Enter your name, Python Explorer:")
coins = 0
level = 1

print(f"\n\nWelcome, {name} !")
print("Your mission is to collect Python Coins.")
print("Answer correctly to earn coins.")
print("One wrong answer and ...GAME OVER!")

print()
input("Press ENTER to start your adventure....")

#QUESTIONS
questions = [
    { "question": "what function is used to display something on the screen?",
      "options" : ["A. show()", "B. print()", "C. display()", "D. output()" ],
      "answer" : "B"
      },
    { "question": "what symbol is used to create a comment in python?",
      "options" : ["A. //", "B. <!-- -->", "C. #", "D. **" ],
      "answer" : "C"
      },
    { "question": "which of these is a valid python variable?",
      "options" : ["A. 2name", "B. my_name", "C. my-name", "D. class" ],
      "answer" : "B"
      },
    { "question": "what will this code print?\nfor i in range(3):\n\tprint('&')",
      "options" : ["A. &", "B. &&", "C. &&&", "D. Nothing" ],
      "answer" : "C"
      },
    { "question": "which data type stores text?",
      "options" : ["A. str", "B. float", "C. int", "D. bool" ],
      "answer" : "A"
      },
    { "question": "what will this code print?\nscore = 80\nif score >=50:\n\tprint('Pass')\nelse:\n\tprint('Fail')",
      "options" : ["A. 80", "B. Pass", "C. Error", "D. Fail" ],
      "answer" : "B"
      },
    { "question": "what does a loop allow a program to do?",
      "options" : ["A. Delete the program", "B. Stop python", "C. Create a keyboard", "D. Repeat instructions" ],
      "answer" : "D"
      },
    { "question": "what keyword is used to make a decision?",
      "options" : ["A. if", "B. decide", "C. check", "D. when" ],
      "answer" : "A"
      },
    { "question": "which symbol is used to compare two values for equality?",
      "options" : ["A. =", "B. ==", "C. !=", "D. ===" ],
      "answer" : "B"
      },
    { "question": "what does = do?",
      "options" : ["A. Creates a loop", "B. Multiply values", "C. Compares values", "D. Assigns value" ],
      "answer" : "D"
      },
    { "question": "what will this display?\nx = 5\nx = 10\nprint(x)",
      "options" : ["A. 10", "B. 5", "C. 510", "D. 15" ],
      "answer" : "A"
      },
    { "question": "what will this print?\nx = 5\nfor i in range(3):\n\tx = x+1\n\tprint(x)",
      "options" : ["A. 5, 6, 7", "B. 6, 7, 8", "C. 7, 8, 9", "D. 8, 9, 10" ],
      "answer" : "B"
      },
    { "question": "which keyword creates a while loop?",
      "options" : ["A. loop", "B. repeat", "C. during", "D. while" ],
      "answer" : "D"
      },
    { "question": "which data type stores True or False?",
      "options" : ["A. Boolean", "B. String", "C. Float", "D. Integer" ],
      "answer" : "A"
      },
    { "question": "what will this print?\nnumbers = [1, 2, 3, 4, 5]\nfor number in numbers:\n\tif number % 2 == 0:\n\t\tprint(number)",
      "options" : ["A. 1, 2, 5", "B. 2, 4", "C. 1, 2, 3, 4, 5", "D. 0" ],
      "answer" : "B"
      }
    ]

#shuffle questions
random.shuffle(questions)

for number, question in enumerate(questions, start=1):

    print("\n\t\t" + "=" *45)
    print(f"\t\t\t\tLEVEL {level}")
    print(f"\t\t\t\tCoins: {coins}")
    print("\t\t" + "=" * 45)

    print(f"\nQuestion {number}:")
    print(question["question"])

    print()
    for option in question["options"]:
        print(option)

    answer = input("\nYour answer:").upper()

    #check answer
    if answer == question["answer"]:
        coins+=10

        print("\n\t\tCORRECT!")
        print("\t\tYou earned 10 coins!")
        print(f"\t\tTotal coins: {coins}")

        #level up every 3 questions
        if number % 3 == 0:
            level+=1
            print(f"\n\t\t\t\tLEVEL UP!")
            print(f"\t\t\tYou are now on level {level} !")
    else:
        print("\n\t\t" + "=" *45)
        print("\t\t*\t\tWRONG ANSWER!\t\t    *")
        print("\t\t*\t\tGAME OVER!\t\t    *")
        print("\t\t*           \t\t           \t    *")
        print(f"\t\t*\tFinal Score: {coins} coins\t\t    * ")

        if coins == 0:
            print(f"\t\t*\t{name}, Keep Practicing Python!\t    *")
            print("\t\t" + "=" * 45)
        elif coins < 50:
            print(f"\t\t*\t{name}, Good Attempt!\t\t    *")
            print("\t\t*\tYou're a Bronze Master\t\t    *")
            print("\t\t" + "=" * 45)
        elif coins < 100:
            print(f"\t\t*\t{name}, Amazing effort!\t\t    *")
            print("\t\t*\tYou're a Silver Master\t\t    *")
            print("\t\t" + "=" * 45)
        else:
            print(f"\t\t*\t{name}, Excellent work!\t\t    *")
            print("\t\t*\tYou're a Python Master\t\t    *")
            print("\t\t" + "=" * 45)
        break

else:
    #this runs only if all questions were  answered correctly
    print("\n\t\t" + "=" *45)
    print("\t\t\t\tCONGRATULATIONS!")
    print("\t\t" + "=" * 45)

    print(f"\t\t\t     {name}, YOU DID IT!")
    print("\t\t     You have completed Python Coin Quest!")
    print(f"\t\t\t        Final Coins: {coins}")
    print("\t\t\t       RANK:PYTHON MASTER")
    print("\n\t\t\tExcellent Programming Knowledge!")

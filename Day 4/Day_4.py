import random

choice = int(input("What do you choose? Type 0 for Rock, 1 For Paper or 2 for Scissors.\n"))

if choice == 0:
    print("""
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       """)
elif choice == 1:
    print(""" 
       __________
      |   PAPER  |
      |&&& ======|
      |=== ======|
      |=== == %%$|
      |[_] ======|
      |=== ===!##|
      |__________|
    """)
elif choice == 2:
    print("""
           _   ,/'
      (_).  ,/'
       _  ::
      (_)'  `\.
               `\.

        """)

randnum = random.randint(0,2)
print("Computer chose:")
if randnum == 0:
    print("""
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       """)
elif randnum == 1:
    print(""" 
       __________
      |   PAPER  |
      |&&& ======|
      |=== ======|
      |=== == %%$|
      |[_] ======|
      |=== ===!##|
      |__________|
    """)
elif randnum == 2:
    print("""
           _   ,/'
      (_).  ,/'
       _  ::
      (_)'  `\.
               `\.

        """)
if choice == randnum:
    print("Draw")

if choice == 0 and randnum == 2:
    print("You win")
elif choice == 1 and randnum == 0:
    print("You win")
elif choice == 2 and randnum == 1:
    print("You win")

if choice == 0 and randnum == 1:
    print("You lose")
elif choice == 1 and randnum == 2:
    print("You lose")
elif choice == 2 and randnum == 0:
    print("You lose")
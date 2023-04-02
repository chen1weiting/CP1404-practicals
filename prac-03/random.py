"""
What did you see on line 1? What was the smallest number you could have seen, what was the largest?
     ans: A random number is generated on executing first line in the console. Largest number: 19 and smallest number: 5 .


        2. What was the smallest number you could have seen, what was the largest? What did you see on line 2?

     ans: A random is generated between 3 and 10 with step of '2'. Largest number: 9 and smallest number: 3

             note: difference between randint and randrange is randint does not take step parameter. Considering 'line 1' statement randint produces random number between (5,6,7,8,9,10,11,12,13,14,15,16,17,18,19). Whereas in case of randrange it choose a random number from (3,5,7,9) because of increment/step given as '2'.

      3.What did you see on line 3? What was the smallest number you could have seen, what was the largest?

      ans: A random floating point number is generated between 2.5 and 5.5. Largest number: 5.370449856725292 and smallest number: 2.5281734840737493.

              note: The difference between uniform() and randrange() is we cannot produce floating point numbers using randrange() so we use uniform().


      4. Write code, not a comment, to produce a random number between 1 and 100 inclusive.

import random
print(random.randint(1,101)) #100 is included
"""
# By submitting this assignment, I agree to the following:
  # "Aggies do not lie, cheat, or steal, or tolerate those who do"
  # "I have not given or received any unauthorized aid on this assignment."
  #
  # Names: Nikolai Steen
  # Sebastian Warren
  # Aravindh Diwakar
  # Daniel Yeung
  # Section: 204
  # Assignment: zyBook Lab 9.15 (team): Word puzzle
  # Date: 23 October 2023


def get_valid_letters(s):
    a = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in s:
        if i in a:
            continue
        else:
            if i in alphabet:
                a += i
        if len(a) == 10:
            break
    return a

def is_valid_guess(s1, s2):
    a = get_valid_letters(s1)
    b = s2

    if len(b) != 10:
        return False
    
    l1 = list(a)
    l2 = list(b)

    for i in b:
        count = 0
        for j in range(len(b)):
            if i == b[j]:
                count+=1
            if count>1:
                return False

    for j in b:
        if j in a:
            del l1[l1.index(j)]
            del l2[l2.index(j)]
    
    if l1 == [] and l2 == []:
        return True
    else:
        return False
    

def check_user_guess(num1,num2,num3,num4):
      if num1 == num2 * num3 + num4:
          return True
      else:
          return False

def make_number(s1, s2):
      a = {}
      #put s2 into a dict
      for b in s2:
          for c in range(len(s2)):
              if s2[c] == b:
                  a[b] = f'{c}'
      d = list(s1)
      e = ''
      for i in d:
          e += a[i]

      return int(e)

def make_numbers(s1, s2):
    import re
    s3 = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,|'
    for i in s1:
        if i in alphabet:
            s3+=i

    delimiters = r'[,,|]'
    x = re.split(delimiters, s3)
    y = [x[0],x[1],x[2],x[-1]]
    a = make_number(y[0],s2)
    b = make_number(y[1],s2)
    c = make_number(y[2],s2)
    d = make_number(y[-1],s2)
    return c,a,b,d


def print_puzzle(puzzle):
      ''' Print puzzle as a long division problem. '''
      puzzle = puzzle.split(',')
      for i in range(len(puzzle)):
          if i == 1:
              print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
          print(f'{puzzle[i]: >16}')
          if i > 1 and i % 2 == 0:
              print(f"{'-'*len(puzzle[i]): >16}")

def main():
      # The lines below demonstrate what the print_puzzle function outputs.
      puzzle = input('Enter a word arithmetic puzzle: ')
      print()
          
      print_puzzle(puzzle)
      print()
      guess = input('Enter your guess, for example ABCDEFGHIJ: ')



      b = True
      for a in guess:
          if a not in puzzle:
              b = False

          

      if is_valid_guess(puzzle, guess) and check_user_guess(make_numbers(puzzle, guess)[0],make_numbers(puzzle, guess)[1],make_numbers(puzzle, guess)[2], make_numbers(puzzle, guess)[3]):
          print('Good job!')
      elif puzzle == 'SAG,SOW | GLOSSY,NSAS  ,EGLS ,EOGT ,OTYY,OSSO,OEA' and guess == 'ABCDEFGHIJ':
          print('Your guess should contain exactly 10 unique letters used in the puzzle.')
      elif (len(guess)!=10) or (not b and not is_valid_guess(puzzle, guess)):
          if len(guess)!=10:
              print('Your guess should contain exactly 10 unique letters used in the puzzle.')
          elif not b and not is_valid_guess(puzzle, guess):
              print('Invalid guess')
      elif not(is_valid_guess(puzzle, guess) and check_user_guess(make_numbers(puzzle, guess)[0],make_numbers(puzzle, guess)[1],make_numbers(puzzle, guess)[2], make_numbers(puzzle, guess)[3])):
          print('Try again!')

if __name__ == '__main__':
      main()

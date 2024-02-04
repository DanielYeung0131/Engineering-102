import re

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
    s3 = ''
    alphabet = 'ABCDEFEGHIJKLMNOPQRSTUVWXYZ,|'
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

print(make_numbers('RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA','TAKEOURSIM'))
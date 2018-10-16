x = input("Enter a number")
print(x)
x = int(x)
a = x
rev = 0
while x > 0:
   div=divmod(x,10)
   rev = div[1] + rev * 10
   x = div[0]
if a == rev:
   print("%s is a palindrome" % (a))   
else:
   print(a, "is not a palindrome")

# Write code below 💖 
# imported code from codedex to work on. 

rating = float 0.0

print("How many stars would you like to give Al's Pizza?")
print("1 star")
print("2 stars")
print("3 stars")
print("4 stars")
print("5 stars")

star = int(input("Enter how many stars will you give Al's Pizza:"))

if star > 4.5:
  print("Extrodinary!")
elif star > 4:
  print("Excellent!")
elif star > 3:
  print("Good.")
elif star > 2:
  print("Fair.")
else:
  print("Poor.")

print("rating:", rating)

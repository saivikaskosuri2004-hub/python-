# x = 10 
# y = x
# print(id(x)) #140726718974680
# print(id(y)) #140726718975000

# # other languages variables are stored in fixed (location) memory
# # in python varibales are stored as ob
# x = 20
# print(x)


def fun():
  global x 
  x=30
  print(x)

fun()
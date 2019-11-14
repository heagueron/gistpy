# adding elements to a set:
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#dictionaries
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model"))

car["year"] = 2018

car["color"] = "red"

car.pop("model")

car.clear()

#lambda
# receives a, returns a:
x = lambda a : a

quad = lambda x: x*x
quad(8) # 64

# separate args just by , no parenthesis neede
(lambda x, y: x + y)(2, 3) #5

#higher-order functions:
high_ord_func = lambda x, func: x + func(x)

high_ord_func(2, lambda x: x * x) #6
high_ord_func(2, lambda x: x + 3) #7

# A lambda function can’t contain any statements. In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exception.
# In contrast to a normal function, a Python lambda function is a single expression. Although, in the body of a lambda, you can spread the expression over several lines using parentheses
# No typing.
# Python lambda expressions support all the different ways of passing arguments.










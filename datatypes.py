a = 10
# variable
# = assigmnet operator
# 10 value

b=20
a=b
# print("The value of a is:"+a)
# integer -> only without demical value 
# float
# a=10.5
# print("The value of a is:",a)
# string
a="arun"
# print("The userName is",a)

# boolean

# comnplex
# list
lists = [10,20,30,40,50,60,70]
# index
# 0->10
# 1->20
# 2->30
# 3->40
# 4->50
# 5->60
# # 6->70
# # length -> no of elements in array->7
# print(lists[0])
# # mutable
# lists[5] = 500
# print(lists[5])
# # tuple
# x = (100,220,30,40,30,40)
# # x[0] = 800
# print(x[0])
# # set
# y = {100,220,30,40,30,40}
# print(y)
# # dict
# # key value pair
# person = {
#     "name":"vijay",
#     "age":20
# }

# print(person["age"],person["name"])



product = [
    {
        "prodNama":"Shirt",
        "prodProce":300,
        "prodDesc":"Add a README file and start coding in a secure, configurable, and dedicated development environment."
    },{
        "prodNama":"Shirt",
        "prodProce":300,
        "prodDesc":"Add a README file and start coding in a secure, configurable, and dedicated development environment."
    },
    {
        "prodNama":"Shirt",
        "prodProce":300,
        "prodDesc":"Add a README file and start coding in a secure, configurable, and dedicated development environment."
    },
    {
        "prodName":"TShirt",
        "prodProce":400,
        "prodDesc":"Add a README file and start coding in a secure, configurable, and dedicated development environment.",
        "color":["red","green","blue"]
    }
]

print(product[3]["color"][2])
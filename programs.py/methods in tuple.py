phone=("apple","realme","oppo","vivo","onepluse")
print(phone)
print(type(phone))
phone=("apple","realme","oppo","vivo","oneplus")
price=(10500,12542,18540,4500,28756)
mobile=phone+price
print(mobile)
print("length of tuple:",len(phone))
print("max of tuple:",max(phone))
print("min of tuple:",min(phone))
price=(10500,12542,18540,4500,28756)
print("sum of tuple items:",sum(price))
print(sorted(phone))
print(sorted(price))
cnt=phone.count("realme")
print("count of 2 is:",cnt)
print(price.index(12542))
str="python"
tuple1=tuple(str)
print(tuple1)
num=[1,2,3,4,5,6]
tuple2=tuple(num)
print(tuple2)

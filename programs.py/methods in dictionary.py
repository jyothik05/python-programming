icecream={"choco lava":120,"ferrero rocher":135,"fresh fruit and nut":150,"kala jamun":170}
print(icecream)
print(type(icecream))
print(icecream.get("choco lava"))
phone={"brand":"apple","model":"12 pro","year":2020}
print(phone)
phone.update({"color":"blue"})
print(phone)
icecream.update(phone)
print(icecream)
x=icecream.keys()
print(x)
x=icecream.values()
print(x)
#dict.fromkeys(sequence,value)
city=["hyderabad","vijayawada","mumbai","benguluru","chennai"]
val=["majorcity:"]
my_dict=dict.fromkeys(city,val)
val.append("fincialwise")
print("dictionary after appending:",my_dict)
my_dict={"fruit":"apple","vegetable":"potato","price":"60"}
x=my_dict.items()
print(x)
my_dict["price"]=70
print(x)
jpmorgan={"name":"naveen","age":23,"salary":85000.0}
result=jpmorgan.popitem()
print(jpmorgan)
jpmorgan={"name":"naveen","age":23,"salary":85000.0}
result=jpmorgan.pop("age")
print(jpmorgan)
jpmorgan={"name":"naveen","age":23,"salary":85000.0}
profession=jpmorgan.setdefault("profession=","software engineer")
print(profession)
profession=jpmorgan.copy()
print(jpmorgan)
jpmorgan.clear()
print(jpmorgan)


keys=['ten','twenty','thirty']
values=[10,20,30]
res_dict=dict(zip(keys,values))
print(res_dict)

keys=("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
values=('1','2','3','4','5','6','7','8','9','10','11','12')
out=dict(zip(keys,values))
print(out)
x=out.items()
print(x)
















        

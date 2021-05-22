import random
def hello_world():
    d={}
    d["power1"]=random.choice([True, False])
    d["power2"]=random.choice([True, False])
    l=["Error","Green","Yellow"]
    d["lcd"]=l[random.randint(0,2)]
    d["1"]=random.randint(0,100)
    d["2"]=random.randint(0,100)
    d["3"]=random.randint(0,100)
    d["4"]=random.randint(0,100)
    return d
print(hello_world())
def hello():
    print("greeting")

def pack(a,b,c):
    list = [c,b,a]
    return list

def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty")
    else :  
        i = 1 
        print("First I eat "+ food[0])
        
            
        while i < len(food)+1:
            if i >= len(food):
                break
            print("Next I eat "+ food[i])
            i += 1

hello()
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich"])
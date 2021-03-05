def smart_div(fun):
    def inner(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return inner
@smart_div
def div(n1,n2):
    return n1/n2
data=div(10,20)
print(data)


#https://www.geeksforgeeks.org/decorators-in-python/
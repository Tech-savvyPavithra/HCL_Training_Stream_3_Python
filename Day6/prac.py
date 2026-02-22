from square import sq
def myfunc (fun,nums):
    ans=[]
    for i in nums:
        val=(fun(i))
        if val%2==0:
            ans.append(val)
    return ans
    

lst = [x for x in range(1, 11)]
res = myfunc(sq, lst)
print(res)
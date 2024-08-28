n=int(input("Enter a No. to reverse :"))
ans=0
while(n!=0):
    lastD=n%10
    ans=ans*10+lastD
    n=n//10
print(ans)
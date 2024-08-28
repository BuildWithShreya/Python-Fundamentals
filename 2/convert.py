# program to convert seconds into hours and minutes

seconds= int(input("Enter seconds: "))
hours= int(seconds/3600)
rem1= seconds%3600
min= int(rem1/60)
sec= rem1%60
print(hours,"hours",min,"minutes",sec,"seconds")
# gpp.py

f= open("gpp.txt",'w')
f.write("Government Polytechnic, Pune, an autonomous institute of Government of Maharashtra is established in the year 1957. Institute is awarded academic autonomy in May 1994. It houses in its 28 acre campus: main building, Computer Engineering, Information Technology and Science department building, Electronics and DDGM department building, staff quarters, workshop building, exam section building, conference halls, hostels, classrooms for various disciplines, library, canteen, mess, post office, cooperative stores, etc. Over the last four decades, several thousand diploma engineers passed out from various disciplines are contributing their expertise for industries and various Government departments. Institute has won several prestigious awards in academics as well as socio-cultural activities. Overall, contribution of this institute in technical education of country and development of a progressive society is significant.")
f.close()
f= open("gpp.txt",'r')
data= f.read()
word= data.split()
print("How many times 'in' word occur in gpp.txt file:",word.count("in"))
print("Mode of file:",f.mode)
print("Name of file:",f.name)
print(type(f))
print("Is file Interactive:",f.isatty())
f.close()

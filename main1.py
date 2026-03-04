#  تخزين قيم الطول والعرض و السعر في متغيرات

str_length = input ("Please type length : \n") 
str_width = input("Please type width : \n")
str_price = input("How much for 1 meter ? \n")
#  تحويل قيم الطول و العرض و السعر من نص الي عدد

length = float(str_length)
width = float(str_width)
#  حساب المساحة عن طريق ضرب الطول في العرض ، وتحويل الناتج من عدد الي نص

area = (length * width)
str_area = str(area)
print ("The total area is : " + str_area)
#  تحويل السعر من نص الي عدد ،وحساب السعر النهائي عن طريق ضرب المساحه في سعر المتر الواحد 

price = float(str_price)
total = (price * area)
str_total = str(total)

print ("Give the guy : " + str_total + "$")
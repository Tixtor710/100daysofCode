sum_odd_didgits=0
sum_even_digits=0
total =0

card_number= input("Enter Credit card Numnber #: ")
card_number = card_number.replace("-","")
card_number= card_number.replace(" ","")

card_number= card_number[: : -1]

for x in card_number[: : 2]:
    sum_odd_didgits = sum_odd_didgits =+ int(x)

for x in card_number[1: :2]:
    x= int(x)*2
    if x >=10:
        sum_even_digits += (1+(x%10))
    else:
        sum_even_digits +=10

total= sum_odd_didgits+ sum_even_digits

if total% 10 ==0:
    print("Valid")
else:
    print("Inval;id")
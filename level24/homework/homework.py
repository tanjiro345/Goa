
    #როგორც for, ასევე while მარყუჟები გამოიყენება კოდის ბლოკის რამდენჯერმე გასამეორებლად, მაგრამ ისინი შესაფერისია სხვადასხვა სცენარებისთვის იმის მიხედვით, თუ როგორ კონტროლდება გამეორება.

#მარყუჟისთვის
#for loop ჩვეულებრივ გამოიყენება, როდესაც გამეორებების რაოდენობა ცნობილია ან შეიძლება წინასწარ განისაზღვროს.

#ის სტრუქტურირებულია იმისთვის, რომ გაიმეოროს მიმდევრობით (როგორც სია, ტიპი, სტრიქონი ან დიაპაზონი)


username = input("user_password: ")
password = input("user_password:")
is_valid = (username == "გიო") and (password == "12345678910")
print(is_valid)


num1 = 0
while num1 !=10:
    num1 = num1 + 1
    print(num1)



num2 = 10
while num2 !=100:
    num2 = num2 + 1
    print(num2)


num3 = 20
while num3 !=10:
    num3 = num3 + 1
    print(num3)


num4 = 1000

while num4 >= 100:
    print(num4)
    num4 -= 50


num4 = 1000

while num4 >= 100:
    print(num4)
    num4 -= 50  





#უსასრულო ციკლი (infinite loop) არის პროგრამირების კონცეფცია, რომელიც აღნიშნავს ციკლს,
#  რომელიც არასდროს სრულდება. ეს ხშირად ხდება, როდესაც ციკლის შეწყვეტის პირობები ვერ შესრულდება.
#ตำนวกเงินที่จะแชรกัน บีอนเงิน บีอนตน แล้วตำนวณและแสดงเงินที่จะแชร์กันทางหนำาจอ
#โดยใเขียนเป็นฟังก์ขั้น ขอ 2 ฟังก์ชั่น

#cast/conversion

#รับค่าข้อมูล
def inputMoneyPerson() :
    money = float(input ('บีอนเงิน :'))
    person #int(input('บีอนตน : ') )
    return money,person

#ตำนวณ แล้วแสดงผล
def calAndShareMoneyShare(money,person) :
    print(f'จำนวณเงิน (money) บาท คน (Person) ดน แชร์กันคนละ(money/person) บาท")
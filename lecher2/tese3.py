#รับคำข้อมูลจากแป้นพิมพ์
emp_name = input ('ป้อนช็อพนักงาน')
sale_price = float(input('ป้อนยอดขาย : '))
4 print('---------------------')
#แปลง Str เป็น number --> int() จำนวนเต็ม float () จำนวนจริงหรือทศนิยม
commission = float(sale _price)* 10 / 100
s = format(float(sale_price),".2f")
c = format(float(commission),".2f")

print(f'คุณ (emp_name) ยอดขาย (float(sale_price:,.2f)) บาท')
print("คุณ",emp_name ,"ยอดขาย",S,"บาท ได้ด่าตอม",c,)
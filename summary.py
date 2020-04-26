print("-----------------------------------")
print("# Summation Program")
print("# Type 'exit' to end the program")
print("-----------------------------------")

# ตัวแปรไว้เก็บผลรวม
sumdata = 0
count = 1

while True:
    
    data = input(f"Enter number {count}: ")
    
    # ตรวจสอบผู้ใช้ป้อน exit หรือไม่ ?
    if data == 'exit':
        break
    
    # การหาผลรวม
    sumdata += int(data)
    #sumdata = sumdata + int(data)
    count = count + 1

print(sumdata)

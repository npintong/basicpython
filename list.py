# LISTS
# DICTIONARIES
# TUPLES
# SETS

# การใช้ LISTS

number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jany', 'Wason']
mixed = [10, 25.75, True, 'Samit']

# ตรวจสอบชนิดของข้อมูล Data type
print(type(number))
print(type(name))
print(type(mixed))

# การเข้าถึงสมาชิกใน list
print(number[1])
print(name[2])
print(mixed[3])

# นับสมาชิกทั้งหมดของ Number
print("สมาชิกทั้งหมดของ Number = ", len(number))
# print(number)

# การสร้าง Empty List
data = []

# การเพิ่มสมาชิกเข้าไปใน List
# data.append(10)

i = 1

while i <= 10:
    data.append(i)
    i = i+1

print(data)

# การอัพเดทสมาชิกใน list
#data[1] = 12

# ฟังก์ชั่นวนลูปอ่านสมาชิกทั้งหมด
data = [1, 2, 3, 4, 5, 6, 7]
for n in data:
    print(n,end=" ")


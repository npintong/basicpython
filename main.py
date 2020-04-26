# Import ทั้งหมดทุกฟังก์ชั่นใน Module

#import numbers

# Import มาบางฟังก์ชั่น

#from numbers import factorial
#from numbers import factorial, fibonacci
# Import ทุกฟังก์ชั่น
#from numbers import*

# Import และเปลี่ยนชื่อฟังก์ชั่น
from numbers import factorial as fa, fibonacci as fi
# เรียกใช้งาน
#print(numbers.factorial(5))
#print(numbers.fibonacci(100))

#print(factorial(5))
print(fa(5))
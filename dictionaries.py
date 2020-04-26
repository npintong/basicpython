scores = {
    'john': 1200,
    'bobby': 2000,
    'janny': 4200
}

print(scores)

print(scores['bobby'])

# เพิ่มสมาชิกใหม่ใน dictionary

scores['roger'] = 3200

print(scores)


# การสร้าง Empty Dictionary

points = {}

points['mar_a'] = 10.2
points['mar_b'] = 500
points['mar_c'] = 20.88

# การ loop อ่านสมาชิกของ Dictionary ออกมา
for k, v in scores.items():
    print(k, v)

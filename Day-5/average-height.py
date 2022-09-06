student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

count = 0;
sum= 0;
for n in student_heights:
    count += 1
    sum += n

print(sum/count)
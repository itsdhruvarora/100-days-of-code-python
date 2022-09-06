scores = input("Enter a list of students score: ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

print(scores)

max = -1;

for n in scores:
    if(max < n):
        max = n

print(max)

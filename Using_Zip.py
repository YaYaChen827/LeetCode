# Using Zip

sub, people = map(int, input().split())

score = []
for i in range(people):
	score.append(list(map(float, input().split())))

print (*[sum(student)/people for student in zip(*score)], sep="\n")
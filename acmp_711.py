file_in = open("INPUT.TXT", "r", encoding="utf-8")
file_out = open("OUTPUT.TXT", "w", encoding="utf-8")

first = file_in.readline().split()
if first:
    n = int(first[0])
    m = int(first[1])
else:
    n = 0
    m = 0

best_name = ""
best_time = None

for _ in range(n):
    name = file_in.readline().rstrip("\n")
    times_line = file_in.readline().split()
    total = 0
    for i in range(min(m, len(times_line))):
        total += int(times_line[i])

    if best_time is None or total < best_time:
        best_time = total
        best_name = name

file_out.write(best_name)

file_in.close()
file_out.close()

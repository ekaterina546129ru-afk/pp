file_in = open("INPUT.TXT", "r", encoding="utf-8")
data = file_in.read().strip()
file_in.close()

if data:
    n = int(data)
else:
    n = 0

sum_of_dividers = 0
for d in range(1, n + 1):
    if n % d == 0:
        sum_of_dividers += d

file_out = open("OUTPUT.TXT", "w", encoding="utf-8")
file_out.write(str(sum_of_dividers))
file_out.close()

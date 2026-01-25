file_in = open("INPUT.txt", "r", encoding="utf-8")
file_out = open("OUTPUT.txt", "w", encoding="utf-8")

t_room, t_cond = map(int, file_in.readline().split())
mode = file_in.readline().strip()

if mode == "freeze":
    if t_room > t_cond:
        result = t_cond
    else:
        result = t_room

elif mode == "heat":
    if t_room < t_cond:
        result = t_cond
    else:
        result = t_room

elif mode == "auto":
    result = t_cond

elif mode == "fan":
    result = t_room

file_out.write(str(result))

file_in.close()
file_out.close()


import sys

n = int(sys.stdin.readline())
set = 0
for i in range(n):
	full_cmd = sys.stdin.readline().split()
	if full_cmd[0] == "empty":
		set = 0
	elif full_cmd[0] == "all":
		set = (1 << 20) - 1
	else:
		cmd = full_cmd[0]
		target = int(full_cmd[1]) - 1
		if full_cmd[0] == "add":
			set = set | (1 << target)
		elif full_cmd[0] == "check":
			if set & (1 << target) == 0:
				print(0)
			else:
				print(1)
		elif full_cmd[0] == "toggle":
			set = set ^ (1 << target)
		elif full_cmd[0] == "remove":
			set = set & (~(1 << target))

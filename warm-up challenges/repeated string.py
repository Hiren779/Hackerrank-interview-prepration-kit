s = raw_input().strip()
n = long(raw_input().strip())

count_in_s = s.count('a')
print n // len(s) * count_in_s + s[0:n % len(s)].count('a')

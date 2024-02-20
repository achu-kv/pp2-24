import re

# task 1
def match_a_0bplus(line):
    match = re.search("(a)|(ab*)", line)
    if match is None:
        return False
    return len(match.group()) > 0

# task 2
def match_a_23b(line):
    match = re.search("(abb)|(abbb)", line)
    if match is None:
        return False
    return len(match.group()) > 0

# task 3
def lower_under(line):
    rgx = '([a-z]+_[a-z]_)*[a-z]'
    res = re.findall(rgx, line)
    return res
    # FINISH

# task 4
def up_low(line):
    return re.findall("[A-Z][a-z]", line)

# task 5
def abstring(line):
    return re.findall('a*b', line)

# task 6
def rep(line):
    return re.sub('[ ,.]', ',',line)

# task 7
def snk_to_cml(line):
    print(re.split('([a-z]|[A-Z])_', line))

# task 8
def split_up(line):
    return re.split('[A-Z]', line)

# task 9
    

print(split_up("Among Us"))
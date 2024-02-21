import re

# task 1
def match_a_0bplus(line):
    match = re.search("ab*", line)
    if match is None:
        return False
    return len(match.group()) > 0

# task 2
def match_a_23b(line):
    match = re.search("ab{2,3}", line)
    if match is None:
        return False
    return len(match.group()) > 0

# task 3
def lower_under(line):
    rgx = '(?:[a-z]*_[a-z]+)+'
    res = re.findall(rgx, line)
    return res

# task 4
def up_low(line):
    return re.findall("[A-Z][a-z]*", line)

# task 5
def abstring(line):
    return re.findall('a.*b', line)

# task 6
def rep(line):
    return re.sub('[ ,.]', ':',line)

# task 7
def snk_to_cml(line):
    line = line.capitalize()
    return re.sub('_[a-z]', lambda x: x.group()[1].upper(), line)

# task 8
def split_ups(line):
    return re.sub('[A-Z]+[^A-Z]+', lambda x: ' ' + x.group(), line).split()

# task 9
def rep_ups(line):   
    return re.sub('[A-Z]+[^A-Z]+', lambda x: ' ' + x.group(), line).strip()

# task 10
def cml_to_snk(line):
    return re.sub('[a-z][A-Z]', lambda x: x.group()[0] + '_' + x.group()[1].lower(), line).lower()


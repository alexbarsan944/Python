# Verify using a regular expression whether a string is a valid CNP.
import re


def verify_cnp(cnp):
    control = '279146358279'
    sum = 0

    if not len(cnp) == 13:
        return 'Invalid CNP'
    else:
        s = cnp[:1]
        aa = cnp[1:3]
        ll = cnp[3:5]
        zz = cnp[5:7]
        jj = cnp[7:9]
        nnn = cnp[9:12]
        c = cnp[-1]

        if not re.match(r'[1-8]', s):
            return 'Invalid CNP'
        if not re.match(r'[0-9]{2}', aa):
            return 'Invalid CNP'
        if not re.match(r'[0][1-12]|[0-12]*', ll):
            return 'Invalid CNP'
        if not re.match(r'[0][1-9]|[0-31]*', zz):
            return 'Invalid CNP'
        if not re.match(r'[0][1-9]|[0-52]*', jj):
            return 'Invalid CNP'
        if not re.match(r'[0-9]{3}', nnn):
            return 'Invalid CNP'
        for i in range(0, len(cnp) - 1):
            sum += int(cnp[i]) * int(control[i])

        if sum % 11 == 10:
            expected = 1
        else:
            expected = sum % 11

        if not int(c) == expected:
            return 'Invalid CNP2'

        return 'Valid CNP'


print(verify_cnp('1990510276438'))

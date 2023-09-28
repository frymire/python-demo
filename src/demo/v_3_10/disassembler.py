
from dis import dis


def sum_it():
    vara = 10
    varb = 20
    print(f"vara + varb = {vara + varb}")


dis(sum_it)  # disassemble the function

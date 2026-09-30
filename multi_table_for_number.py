def multiTable(multiplicando):
    UNO = 1
    DIEZ = 10
    nums = range(UNO, DIEZ + UNO)
    return "\n".join(f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}" for multiplicador in nums)
    
multiTable(6)
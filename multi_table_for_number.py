def multiTable(multiplicando):
    nums = range(1,11)
    return "\n".join(f"{i} * {multiplicando} = {i * multiplicando}" for i in nums)
    
multiTable(6)
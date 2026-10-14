def permute_a_palindrome(input):
    impar = 0

    for chart in set(input):
        contador = input.count(chart)

        if contador % 2 != 0:
            impar += 1

    if impar <= 1:
        return True
    else:
        return False
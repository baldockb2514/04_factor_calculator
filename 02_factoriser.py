
def get_factors(to_factor):

    stop = int(to_factor**(0.5))

    factors_list = []

    for item in range(1, stop, +1):
        is_factor = to_factor % item

        # if modulo is 0, the number is a factor
        if is_factor == 0:

            # gets second factor by dividing 'to factor' by the first factor
            factor_2 = (to_factor / item)

            factors_list.append(item)

            if factor_2 not in factors_list:
                factors_list.append(factor_2)

    factors_list.sort()
    return factors_list






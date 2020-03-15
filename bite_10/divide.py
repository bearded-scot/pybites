def positive_divide(numerator, denominator):
    try:
        ret = numerator/denominator
        if ret < 0:
            raise ValueError('Result is negative')
        return ret
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError('the numerator or denominator is the wrong type')



"""_summary_
"""


def apply_vat(price: float, percent: float):
    """if not isinstance(price, float):
        raise ValueError(f'Price (${price}) is not a number')
    elif not isinstance(percent, float):
        raise ValueError(f'Percent ({percent}%)')
    elif price < 0:
        raise ValueError(f'Price (${price}) is negative')
    elif percent < 0:
        raise ValueError(f'Percentage ({percent}%) is negative')
    elif percent > 100:
        raise ValueError(f'Percentage ({percent}%) is to high')
    else:"""
    return price + ((percent/100) * price)
    

if __name__ == '__main__':
    
    print(apply_vat(100, 25))
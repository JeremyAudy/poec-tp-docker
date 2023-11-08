"""
main
"""


from calc import apply_vat
import sys

price = float(sys.argv[1])
percent = float(sys.argv[2])

if __name__ == "__main__":
    print(apply_vat(price, percent))
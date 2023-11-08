# TVA CALCULATOR
### Doc version : c1 - 08/11/2023
## Project descroption
Calculate the price of a product with is TVA

## Prerequisites
-Docker

## How to use
- In a terminal go to the parent file of poec-tp-docker use the command:
  - docker build -t tp-docker poec-t-docker
  - docker run -it tp-docker python src/main.py argument1 argument2
    - argument1 is the price it can't be negative
    - argument2 id the percentage of the TVA it needs to be between 0 and 100

## How to test
- In a terminal go to the parent file of poec-tp-docker use the command:
  - docker build -t tp-docker poec-t-docker
  - docker run -it tp-docker python src/test.py
  
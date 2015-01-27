# MiniMathematica

## What is this?
This is a simple calculator that uses the [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) and [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

## What does it do?
This calculator can do the following things:
- evaluate simple expressions(__addition__, __subtraction__, etc.)
- evaluate trigonometric functions(__sine__, __cosine__, __tangent__ and __cotangent__)
- evaluate __square root__, __nth-root__ and __power__
- evaluate __logarithms__
- supports constants(__Pi__ and __E__)
- supports negative numbers
- evaluate an expression comprised of all of the above

## How to run it?
You need to have __Python3__ installed and if you do, you can run this program by executing the following command:
`python3 cli.py`

## Then what?
Enter a (valid) mathematical expression using the following syntax:
- For the trigonometric functions:
	+ `sin(n)`, where __n__ is the number you want the sine of.
	+ `cos(n)`, where __n__ is the number you want the cosine of.
	+ `tg(n)`, where __n__ is the number you want the tangent of.
	+ `cotg(n)`, where __n__ is the number you want the cotangent of.
- For roots:
	+ `sqrt(n)`, where __n__ is the number you want the square root of.
	+ `nthrt(k, n)`, where __k__ is the number you want the __n__-th root of.
- For powers:
	`pow(k, n)`, where __k__ is the number you want the __n__-th power of.
- For logarithms:
	`log(k, n)`, where __k__ is the base and __n__ the number you want the logarithm of.

#### Example
	Enter an expression you would like to be calculated.
    > 5 + sin(pi) / pow(2, 10) - log(e, pow(e, sqrt(4)))
    The result is: 3.0


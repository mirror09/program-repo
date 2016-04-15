def simpleDerivativeCalculator(equation):
    for e in range(1,len(equation)):
        if equation[e].isalpha():
            c = equation[e]
            print c
            a = int(equation[2:e])
            print a
            b = int(equation[e+2:])
            print b
            break
    return "y'="+str(a*b)+c+"^"+str(b-1)

print(simpleDerivativeCalculator("y=37686x^22"))


def Fibonacci(ele):
    """ This function is created to return the (ele index) number in the series """
    if ele == 0:
        return 0
    elif ele == 1:
        return 1
    elif type(ele) != int:
        return "IT'S NOT A NUMBER"
    else:
        return Fibonacci(ele - 2) + Fibonacci(ele - 1)
            

def Lucas(ele):
    """" This function is created to return the (ele index) number in the series """
    if ele == 0:
        return 2
    elif ele == 1:
        return 1
    elif type(ele) != int:
        return "IT'S NOT A NUMBER"
    else:
        return Lucas(ele - 2) + Lucas(ele - 1)

def sum_series(ele, x=0, y=0):
    """ This function is created to allow the user to choose the parameters with him self so if the user choosse one ele it will work with the fibonacci, if the user choose three ele it will work with lucas otherwise it will create a new series """
    if ele == 0:
        return x
    elif ele == 1:
        return y
    elif type(ele) != int:
        return "IT'S NOT A NUMBER"
    else:
        return sum_series(ele-2,x,y) + sum_series(ele-1,x,y)

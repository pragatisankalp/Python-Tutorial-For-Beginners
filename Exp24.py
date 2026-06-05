
def test1():
    x=9
    def test2():
        global x
        x=67
        print(x)
    print("After test1, value of x is: ", x)
    test2()
    print("After test 2, value of x is: ", x)
test1()



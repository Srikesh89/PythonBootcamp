#python ./one.py
def f1():
    print('fcn in one.py')
print("Top level in one.py")
# def f2():
#     pass
# def f3():
#     pass
# def f4():
#     pass

if __name__ == "__main__":
    print('one.py is being run directly')
    f1()
else:
    print('one.py has been imported')
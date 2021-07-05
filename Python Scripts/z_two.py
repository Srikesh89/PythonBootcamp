#two.py
import z_one

print("Top level in two.py")
z_one.f1()

if __name__ == '__main__':
    print('two.py is run directly')
else:
    print('two.py has been imported')
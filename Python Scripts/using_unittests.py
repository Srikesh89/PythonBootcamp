'''Doc string for good pylint score'''

def myfunc():
    '''Another doc string'''
    first = 1
    second = 2
    print(first)
    print(second)

def cap_text(text):
    '''input string, output capitalized first char string'''
    return text.title()

if __name__ == '__main__':
    myfunc()
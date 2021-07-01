#Skyline Exercise
def myfunc(string):
    skyline_string = ''
    string_length = len(string)
    current_index = 0
    while(current_index < string_length):
        if(current_index%2==1):
            #do odd letter
            skyline_string += string[current_index].lower()
        else:
            #do even
            skyline_string += string[current_index].upper()
        current_index += 1
    return skyline_string

print(myfunc('abcdefgh'))
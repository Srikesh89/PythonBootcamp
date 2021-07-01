def summer_69(arr):
    sum = 0
    has_six_been_shown = False
    has_nine_been_shown = False
    for number in arr:
        if number == 6:
            has_six_been_shown = True
            continue
        if number == 9:
            has_nine_been_shown = True
            continue
        if(not has_six_been_shown):
            sum += number
        elif(has_six_been_shown and not has_nine_been_shown):
            continue
        elif(has_six_been_shown and has_nine_been_shown):
            sum += number
    return sum

summer_69([4,5,6,7,8,9])
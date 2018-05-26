
print_order = 0

upper_num = 40

def print_diamond():
    dot_1 = upper_num / 2
    dot_2 = upper_num / 2
    counter = 0
    for j in range(1 + (upper_num // 2)):
        for i in range(upper_num):
            if (i == dot_1) or (i == dot_2):
                print('*', end='')
            else:
                print('-', end='')
        print()
        if counter < 10:
            dot_1 += 1
            dot_2 -= 1
            counter += 1
        elif counter >= 10:
            dot_1 -= 1
            dot_2 += 1            

print_diamond()
    

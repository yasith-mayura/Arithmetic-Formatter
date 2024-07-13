line1 = []
line2 = []


def arithmetic_arranger(problems, show_answers=False):
    for problem in problems:
        index = problem.find(" ")

        line1.append(problem[:index])
        line2.append(problem[index+1:])
    




def print_arranged_arithmetic():
    for number in line1:
            print(number,end="    ")
    
    print("")
    
    for number in line2:
        print(number,end=" ")









print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print_arranged_arithmetic()

##########################
#Erik Marquez
#Lab 8
#10/8/18
#
#########################


def user_mpg_input():
    '''Takes user inpur and validates,
    value must be greater then 0 or less then or equal to 100
    '''
    while True:
        try:
            user_input=float(input('Enter the minimum mpg ==>'))
            if user_input > 0 and user_input < 101:
                break
            elif user_input < 0 or user_input > 100:
                print('Input must be between 1-100')
        except ValueError:
            print('You must enter a number for the fuel economy')
    return user_input

def file_to_open():
    '''ask user for file to open and validates'''
    while True:
        try:
            file= input('\nEnter the name of the input vehicle file ==>')
            fh=open(file)
            break
        except FileNotFoundError:
            print('Could not open file {}. Make sure it ends with .txt'.format(file))
    lines = fh.readlines()
    fh.close()
    return lines


def file_to_save():
    '''Ask user for file to save and validates'''
    while True:
        try:
            save_file = input('\nEnter the name of the file to output to ==>')

            sf = open(save_file, 'w')

            break
        except:
            print('There is an IO Error', save_file)

    return sf

def mpg_return(mpg_input,input,output):
    '''Take the user input and returns a file with cars meeting the criteria'''
    for line in input[1:]:
        try:
            make_model = line.split('\t')
            mpg = (line.split('\t')[7])
            combined_mpg = float(line.split('\t')[7])
            if mpg_input <= combined_mpg:

                print('{:<5}{:<20}{:<40}{:>10}'.format (make_model[0],make_model[1],make_model[2],mpg))
                print('{:<5}{:<20}{:<40}{:>10}'.format (make_model[0],make_model[1],make_model[2],mpg), file=output)

        except ValueError:
            print('Could not convertt valur {} for {} {} {}'.format(line.split('\t')[7],make_model[0],make_model[1],make_model[2]))
    #output.close()



## main loop

while True:
    user_input = user_mpg_input()

    mpg_file = file_to_open()

    save_file = file_to_save()

    mpg_return(user_input,mpg_file,save_file)




#
# This Program creates the basic setup for every day of my 30 days challenge.
# The setup includes a python 'day_##.py' file for the code and one 'test_day_##.py' file for tests.
#


import os


def find_highest_day():
    """
    find the highest day number and return it
    """
    highest_number = 0
    os.chdir('../')
    # list all directories in the specified directory
    directories = [obj for obj in os.listdir('./') if os.path.isdir(obj)]
    # find the hightest day number by extracting the day number from the directory names
    for directory in directories:
        try:
            number = int(directory[-2:])
            print(number)
            if number > highest_number:
                highest_number = number
        except Exception:
            print('Exception')
    else:
        print('Highest Number is {}'.format(highest_number))
    return highest_number


def create_new_day(new_day):
    """
    Creates a new folder and a script with the given day number
    """
    # create directory
    os.makedirs('./Day_{:02d}'.format(new_day))
    os.chdir('./Day_{:02d}'.format(new_day))
    # create files
    open('day_{:02d}.py'.format(new_day), 'a').close()
    open('test_day_{:02d}.py'.format(new_day), 'a').close()


def run():
    last_day = find_highest_day()
    new_day = last_day + 1
    create_new_day(new_day)


if __name__ == '__main__':
    run()

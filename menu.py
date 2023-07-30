# STL imports
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", required=False, default=None)
    args, _ = parser.parse_known_args()
    return args
class Option:
    def __init__(self, description, func):
        self.description = description
        if func is not None:
            self.function = func()



def start():
    args = get_arguments()
    option = args.o
    possible_options = {}
    print('OPTION IS', option)
    if option is None or option == '':
        print('********** THIS IS MENU  **********')
        for option in possible_options:
            print(option)
        print('********** SELECT OPTION **********')
    else:
        selected_option = possible_options[int(option)]
        print(f'SELECTED OPTION IS {selected_option.description}')
        selected_option.function()

if __name__ == "__main__":
    start()

from loader import Loader


class MenuComponent(Loader):

    def __init__(self):
        self.__menu_list = {1: ['1 - Download video', self.load_video],
                            2: ['2 - Download playlist', self.load_playlist]}

        self.selected_item = None
        self.user_num = None

    def menu(self):
        return self.__menu_list

    def print_menu_items(self):
        for key, value in self.__menu_list.items():
            print(value[0])

    @staticmethod
    def user_input_validate(value):
        try:
            int(value)
            return True

        except:
            print('Enter the number')
            return False

    def user_input(self):
        user_inp_num = input('\nEnter number from menu: ')

        if self.user_input_validate(user_inp_num):
            return int(user_inp_num)

    def user_select(self, user_input):
        for key, value in self.__menu_list.items():
            if key == user_input:
                return value[1]

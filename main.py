
from menu import MenuComponent

def main():
    menu = MenuComponent()

    while True:
        menu.print_menu_items()
        selected_funk = menu.user_select(menu.user_input())
        selected_funk()



if __name__ == '__main__':
    main()

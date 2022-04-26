# Programmer: Andrew Dwyer
# Date: 4/26/22

import views.main_view.main_view as main_view


# this is the entry point for the application
def main():
    # set up db here
    # calls the main window to display itself
    app_view = main_view.MainView()


# call main() if not imported as a module
if __name__ == '__main__':
    main()

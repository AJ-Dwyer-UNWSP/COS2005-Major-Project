# Programmer: Andrew Dwyer
# Date: 4/26/22

import views.main_view.main_view as main_view
import db_handlers.db_initializer as db_initializer
from data_context import DataContext


# this is the entry point for the application
def main():
    # initializes the db
    db_init = db_initializer.DBInitializer()
    data_context = DataContext(db_init)

    # calls the main window to display itself
    app_view = main_view.MainView(data_context)

    # the app was closed so close the db connection
    db_init.close()


# call main() if not imported as a module
if __name__ == '__main__':
    main()

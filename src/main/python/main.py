from fbs_runtime.application_context.PyQt5 import ApplicationContext

import sys
import Controller as Control


# Application
class AppContext(ApplicationContext):
    def run(self):
        controller = Control.Controller()
        controller.show_MainWindow()
        return self.app.exec_()


# Main Application
if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
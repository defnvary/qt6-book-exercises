# only needed for access to command line arguments
import sys

from PyQt6.QtWidgets import QApplication, QWidget

# only one QApplication instance per application
# pass in sys.argv to allow command line arguments in app
# if you wont't use c l args QApplication([]) works too

app = QApplication(sys.argv)

# create a qt widget which will be our window
window = QWidget()
window.show()  # windows are hidden by default

# start the event loop
app.exec()

# your application won't reach here until you exit and the event loop has stopped.

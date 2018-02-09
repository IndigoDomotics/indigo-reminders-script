### Reminders AppleScript

The purpose of this script is to provide a bridge between Python scripts
that use py-applescript (installed with Indigo 7.1 and up) and the
Reminders App in macOS. Why would you want to do this? So that you can
easily create Reminders from Python (and, therefore, from Indigo).

This script is a useful pattern for others that want to bridge
AppleScriptable macOS apps to Python.

If you are using Indigo 7.0.x, you can [download and install py-applescript v1.0.1
from our repo](https://github.com/indigodomo/py-applescript). The [1.0.0
version which is currently in PyPI](https://pypi.python.org/pypi/py-applescript/1.0.0) and installable via `pip` has a bug
which keeps it from correctly loading AppleScript files.
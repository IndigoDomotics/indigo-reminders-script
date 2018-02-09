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

### Usage

Download the latest release from the releases link above. Once you've got
it downloaded to your Mac, move the `Reminders.scpt` AppleScript file to
some safe, permanent location. We recommend that you put them here:

[INDIGO INSTALL DIR]/Scripts

where [INDIGO INSTALL DIR] is equal to the appropriate installation directory
for your version of Indigo. For Indigo 7, the install directory is:

`/Library/Application Support/Perceptive Automation/Indigo 7`

Then you can take a look at the `reminders-test.py`
file that was also in the repo for examples of how to load and call the
script. That script has logic at the top that will help guarantee that
the script will always run from the right place even when you upgrade
to a newer major version. That's why we recommend that you install it
to the above location.

[See the wiki](https://github.com/IndigoDomotics/indigo-reminders-script/wiki)
for a full description of how to use this script.
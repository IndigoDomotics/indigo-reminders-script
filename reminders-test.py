# Import the py-applescript module
import applescript

# Import other standard Python stuff
from datetime import datetime, timedelta
import sys

# To make this script as universal as possible, we're goin to get a little tricky with
# imports. First, we'll attempt to import the indigo module, which should only work if
# this script is running from within Indigo.
try:
    import indigo
except:
    indigo = None

# Assuming you've followed the recommendations on where to put the script and you're running
# it from Indigo, this section that specifies the script path should work nicely with no changes
# and is future proof since it should work from any version of Indigo after Indigo 6.
if indigo:
    path_to_script = indigo.server.getInstallFolderPath() + "/Scripts/Reminders.scpt"
else:
    # If you aren't running the script from Indigo then you should use this line along with a
    # a full path specifier. Take out the if/else from above even if you are running from
    # Indigo but are using a custom path.
    path_to_script = "/Reminders.scpt"

# Now that we have the path sorted, load the script using the py-applescript module
reminders = applescript.AppleScript(path=path_to_script)

# For these examples, we'll set the due date to be 24 hours from the time this script is run
due_date = datetime.today() + timedelta(days=1)

#
# Create the reminder dictionary
#
reminder_dict = {
    "title": "Test Reminder",
    "notes": "Notes go here",
    "due_date": due_date,
    "destination_list": "Reminders",
    "destination_account": "iCloud",
    "priority_string": "high"
}
#
# Call the makeNewReminder handler in the Reminders script. The syntax to call an AppleScript handler
# follows this pattern:
#
#     return_data = scriptobject.call("handlername", ["parameter1", ["parameter2"...]])
#
# We want to call the makeNewReminder(reminder_record) method of the script, so our call looks like this:
reply = reminders.call("makeNewReminder", reminder_dict)
if not reply["success"]:
    reason = reply["reason"]
    print("makeNewReminder failed: ({}) {}".format(reason["error_number"], reason["error_message"]))
    sys.exit(reason["error_number"])
#
# Mark the reminder as complete, but don't automatically delete it
#
completion_dict = {
    "delete_reminder": False,
    "reminder_id": reply["reminder_id"]
}
reply = reminders.call("completeReminder", completion_dict)
if not reply["success"]:
    reason = reply["reason"]
    print("completeReminder failed: ({}) {}".format(reason["error_number"], reason["error_message"]))
    sys.exit(reason["error_number"])
#
# Delete the reminder
#
reply = reminders.call("deleteReminder", reply["reminder_id"])
if not reply["success"]:
    reason = reply["reason"]
    print("deleteReminder failed: ({}) {}".format(reason["error_number"], reason["error_message"]))
    sys.exit(reason["error_number"])

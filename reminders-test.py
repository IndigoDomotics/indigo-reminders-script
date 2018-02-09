# Import the py-applescript module
import applescript

# Import other standard Python stuff
from datetime import datetime, timedelta
import sys

# Change this to point to the actual location of your script
path_to_script = "/Reminders.scpt"
reminders = applescript.AppleScript(path=path_to_script)

due_date = datetime.today() + timedelta(days=1)

#
# Create the reminder
#
reminder_dict = {
    "title": "Test Reminder",
    "notes": "Notes go here",
    "due_date": due_date,
    "destination_list": "Reminders",
    "destination_account": "iCloud",
    "priority_string": "high"
}
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

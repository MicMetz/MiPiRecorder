import os
import sys
import config



#
def time_stamp():
	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")
	return ("Time:", current_time)
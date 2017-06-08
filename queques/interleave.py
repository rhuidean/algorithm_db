### retrieve the current file name
import sys
import os
current_file_name = os.path.basename(sys.argv[0])

### retrieve all the .py files in the current directory
import glob
for filename in glob.glob('*.py'):
	### exclude current file
	if filename == current_file_name:
		pass

	else:
		print filename
		code = "from "+filename.replace('.py','')+" import *"
		print code
		exec(code)

a=SLQueue()
print a
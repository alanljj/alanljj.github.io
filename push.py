# -*- coding: utf-8 -*-
#!/usr/bin/env python

import subprocess
import datetime

commit_value = input('Please enter update log: ')
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "auto push at " + commit_value + '@' + str(datetime.datetime.now())])
subprocess.call(["git", "push"])
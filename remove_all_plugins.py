#!/usr/bin/env python3

import sys, os.path, subprocess

stdoutdata = subprocess.getoutput("cordova plugin list")
if ("command not found" in stdoutdata):
  print("cordova not installed :(");
  sys.exit(1)

if ("No plugins added" in stdoutdata):
  print("all plugins have been removed :)");
  sys.exit(1)

for item in stdoutdata.split("\n"):
  cmd = "cordova plugin remove " + item.split()[0]
  print(cmd)
  result = subprocess.getoutput(cmd)
  print(result)

print("done! bye!! ;)")

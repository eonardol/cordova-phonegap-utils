#!/usr/bin/env python3

import sys, os.path, subprocess
import argparse

# argument parsing
parser = argparse.ArgumentParser(description='Generate Android/iOS icons for Cordova / Phonegap projects')
parser.add_argument("-i", "--icon", metavar="/path/icon.png", default="icon.png", dest="icon_path", help="the icon path")
args = parser.parse_args()
icon_path = args.icon_path

# check imagemagick
stdoutdata = subprocess.getoutput("which convert")
stdoutarr = stdoutdata.split();
if (len(stdoutarr)==0):
  print("convert command not found: do you have installed ImageMagick?")
  sys.exit(1)

convert_path = stdoutdata.split()[0];
print("convert command: " + convert_path)

# verifico la presenza dell'icona
if os.path.isfile(icon_path) is False:
  print("file", icon_path, "not found")
  sys.exit(1)

# funzione per il resize
def resize(size, out_dir, ico_name="icon"):
  if not os.path.exists(out_dir):
    print("creating", out_dir)
    os.makedirs(out_dir)
  cmd = "%s %s -resize %dx%d %s/%s.png" % (convert_path, icon_path, size, size, out_dir, ico_name)
  print (cmd)
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  p.wait()

# Android icons
resize(96, "android/res/drawable");
resize(72, "android/res/drawable-hdpi");
#resize(72, "android/res/drawable-land-hdpi");
#resize(72, "android/res/drawable-land-ldpi");
#resize(72, "android/res/drawable-land-mdpi");
#resize(72, "android/res/drawable-land-xhdpi");
resize(36, "android/res/drawable-ldpi");
resize(48, "android/res/drawable-mdpi");
resize(96, "android/res/drawable-xhdpi");

# iOS icons
resize(40, "ios/icons", "icon-40");
resize(80, "ios/icons", "icon-40@2x");
resize(50, "ios/icons", "icon-50");
resize(100, "ios/icons", "icon-50@2x");
resize(60, "ios/icons", "icon-60");
resize(120, "ios/icons", "icon-60@2x");
resize(72, "ios/icons", "icon-72");
resize(144, "ios/icons", "icon-72@2x");
resize(76, "ios/icons", "icon-76");
resize(152, "ios/icons", "icon-76@2x");
resize(29, "ios/icons", "icon-small");
resize(58, "ios/icons", "icon-small@2x");
resize(57, "ios/icons", "icon");
resize(114, "ios/icons", "icon@2x");

#!/usr/bin/env python3

import sys, os.path, subprocess
import argparse

# argument parsing
parser = argparse.ArgumentParser(description='Generate iPhone splashscreen')
parser.add_argument("-s", "--splash", metavar="/path/splash.png", default="splash.png", dest="splash_path", help="the splash path")
args = parser.parse_args()
splash_path = args.splash_path

# check imagemagick
stdoutdata = subprocess.getoutput("which convert")
stdoutarr = stdoutdata.split();
if (len(stdoutarr)==0):
  print("convert command not found: do you have installed ImageMagick?")
  sys.exit(1)

convert_path = stdoutdata.split()[0];
print("convert command: " + convert_path)

# verifico la presenza dell'icona
if os.path.isfile(splash_path) is False:
  print("file", splash_path, "not found")
  sys.exit(1)

# funzione per il resize
def resize(width, height, out_dir, ico_name="icon"):
  if not os.path.exists(out_dir):
    print("creating", out_dir)
    os.makedirs(out_dir)
  cmd = "%s %s -resize %dx%d! %s/%s.png" % (convert_path, splash_path, width, height, out_dir, ico_name)
  print (cmd)
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  p.wait()

# iOS splash
resize(640, 1136, "ios/splash", "Default-568h@2x~iphone");
resize(750, 1334, "ios/splash", "Default-667h");
resize(1242, 2208, "ios/splash", "Default-736h");
resize(640, 960, "ios/splash", "Default@2x~iphone");
resize(320, 480, "ios/splash", "Default~iphone");

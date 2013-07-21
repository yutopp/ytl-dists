#! /usr/bin/env python3
import os
import sys
import platform
import datetime

#
if "BOOST_ROOT" not in os.environ:
    print("Please set BOOST_ROOT to Environment Variable.")
    exit(-1)

#
compilers = sys.argv[1:]
compilers_opt = ",".join(compilers)

if len(compilers) == 0:
    print("Please specify compilers for test.")
    exit(-1)

#
print( datetime.datetime.today() )

#
master_dir = os.getcwd()
print(master_dir)
for p in [os.path.join(master_dir,x,"libs",x[4:],"test") for x in os.listdir(master_dir) if os.path.isdir(x)]:
    if os.path.exists(p):
        os.chdir(p)
        print(os.getcwd())
        if ( platform.system() == "Windows" ):
            os.system("%BOOST_ROOT%\\b2 --verbose-test --toolset=\"{0}\"".format(compilers_opt))
        else:
            os.system("$BOOST_ROOT/b2 --verbose-test --toolset=\"{0}\"".format(compilers_opt))


#
print( datetime.datetime.today() )

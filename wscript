import sys
import os
sys.path.append(os.path.join('..', 'build-tools'))
from shared_wscript import *

def options(opt):
    options_desktop(opt)

def configure(conf):
    configure_desktop(conf)

def build(bld):
    bld.stlib(source=GTEST_SOURCE,
              includes=GTEST_INCLUDE,
              target='gtest')

GTEST_SOURCE = [
    'src/gtest-all.cc'
]

GTEST_INCLUDE = [
    './',
    'include/',
]

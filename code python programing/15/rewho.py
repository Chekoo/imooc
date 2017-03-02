#coding=utf-8

from os import popen
import re
from re import split

f = popen('who', 'r')
for eachLine in f.readlines():

    print re.split('\s\s+', eachLine)
f.close()
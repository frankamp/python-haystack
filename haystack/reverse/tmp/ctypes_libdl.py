#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2011 Loic Jaquemet loic.jaquemet+python@gmail.com
#

__author__ = "Loic Jaquemet loic.jaquemet+python@gmail.com"

import ctypes
import logging, sys

''' insure ctypes basic types are subverted '''
from haystack import model

from haystack.model import is_valid_address,is_valid_address_value,getaddress,array2bytes,bytes2array
from haystack.model import LoadableMembers,RangeValue,NotNull,CString

log=logging.getLogger('ctypes_libdl')


# ============== Internal type defs ==============
class CPP(LoadableMembers):
  ''' defines classRef '''
  pass

class A(CPP):
  _fields_ = [
    ('a', ctypes.c_uint)
  ]

model.registerModule(sys.modules[__name__])
############# Start expectedValues and methods overrides #################

# test

import sys,inspect
src=sys.modules[__name__]

def printSizeof(mini=-1):
  for (name,klass) in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    if type(klass) == type(ctypes.Structure):# and klass.__module__.endswith('%s_generated'%(__name__) ) :
      if ctypes.sizeof(klass) > mini:
        print '%s:'%name,ctypes.sizeof(klass)

import time
import subprocess, os
from subprocess import PIPE
import sys
from subprocess import PIPE, Popen
from threading  import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

ON_POSIX = 'posix' in sys.builtin_module_names

def enqueue_output(out, queue):
    for line in iter(out.readline, ''):
        queue.put(line)
    out.close()

def getOutput(p):
  q = Queue()
  t = Thread(target=enqueue_output, args=(p.stdout, q))
  t.daemon = True # thread dies with the program
  t.start()
  return q,t

def readlines(q):
  lines=[]
  notEmpty = True
  while notEmpty:
    try:  
      line = q.get_nowait() or q.get(timeout=1)
    except Empty:
      notEmpty = False  
    else:
      lines.append(line)
  return lines

def dumpMemory(pid, fname):
  def dumpit(pid, fname):
    from haystack import memory_dumper
    memory_dumper.dumpToFile(pid, fname)
  t = Thread(target=dumpit, args=(pid, fname))
  t.daemon = True # thread dies with the program
  t.start()
  t.join()
  return fname
  
def makeDumps():
  dumps = []
  
  cmd = ['./src/test-ctypes2']
  p = subprocess.Popen(cmd, bufsize=1, stdin=PIPE, stdout=PIPE)
  q,t = getOutput(p)

  print '\n -- * init data 4 child pid:', p.pid
  out = ''.join(readlines(q))
  while 'START' not in out:
    time.sleep(.1)
    out = ''.join(readlines(q))
  fname = dumpMemory(p.pid, 'test-ctypes2.dump.0')
  print '[+] dumped clean state in', fname
  dumps.append(file(fname,'rb'))
  
  stopMe = False
  i=1
  while not stopMe:
    print '[-] sending enter'
    p.stdin.write('\n')
    out = ''.join(readlines(q))
    while 'OPEN' not in out:
      if 'END' in out:
        print '[+] this is the END... the only END , my friend...'
        stopMe = True
        break
      time.sleep(.1)
      out = ''.join(readlines(q))
    if not stopMe:
      fname = dumpMemory(p.pid, 'test-ctypes2.dump.%d'%(i))
      print '[+] dumped', out.split(' ')[1].strip(), 'in' , fname
      dumps.append(file(fname,'rb'))
    i+=1
    
  return dumps
  
import md5
def buildMappingsHashes(maps):
  return [ (md5.md5(m.mmap().getByteBuffer()).hexdigest(), m.mmap() ) for m in maps]

def getDiff(d1, d2):
  from haystack import dump_loader
  mappings1 = dump_loader.load(d1)
  mappings2 = dump_loader.load(d2)
  log.debug('Building hashes for %s'%(d1.name))
  m1 = dict(buildMappingsHashes(mappings1))
  log.debug('Building hashes for %s'%(d2.name))
  m2 = dict(buildMappingsHashes(mappings2))
  
  # new mappings in d2
  pnames1 = set([m.pathname for m in m1.values()])
  pnames2 = set([m.pathname for m in m2.values()])
  new2 = pnames2 - pnames1
  news = []
  for pathname in new2:
    news.extend(mappings2.getMmap(pathname))
  print 'new mappings in %s:'%(d2.name)
  for n in news:
    print n
  # believe in hash funcs.
  diff2 = set(m2.keys()) - set(m1.keys())
  diffs = []
  revm1 = dict((v,k) for k, v in m1.items())  
  print 'modified mappings in %s:'%(d2.name)
  for h2 in diff2:
    m = m2[h2]
    if m.pathname in pnames1:
      print m
      diffs.append(m)
  return news, diffs
  
def main():
  logging.basicConfig(level=logging.DEBUG)

  logging.getLogger('dumper').setLevel(logging.ERROR)
  logging.getLogger('loader').setLevel(logging.DEBUG)
  logging.getLogger('ctypes_libdl').setLevel(logging.DEBUG)
  
  #dumps = makeDumps()
  dumps = [file('test-ctypes2.dump.%d'%i,'rb') for i in range(4)]
  
  #n1, diff1 = getDiff(dumps[0], dumps[1])
  #import code
  #code.interact(local=locals())

  n2, diff2 = getDiff(dumps[1], dumps[2])
  import code
  code.interact(local=locals())

  n3, diff3 = getDiff(dumps[2], dumps[3])
  import code
  code.interact(local=locals())

if __name__ == '__main__':
  main() #printSizeof()


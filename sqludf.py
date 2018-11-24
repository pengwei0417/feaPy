#/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../lib")
sys.path.append("./lib")
sys.path.append("../")
from functools import reduce
import pandas as pd
import numpy as np

def sqlstr(df,p=""):
  """
  #组合查询语句
  """
  p=p.strip()
  wheres=p.split(",")
  wheresql=reduce(lambda x,y:x+" " + y,map(lambda x:"and instr(jyaq"))
  df=pd.DataFrame({"c":[wheresql]})
  return df

def pp(df,arg1="",arg2=""):
  p=args["key"]
  df=pd.DataFrame({"p":[arg1]})
  return df
  # print(args[1])
  # print(args[2])

pp(key="a")
# df=sqlstr(None,"a,b,c,d")
# print(df)
#/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../lib")
sys.path.append("./lib")
sys.path.append("../")
import jaydebeapi
#import pandas as pd
#import numpy as np
#import pymysql

__workSpace="../workspace/"

from enum import Enum

class datatype(Enum):
  oracle=1
  mysql=2
  mssql=3

class orh:
  def __init__(self,datatype):
    if (datatype==datatype.oracle):
      self.type="oracle"
    elif (datatype==datatype.mysql):
      self.type="mysql"
    elif(datatype==datatype.mssql):
      self.type="mssql"
    
  def gettype(self):
    return self.type

o=orh(datatype.mssql)
print(o.gettype())

def test(df,p=""):
    return df
    
def connOracle(df,p=""):
  url='jdbc:oracle:thin:@127.0.0.1/orcl'
  user='scott'
  password='tiger'
  dirver='oracle.jdbc.driver.OracleDriver'
  jarFile='py4j0.10.7.jar'
  sqlStr='select * from dual'
  #conn=jaydebeapi.connect('oracle.jdbc.driver.OracleDriver',['jdbc:oracle:thin:@127.0.0.1/orcl','scott','tiger'],'D:\\MY_TOOLS\\ojdbc6.jar')
  conn=jaydebeapi.connect(dirver,[url,user,password],jarFile)
  return df
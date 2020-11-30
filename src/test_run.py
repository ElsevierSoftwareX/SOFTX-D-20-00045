#%% libraries
import os
import time

from   pyomo.environ import ConcreteModel
from openTEPES import InputData
CWD = os.getcwd()
Test_Path = CWD + '/src/openTEPES'
os.chdir(Test_Path)

StartTime = time.time()

CaseName = '9n'

#%% model declaration
mTEPES = ConcreteModel()

# InputData(CaseName, mTEPES)

TotalTime = time.time() - StartTime
print('Total time                            ... ', round(TotalTime), 's')
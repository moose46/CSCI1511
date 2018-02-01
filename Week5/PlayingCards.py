import sys, math

sys.path.append('./')
##import PickACard
from PickACard import *

for i in range(7):
    aSuit = pickSuit()
    aValue = pickValue()

    print(aValue, " ", aSuit)




import pytest
import conf.globalFacts as globalFacts
import senceCheck
import  sys,os


projectPath = os.path.join(os.path.split(os.path.realpath(__file__))[0],os.path.pardir)
sys.path.append(projectPath)
if __name__ == '__main__':
    assert senceCheck.get_sence(r"d:\a.png") == globalFacts.SenceVictory

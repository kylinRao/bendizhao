import datetime,os,sys,time




tasksList = [

    {"fixdeTime":datetime.time(5,00,0,0),"fileName":"all_5723.py"},

    {"fixdeTime":datetime.time(10,0,0,0),"fileName":"juexing_5723.py"},
    {"fixdeTime":datetime.time(12,0,0,0),"fileName":"yuhun_5723.py"},
    {"fixdeTime":datetime.time(14,0,0,0),"fileName":"jieJieTuPo_5723.py"},


    {"fixdeTime":datetime.time(16,0,0,0),"fileName":"tansuo_5723.py"},
    {"fixdeTime":datetime.time(17,0,0,0),"fileName":"jieJieTuPo.py"},
    {"fixdeTime":datetime.time(18,0,0,0),"fileName":"jieJieTuPo_5723.py"},
    {"fixdeTime":datetime.time(20,0,0,0),"fileName":"add_10_food_5723.py"},
    {"fixdeTime":datetime.time(22,0,0,0),"fileName":"jieJieTuPo_5723.py"},


]

def run(now,*args):
    for subDic in args[0]:
        #print type(subDic),subDic
        if now.hour == subDic["fixdeTime"].hour and now.minute == subDic["fixdeTime"].minute:
            print "cmd : python  {fileName}".format(fileName=subDic["fileName"])
            os.system("python  {fileName}".format(fileName=subDic["fileName"]))
    return True


if __name__ == '__main__':

    print "this py script executed when windows starts,scheduled yinyangshi tasks are written down in this script!"
    print "we have the following tasks to be done:"
    for item in tasksList:
        print item
    while 1:
        now = datetime.datetime.now()

        run(now,tasksList)
        time.sleep(50)






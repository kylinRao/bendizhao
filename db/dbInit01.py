# coding=utf-8
#!/usr/bin/env python
import sqlite3
import os

import datetime
from time import sleep

import MySQLdb

from conf.globalFacts import loggerInner

DATABASE = os.path.join(os.path.dirname(__file__),"phone-db")
conn = sqlite3.connect(DATABASE)


# 创建表格、插入数据
def getDbConn():
    # DATABASE = r"D:\projects\github\rentPhoneServerManager\db\house.db";
    conn = MySQLdb.connect("192.168.1.112", "admin", "Huawei123", "adminserver", charset='utf8' )
    # conn = sqlite3.connect(DATABASE)
    return conn
def create_db():
    # 连接

    c = conn.cursor()
    with open('v1.0.sql', 'r') as f:
        # print(f.read())
        c.executescript(f.read())
        # 提交！！！
        conn.commit()
        # 关闭
        conn.close()
def exeSql(phone,inviteCode):
    conn = getDbConn()
    cur = conn.cursor()
    cur.execute("replace into phone values ('{time}','{phone}','{inviteCode}','2018-05-15')".format(time=datetime.datetime.now(),phone=phone,inviteCode=inviteCode))
    conn.commit()
def insertRelationShip(phoneSlaveList, inviteByCode):
    conn = getDbConn()
    cur = conn.cursor()
    for phone in phoneSlaveList:
        cur.execute("replace into inviteRelationship values ('{phone}','{inviteByCode}','{invitedTime}','2018-05-15')".format(phone=phone,inviteByCode=inviteByCode,invitedTime=datetime.datetime.now().date()))
    conn.commit()
def moveTodaySlave2Relationship():
    conn = getDbConn()
    cur = conn.cursor()
    cur.execute("SELECT * from phone WHERE updateTime LIKE '%2018-05-16%'")
    res = cur.fetchall()
    for data in res:
        print(data)
        phone = data[1]
        inviteByCode = data[2]
    # for phone in secondPhoneSlaveList:
        cur.execute("replace into inviteRelationship  values ('{phone}','{inviteByCode}','{invitedTime}','2018-05-15')".format(phone=phone,inviteByCode=inviteByCode,invitedTime=datetime.datetime.now().date()))
    conn.commit()
# 不允许其他的客户端读写该表
def lockTableForWrite():
    conn = getDbConn()
    cur = conn.cursor()
    cur.execute("SELECT GET_LOCK('inviteRelationship', 10)")
    # sleep(3)
    cur.execute("SELECT * from inviteRelationship WHERE invitedTime >= DATE_SUB(curdate(),INTERVAL -5 DAY)and lastUseDay !=DATE_SUB(curdate(),INTERVAL 0 DAY) ORDER BY phone LIMIT 1")
    res = cur.fetchall()
    try:

        for data in res:
            loggerInner.info("we got one phone to handle")
            print(data)
            phone = data[0]
            inviteByCode = data[1]
        cur.execute("update  inviteRelationship SET lastUseDay=DATE_SUB(curdate(),INTERVAL 0 DAY) WHERE phone={phone}".format(phone=data[0]))
        conn.commit()
    except:
        loggerInner.info("no more phone to handle ")
        cur.execute("SELECT RELEASE_LOCK('inviteRelationship')")
        # 没有号码要处理了，那么我们返回1
        return 1
    cur.execute("SELECT RELEASE_LOCK('inviteRelationship')")
    # 获取到要处理的电话，那么我们返回那个电话号码
    return phone







if __name__ == '__main__':
    # create_db()
    # #一号手机徒地信息插入
    # insertRelationShip(phoneSlaveList=['15504407547', '13162467935', '18507945612', '18507945612', '15543456049', '13157048692', '15643624784', '15584478689', '15543568045', '15584295953', '15543568842', '15643734149', '13157041976', '13059714670', '15584292949', '15584274563', '13157014284', '13059714946', '15584388445', '13116842875', '15643720041', '15584294149', '15584174783', '15584317904', '17096148904', '13059778545', '13059778545', '13451471491', '13216293334', '17071382057', '13162436125', '13059786545', '17073745815', '17194796424', '17096495343', '17189204113', '17183473938', '13184402707', '1713485442', '17135985442', '17084230635', '17167306405', '17190946187', '15543764948', '13059893946', '17078408959', '13175734904', '13083948160', '18474723433', '17184102343', '17086145159', '15504439548', '1554345064', '15543675064', '13059776494', '13122777412', '18474095703', '13162438121', '18474547920', '13175745645', '18473879572', '17071229149', '17094651351', '17086156991', '18474548127', '13157089094', '17071381760', '15584140229', '18474088926', '13162991828', '13261389048', '15567159743', '13068858259', '17073742850', '17073679853', '13162467086', '13162467017', '17192571445', '17190944586', '13282051484', '13175704820', '13175704475', '13105704389', '17133537184', '17096141484', '18408185132', '17131221843', '13286882335', '15543141280', '13157011524'],inviteByCode="A4844613")
    # # 二号手机徒弟信息插入
    # insertRelationShip(phoneSlaveList=["15543644903","17134212482",'17073740983','17097696070','13454476014','17184104597','17175430745','13122052425','13045702959','17070342618','17086143100','17080627254','15584140210','15671946574','17183800584','15543644167','13122612946','17186804914','17087016493','18340426404','17079474998','17195676805','15543555514','15568830340','15584157391','17083452618','17194954250','13261388841','17190945054','17134854425','15590577454','15506017724','15246371046','17139415049','17096271074','17074359273','17079474427','13282058476','13184400039','13175714503','13175714273'],inviteByCode="A4851172")
    moveTodaySlave2Relationship()


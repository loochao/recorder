#coding=utf-8
import pymongo
import bat
from cmd_tool import *

def check_rank_value():
    '''递归判断，获取正确的评分'''
    s = raw_input("(1~10):")
    try:
        rank = int(s)
    except ValueError, e:
        print u"请输入整数"
        return check_rank_value()
    else:
        # print rank
        if rank>=1 and rank<=10:
            # print u"已保存评分"
            return rank
        else:
            print u"超过范围"
            return check_rank_value()

class MyCMD(BaseCMD):
    '''命令行工具具体实现'''
    def __init__(self,db):
        BaseCMD.__init__(self)
        self.db = db
    def do_record(self,arg):
        sleep={}
        print u"睡眠质量评分:"
        sleep["rank"] = check_rank_value()
        sleep["describe"] = raw_input(u"关于昨晚到今早的睡眠质量描述：")
        shit = {}
        print u"排泄情况评分:"
        shit["rank"] = check_rank_value()
        shit["describe"] = raw_input(u"关于今天排泄状况的描述：")
        sport = {}
        print u"运动质量评分:"
        sport["rank"] = check_rank_value()
        sport["describe"] = raw_input(u"关于今天的运动质量描述：")
        press = {}
        print u"工作压力评分:"
        press["rank"] = check_rank_value()
        press["describe"] = raw_input(u"关于今天的工作压力描述：")
        all = {}
        print u"整天精神状态:"
        all["rank"] = check_rank_value()
        all["describe"] = raw_input(u"关于整天精神状态描述：")
        self.db.recorder.insert({'sleep':sleep,'shit':shit,'sport':sport,'press':press,'all':all})
    def do_look(self, arg):
        for i in self.db.recorder.find():
            print i
    def do_evaluate(self, arg):
        print u"暂时还没有评估功能"

if __name__=="__main__":
    # 打开mongodb本地服务端
    bat.open_mongo()
    # 创建mongodb客户端
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client.record_db  # 连接库
    mycmd = MyCMD(db)
    mycmd.cmdloop()


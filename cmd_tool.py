#coding=utf-8
import sys
import cmd
reload(sys)
sys.setdefaultencoding('gbk')

class BaseCMD(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(recoder)>'
        self.intro = u'''
            Recorder使用说明：
            Recorder是你的health的log。
            每天，系统都会自动启动。
            你需要按照提示手动输入健康信息。
            祝你身体永远健康。
            ^---^ ^---^ ^---^ ^---^ ^---^
            record(r)   开始记录
            look(l)     查看保存的数据
            evaluate(e) 查看评估
            EOF 退出系统
            '''

    def help_EOF(self):
        print u"===退出程序==="

    def do_EOF(self, line):
        sys.exit()

    def help_record(self):
        print u"===开始记录==="

    def do_record(self,arg):

        print u"今天的数据保存成功！"

    def help_look(self):
        print u"===查看保存的数据==="

    def do_look(self,arg):
        print u"查看数据"

    def help_evaluate(self):
        print u"===查看评估==="

    def do_evaluate(self,arg):
        print u"查看评估"

    def help_r(self):
        self.help_record()

    def do_r(self,arg):
        self.do_record(arg)

    def help_l(self):
        self.help_look()

    def do_l(self,arg):
        self.do_look(arg)

    def help_e(self):
        self.help_evaluate()

    def do_e(self,arg):
        self.do_evaluate(arg)

if __name__ == "__main__":
    mycmd = BaseCMD()
    mycmd.cmdloop()

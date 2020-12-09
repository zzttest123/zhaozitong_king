import  logging  ,os , pymysql

from  public import config

class OperationDbInterface(object):
    def __init__(self,host_db = 'localhost',user_db = 'root' , passwd_db = '123456',name_db = 'test_interface',port_db=3306,link_type = 0):
        """
        :param host_db: 数据库服务主机ip
        :param user_db: 数据库用户名
        :param passwd_db: 数据库密码
        :param name_db: 数据库名称
        :param port_db: 端口号
        :param link_type: 连接类型，用于设置输出数据时字典还是元组，默认是字典
        :return:游标
        """
        try:
            if link_type == 0:
                self.conn = pymysql.connect(host = host_db,user = user_db,passwd = passwd_db,
                                            db = name_db,port = port_db,charset = 'utf8',
                                            cursorclass = pymysql.cursors.DictCursor)  #创建数据库连接，返回字典
            else:
                self.conn = pymysql.connect(host=host_db, user=user_db, passwd=passwd_db, db=name_db, port=port_db,
                                    charset='utf8')  #创建数据库连接，返回元组
            self.cur = self.conn.cursor()
        except pymysql.Error as e :
            print("创建数据库连接失败| Mysql Error %d : %s" %(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',level=logging.DEBUG,format= '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

    def op_sql(self,condition):
        """

        :param condition: sql 语句
        :return: 字典形式
        """
        try:
            self.cur.execute(condition) #执行sql语句
            self.conn.commit() #提交游标数据
            result = {'code':'0000','message':'执行通用操作成功','date':[]}
        except pymysql.Error as e:
            self.conn.rollback() #执行回滚操作
            result = {'code': '9999', 'message': '执行通用操作异常', 'date': []}
            print("数据库错误| op_sql %d : %s" %(e.args[0],e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log',level=logging.DEBUG,format= '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

        return result
    #查询表中的单条数据
    def select_one(self,condition):
        """

        :param condition:
        :return:
        """
        try:
            rows_affect = self.cur.execute(condition)
            if rows_affect > 0 :
                results  = self.cur.fetchone() #获取一条结果
                result = {'code':'0000','message':'执行单条查询结果成功','date':results}
            else:
                result = {'code':'0000','message':'执行单条查询结果成功','date':[]}
        except pymysql.Error as e:
            self.conn.rollback()  # 执行回滚操作
            result = {'code': '9999', 'message': '执行通用操作异常', 'date': []}
            print("数据库错误| op_sql %d : %s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=config.src_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)




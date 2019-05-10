import pymysql


def connectDB():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "scrapy", charset='utf8')
    return db

def closeDB(db):
    # 关闭数据库连接
    db.close()

def insertDB(db,sql):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)

    if(affectRows<=0):
        raise Exception("affectRows<=0")

    db.commit()

def selectOneSql(sql,db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)
    data = cursor.fetchone()

    db.commit()

    return data,affectRows

def selectAllSql(sql,db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)
    data = cursor.fetchall()

    db.commit()

    return data,affectRows
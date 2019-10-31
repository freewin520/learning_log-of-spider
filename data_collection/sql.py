# *_*coding:utf-8 *_*
import pymysql

db = pymysql.connect(host='localhost',user='root',password='123',port=3306,db='spiders')
cursor = db.cursor()
#动态插入数据（只需要加入字典）
data = {
    'id':'20120002',
    'name':'Tom',
    'age':23
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
#如果数据主键存在则更新否则插入
sql = 'insert into {table}({keys}) values({values}) on duplicate key update '.format(table=table,keys=keys,values=values)
update = ','.join(["{key}=%s".format(key=key)for key in data])
sql += update
print(sql)
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
#删除数据
# sql = 'delete from {table} where {condition}'.format{table=table,condition=conditon}
#插入数据的一般方法
# sql = 'insert into students(id,name,age) values(%s,%s,%s)'
#更新数据
# sql = 'update students set age = %s where name = %s'
#查询数据
#sql = 'select * from students where age>= 20'
#cursor.execute(sql)
#one = cursor.fetchone()一般通过遍历fetchone()可以降低数据开销
#result = cursor.fetchall()结果为（（），（））

#显示数据库版本
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)
#创建数据库
# sql='CREATE DATABASE spiders DEFAULT CHARACTER SET utf8'
#创建数据表(意别打错)
# sql="create table if not exists students(id varchar(255) not null,name varchar(255) not null, " \
#     "age int not null, primary key (id))"
# cursor.execute(sql)
# db.close()


from gengmei_app.common.dbMysql import GMMysql

dev_id = "863308030651130"
dev_type = "android"

xiaomi = "4da5b6b6"
huawei = "MKJNW18516001634"
xiaomiplatformVersion = "9"
huaweiplatformVersion = "9"
vivo = "be8a9a6d"
vivoplatformVersion = "8.1.0"
oppoplatformVersion = "9"


# mysql配置
mysql_test = GMMysql('bj-cdb-6slgqwlc.sql.tencentcdb.com', '62120', 'work', 'Gengmei1', 'maidian_data')
# mysql_test = Mysql('bj-cdb-6slgqwlc.sql.tencentcdb.com', '62120', 'work', 'Gengmei1', 'maidian_data')
try:
	import pymysql

	pymysql.install_as_MySQLdb()
except Exception:
	# mysqlclient can be used instead of PyMySQL
	pass

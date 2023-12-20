import pymysql
import os
from datetime import datetime

# 连接数据库
connection = pymysql.connect(host='', user='', password='', db='')

try:
    with connection.cursor() as cursor:
        # 获取所有表名
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # 获取当前日期作为文档编写日期
        doc_date = datetime.now().strftime("%Y-%m-%d")

        # 创建 HTML 文件并写入头部信息、样式和文档编写日期
        html_file = open("database_docs.html", "w", encoding="utf-8")
        html_file.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>Database Documentation</title>\n<style>\n")
        html_file.write("table {\nborder-collapse: collapse;\nwidth: 100%;\n}\n")
        html_file.write("th, td {\npadding: 8px;\ntext-align: left;\nborder-bottom: 1px solid #ddd;\n}\n")
        html_file.write("th {\nbackground-color: #f2f2f2;\ncolor: black;\nfont-weight: bold;\n}\n")
        html_file.write("</style>\n</head>\n<body>\n<h2 style='text-align: center;'> 数据库字典序 </h2>\n")
        html_file.write("</style>\n</head>\n<body>\n<h3> Date："+doc_date+"</h3>\n")

        for table in tables:
            table_name = table[0]
            html_file.write(f"<h2>Table: {table_name}</h2>\n<table>\n<thead>\n<tr><th>Column Name</th><th>Data Type</th><th>Nullable</th><th>Key</th><th>Default Value</th><th>Extra</th><th>Comment</th></tr>\n</thead>\n<tbody>\n")

            # 获取表结构和字段备注
            cursor.execute(f"SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA, COLUMN_COMMENT FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table_name}'")
            columns = cursor.fetchall()

            for column in columns:
                column_name, column_type, is_nullable, column_key, column_default, extra, column_comment = column
                html_file.write(f"<tr><td>{column_name}</td><td>{column_type}</td><td>{is_nullable}</td><td>{column_key}</td><td>{column_default}</td><td>{extra}</td><td>{column_comment}</td></tr>\n")

            html_file.write("</tbody>\n</table>\n<br>\n")

        # 写入 HTML 文件尾部信息
        html_file.write("</body>\n</html>\n")

finally:
    connection.close()

# 关闭 HTML 文件
html_file.close()

# 打开生成的 HTML 文件
if os.name == 'nt':
    os.startfile("database_docs.html")
else:
    import subprocess
    subprocess.Popen(["open", "-a", "/Applications/Google\ Chrome.app", "database_docs.html"])
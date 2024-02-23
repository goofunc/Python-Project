from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pymysql

db_config = {
    'host': '',  # 数据库服务器地址
    'user': '',  # 数据库用户名
    'password': '',  # 数据库密码
    'database': '',  # 数据库名称
    'charset': 'utf8mb4',  # 字符编码
}






# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 访问目标网页
url = ""
driver.get(url)

# 等待页面加载完成（如果需要的话，可以添加更复杂的等待条件）
# driver.implicitly_wait(10)  # 单位为秒

#     var product_id = '489';
#     var further_zone    = [];
#     var manjian         = [];
#     var zhifu         = [];
#     var current_lang_code   = 'cn';
#     var current_zone_id     = '49';
#     var further_zone_freight = 200;
#     var chose_store_address = '请选择';
#     var region_id   = '49';
#     var is_zipcode  = '1';
#     var wrong_phone = "号码格式不正确，请重新填写！";
#     var name_1 = '姓名不能为空';
#     var mobile_2 = '手机号码不能为空';
#     var address_1 = '详细地址不能为空';
#     var email_1 = '邮箱格式不正确或不完整';
#     var postal_placeholder = '请输入邮编';
#     var error_postal = '请检查邮编';
#     var select_povince = '选择省份';
#     var select_city = '选择市区';
#     var selec_city = '选择市区';
#     var select_dis = '选择地区';
#     var chose_street = '';
#     var province_choose = "选择地区";
#     var unvalidate_code = "优惠码无效请重新填写";
#     var is_postal   = "2";
#     var is_email    = "2";




# 执行JavaScript代码以获取变量值
# 产品id
product_id = driver.execute_script("return window.product_id")

# 当前匹配语言
current_lang_code = driver.execute_script("return window.current_lang_code")

# 选择地址 请选择
chose_store_address = driver.execute_script("return window.chose_store_address")

# 号码提示 号码格式不正确，请重新填写！
wrong_phone = driver.execute_script("return window.wrong_phone")

# 姓名不能为空
name_1 = driver.execute_script("return window.name_1")

# 手机号不能为空
mobile_2 = driver.execute_script("return window.mobile_2")

# 详细地址不能为空
address_1 = driver.execute_script("return window.address_1")

# 邮箱格式不正确或不完整
email_1 = driver.execute_script("return window.email_1")

# 请输入邮编
postal_placeholder = driver.execute_script("return window.postal_placeholder")

# 请检查邮编
error_postal = driver.execute_script("return window.error_postal")

# 选择省份
select_povince = driver.execute_script("return window.select_povince")

# 选择市区
select_city = driver.execute_script("return window.select_city")

# 选择市区
selec_city = driver.execute_script("return window.selec_city")

# 选择地区
select_dis = driver.execute_script("return window.select_dis")

# 选择地区
province_choose = driver.execute_script("return window.province_choose")

# 优惠码无效请重新填写
unvalidate_code = driver.execute_script("return window.unvalidate_code")


# 建立数据库连接
connection = pymysql.connect(**db_config)

# 创建游标对象
cursor = connection.cursor()

try:
    # 创建游标对象
    with connection.cursor() as cursor:

        # 准备要插入的数据和SQL语句

        data_to_insert = (
        current_lang_code, chose_store_address, wrong_phone, name_1, mobile_2, address_1, email_1, postal_placeholder,
        error_postal, select_povince, select_city, selec_city, select_dis, province_choose, unvalidate_code)

        # SQL 插入语句
        sql_insert_query = """
            INSERT INTO local_language (current_lang_code,chose_store_address,wrong_phone,name_1,mobile_2,address_1,email_1,postal_placeholder,error_postal,select_povince,select_city,selec_city,select_dis,province_choose,unvalidate_code)
            VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)
        """

        # 执行 SQL 插入操作
        cursor.execute(sql_insert_query, data_to_insert)

        # 提交事务（对于支持事务的数据库）
        connection.commit()

except Exception as e:
    # 如果执行过程中发生错误，回滚事务
    connection.rollback()
    print(f"Error occurred: {e}")

finally:
    # 确保在所有情况下都关闭连接
    connection.close()





# 输出变量值

print('done!')



# 关闭浏览器
driver.quit()
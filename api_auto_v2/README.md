

# api_auto_v2

## 一、实现功能如下：

### 1、api_auto_v2功能

1. 对request进行封装，实现get/post请求；
2. 运行pytest框架，对相关接口进行参数化测试;
3. 保存读取cookie，方便后续接口使用；
4. 支持json、图片格式作为body发送post请求；
5. 关联Mysql数据库，并通过sqlalchemy进行数据的增改查；
6. 关联Redis数据库对数据进行查找、删除；
7. 根据不同的测试环境，选择host环境配置进行运行；
8. 生成Allure报告；
9. 生成swagger界面，直接通过接口调用方法；
10. 生成log，查看运行记录及后台返回；
11. 添加身份证、手机号码生成；
### 2、功能界面

#### 1）Log记录

![log.png](https://github.com/edrainann/python_interface_auto/raw/master/README_PHOTOS/log.png)

#### 2）Allure报告

![allure.png](https://github.com/edrainann/python_interface_auto/raw/master/README_PHOTOS/allure.png)

#### 3）Swagger界面

![swagger.png](https://github.com/edrainann/python_interface_auto/raw/master/README_PHOTOS/swagger.png)



## 二、代码分布结构如下：  

1. allure_report：allure生成的报告

   - data：存储数据
   - html：生成html
2. biz_service: 一些常用的服务
   - funding_serivce.py：放款服务
   - mysql_service.py：MySQL连接服务
   - read_env_service.py：读取环境服务
   - redis_service.py：Redis连接服务
3. common：公用文件夹，如短信、签约、贷后等
   - enums：常用的枚举
   - utils：常用的工具
      - config_headers_data.py.py：有关headers头的数据
      - generator_initial_data.py：生成初始数据
      - logger.py：生成的日志设定 
      - request.py：封装request请求
4. db_dal:
   - db_model：通过sqlacodegen，把已存在的数据库模型转为sqlalchemy的模型
5. env_config：各环境配置
4. log：记录执行接口测试后生成的log
7. project_interface：各个项目下的接口及数据
   - data：具体接口需要用到的数据
   - enums：具体项目需要的枚举
   - interface：具体接口
6. resource_files：需要上传的资源文件
7. swagger：通过flask_restplus生成swagger页面，直接通过URL执行用例
8. test_cases：测试用例
9. select_env.py：执行环境选择和主文件路径

## 三、需要用到指令

### 1、更新数据库对象

sqlacodegen使用方法----把已存在的数据库模型转为sqlalchemy的模型
如有数据库表或者字段更新，更进入db_dal/db_model路径下cmd执行以下命令，会自动生成（不加--table 表名参数表示整个库都会生成）

#### 1) 导出整个数据库

sqlacodegen --outfile=models.py mysql://root:password@127.0.0.1:3306/test_db
sqlacodegen --outfile=supply_chain_mapper.py mysql://this_is_username:this_is_password@127.0.0.19:3306/supplychain?charset=utf8 

#### 2) 导出某些表

格式：sqlacodegen 文件名 mysql://用户名:密码@IP:PORT/库名称?charset=utf8 --tables bs_white_list, sc_brand_info
例如：sqlacodegen --outfile supply_chain_model.py mysql://this_is_username:this_is_password@127.0.0.19:3306/supply?charset=utf8 --tables bs_white_lis
sqlacodegen --outfile=supply_chain_model.py mysql://this_is_username:this_is_password@127.0.0.19:3306/supply?charset=utf8 --tables sc_brand_info

### 2、生成allure报告

pytest -s -q --alluredir ./report/xml
allure generate report/xml -o report/html  --clean

#### 1) 先执行pytest，产生allure报告需要的数据

python -m pytest --alluredir=allure_report/data test_cases/supply_g31/g31_user/test_borrower_auth_sms_code_interface.py

#### 2）执行allure，生成allure报告，到指定目录

allure generate allure_report/data -o allure_report/html --clean 

### 3、涉及到的库

 使用`pipreqs`生成requirements.txt ，在需要生成的目录下执行：

`pipreqs ./ --encoding=utf-8 --force`

安装requirements.txt依赖

`pip install -r requirements.txt`




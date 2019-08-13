# api_auto_v1

## 一、实现功能如下：
api_auto_v1功能：
1. 对get/post接口进行封装，实现get/post请求；
2. 运行pytest框架;
3. 保存读取cookie，方便后续接口使用；
4. 支持json、图片格式作为body发送post请求；
5. 关联Mysql数据库进行数据的增改查；
6. 通过Yaml保存配置
7. 添加身份证、手机号码生成


## 二、代码分布结构如下：
1. api：保存系统的接口；  

2. data_config：保存用户数据、环境配置，存放请求中涉及到的header、data、cookies等数据；

3. py_requests：封装get/post、请求url、请求header、cookie、file、validate等；

4. testcases：test_user_flow.py 为用例用法的介绍，实际项目中可以按照不同模块新建，来存放不同模块的接口用例；

5. util: 对测试接口的相关方法的封装；

    use_data.py: 常用数据生成的相关方法

    use_mysql: 数据库关联的相关操作

    use_yaml: 读取保存yaml的相关操作

    ​
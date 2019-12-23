## api_auto_v2：
### 实现功能如下：

#### 1、api_auto_v2功能

1. 对request进行封装，实现get/post请求；
2. 运行pytest框架，对相关接口进行参数化测试;
3. 保存读取cookie，方便后续接口使用；
4. 支持json、图片格式作为body发送post请求；
5. 关联Mysql数据库，并通过sqlalchemy进行数据的增改查；
6. 关联Redis数据库对数据进行查找、删除；
7. 根据不同的测试环境，选择Env配置进行运行；
7. 生成Allure报告；
8. 生成swagger界面，直接通过接口调用方法；
9. 生成log，查看运行记录及后台返回；
10. 添加身份证、手机号码生成。

#### 2、功能界面

##### 1）Log记录

![image.png](https://upload-images.jianshu.io/upload_images/1683050-e54c9547ce46df72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##### 2）Allure报告

![image.png](https://upload-images.jianshu.io/upload_images/1683050-e1d1780f9060b3ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##### 3）Swagger界面

![image.png](https://upload-images.jianshu.io/upload_images/1683050-959718f3604aab70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## api_auto_v1：

使用pytest进行接口测试
#### 实现功能如下：
1. 对get/post接口进行封装，实现get/post请求；
2. 运行pytest框架;
3. 保存读取cookie，方便后续接口使用；
4. 支持json、图片格式作为body发送post请求；
5. 关联Mysql数据库进行数据的增改查；
6. 通过Yaml保存配置
7. 添加身份证、手机号码生成

---

## interface-demo03

满足基本的python自动化接口测试
#### 实现功能如下：
1. 通过Pandas读取excel处理数据；
2. 关联Mysql数据库进行数据的增改查
3. 对多个sheet进行处理运行
4. 添加身份证生成工具

---

## interface-demo02

可以通过excel对用例进行管理
#### 实现功能如下：
1. 通过excel管理测试用例；
2. 支持json、图片格式作为body发送post请求；
3. 对excel的测试数据进行变量处理，可以自动生成测试数据；
4. 保存cookie，方便后续接口使用；
5. 生成log，查看日志。

---

## interface-demo01

这是一个最最基本的python实现自动化接口的脚本。
#### 实现功能如下：
1. 对get/post接口进行封装，实现get/post请求；
2. 运行unittest框架，通过HTMLTestRunner生成测试报告；
3. 对报告进行邮件的发送。

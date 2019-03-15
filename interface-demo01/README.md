# interface-demo01

这是一个最最基本的python实现自动化接口的脚本。


## 一、实现功能如下：

1. 对get/post接口进行封装，实现get/post请求；
2. 运行unittest框架，通过HTMLTestRunner生成测试报告；
3. 对报告进行邮件的发送。

## 二、代码分布结构如下：

（1）main文件夹下的flow.py主运行文件，执行整体流程，运行之后可以生成相应的测试报告，并以邮件形式发送；

（2）report文件夹存放测试结果报告；

（3）test_case文件夹是存放测试用例。test_case01.py为用例用法介绍，实际项目中可以按照不同模块新建python package，来存放不同模块的接口用例；

（4）util对测试接口相关方法的封装：HTMLTestRunner.py对生成测试报告进行封装；send_mail.py对发送邮件进行封装；test_get_post.py对接口请求类型进行封装。

## 三、小tip

记得要在每个python文件夹下加上`__init_.py`文件喔~ 

主要作用：

（1）因为每个package实际上是一个目录（Directory),那么IDE是怎么识别它为package呢？`__init__.py`的第一个作用就是package的标识，如果没有该文件，该目录就不会认为是package。 作为Python中package的标识，不能删除 。

（2）定义__all__用来模糊导入 

（3）编写Python代码(不建议在`__init__.py`中写python模块，可以在包中在创建另外的模块来写，尽量保证`__init__.py`简单） 


# -*- coding:utf-8 -*-
import random
import urllib
import urllib2
'''#coding=utf-8'''
# print 'hello word'
'''
a = 'I want to eat'
print a
'''
# if 2 == 1:
#     print 'success'
# else:
#     print 'false'
# a = 'My name is Mrj'
# b = 'I am 18'
# print a,b
class Person():
    a = 2
    b = ''
    def __init__(self, userName):
        self.b = userName
    # def eat(self):
    #     self.b = 'nihao'
    #     return self.b,self.a
    def write(self):
        handle = open('one.txt','a+')
        handle.write('this is test a words\n')
        handle.close()
        fp = open('one.txt', 'r')
        str = fp.read(10)
        print(str)
    def rand_m(self):
        agent_list=[
            'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.1; chromeframe/12.0.742.100; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; chromeframe/12.0.742.100)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; InfoPath.3; .NET4.0C; .NET4.0E) chromeframe/8.0.552.224',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0 chromeframe/10.0.648.205)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        ]
        '''it = random.randint(0,8)
        headers = {'User-Agent': agent_list[it]}
        r = urllib2.Request('http://www.onethink.com/index.php/home/index/agent/name/xiaoma', '', headers)
        rel = urllib2.urlopen(r).read()
        print(rel)'''
        #异常处理的好处，解决程序中断
        '''try:
            f = open('one.txt', 'w')
        except BaseException as e:
            print(str(e))
        else:
            print('执行正常分支')
            f.close()
        print('执行下面的程序')'''
        '''f = open('one.txt', 'w')
        f.close()
        print('执行下面的程序')'''
        for i in range(1, 9):
            if i % 2 > 0:
                print i
            else:
                pass
one = Person('xiaoma')
one.rand_m()
# print one.eat()
# apple = int('4')
# weight = float('20')
# print(apple*weight)
# height = input('请输入你的身高 ')
# print(type('asdfsafd'))
# a = 22212
# if height > 45:
#     print ('你是小孩子'+"a")
# else:
#     print ('你是大人%d'%height)




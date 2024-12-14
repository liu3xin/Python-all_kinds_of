import time
from random import randint
import time

read_sign = input('是否读档(yes or no)')
if read_sign == 'yes':
    with open('存档.txt',mode = 'r',encoding = 'utf-8') as f:
        for line in f:
            money_cun = line.strip()
            money_cun = int(money_cun)
else:
    money_cun = 5
    
#设置局外数据
money = money_cun
s = 0
flag_ = True

class User:#创建玩家类
    
    def __init__(self,s,num):
        self.s = s
        self.money = money
        self.num = num
        
    def run(self):
        self.s += 1
        
    def printho(self):
        print(f'你的马当前以行走：{self.s}')
        if self.s == self.num:
            return 'user_win'
        
#创建人机类        
class Renji1:
    def __init__(self,s,num):
        self.s = s#初始化数据
        self.num = num
        
    def run(self):
        self.s += 1
        
    def printho(self):
        print(f'人机1当前以行走：{self.s}')
        if self.s == self.num:
            return 'renji1_win'
        
class Renji2:
    def __init__(self,s,num):
        self.s = s#初始化数据
        self.num = num
        
    def run(self):
        self.s += 1
        
    def printho(self):
        print(f'人机2当前以行走：{self.s}')
        if self.s == self.num:
            return 'renji2_win'
        
class Renji3:
    def __init__(self,s,num):
        self.s = s#初始化数据
        self.num = num
        
    def run(self):
        self.s += 1
        
    def printho(self):
        print(f'人机3当前以行走：{self.s}')
        if self.s == self.num:
            return 'renji3_win'
        
def main(s):
    flag = True
    global money
    print(f'你还有{money}元')
    colorlist = ['红桃','红方片','黑桃','黑花']
    c1 = randint(0,3)
    color_1 = colorlist.pop(c1)
    colorlist.append(colorlist[0])

    c2 = randint(0,3)
    color_2 = colorlist.pop(c2)
    while color_2 in colorlist:
        colorlist.remove(color_2)
    while len(colorlist) != 4:
        colorlist.append(colorlist[0])
    
    c3 = randint(0,3)
    color_3 = colorlist.pop(c3)
    while color_3 in colorlist:
        colorlist.remove(color_3)
    while len(colorlist) != 4:
        colorlist.append(colorlist[0])
            
    c4 = randint(0,3)
    color_4 = colorlist.pop(c4)
    num = int(input('请输入跑到距离'))
    user = User(s,num)
    renji1 = Renji1(s,num)
    renji2 = Renji2(s,num)
    renji3 = Renji3(s,num)
    print('已创建完毕角色')
    print(f'''你的马花色是{color_1};
人机1马花色是{color_2};
人机2马花色是{color_3};
人机3马花色是{color_4};''')
    ya = int(input('请输入押注金额'))
    while flag:
        sign = randint(1,4)
        if sign == 1:
            print(f'花色是{color_1}')
            user.run()
        elif sign == 2:
            print(f'花色是{color_2}')
            renji1.run()
        elif sign == 3:
            print(f'花色是{color_3}')
            renji2.run()
        else:
            print(f'花色是{color_4}')
            renji3.run()
            
        win_1 = user.printho()
        win_2 = renji1.printho()
        win_3 = renji2.printho()
        win_4 = renji3.printho()
        
        if win_1 == 'user_win':
            print('you win')
            money += ya*4
            flag = False
        elif win_2 == 'renji1_win':
            print('renji1 win')
            money -= ya
            flag = False
        elif win_3 == 'renji2_win':
            print('renji2 win')
            money -= ya
            flag = False
        elif win_4 == 'renji3_win':
            print('renji3 win')
            money -= ya
            flag = False
        else:
            nextt = input('输入任意符号继续(close即可退出)')
            if nextt == 'close':
                flag = False
                print('退出')
        
while flag_:
    main(s)
    again = input('这局已经结束，是否继续（no或任意键继续）')
    if again == 'no':
        print('游戏结束')
        read2_sign = input('是否存档(yes or no)')
        if read2_sign == 'yes':
            money = str(money)
            with open('存档.txt',mode = 'w',encoding = 'utf-8') as f:
                f.write(money)
        print('ok,再见')
        time.sleep(3)
        flag_ = False
        
    else:
        main(s)

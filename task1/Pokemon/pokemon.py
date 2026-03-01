from __future__ import annotations
import re
import time
import random
from typing import Literal 
MyPokemon:Pokemon = None
ComputerPokemon:Pokemon = None
turn:int = 1
class Pokemon(object):
    name:str = '未知'
    attribute:Literal['草','火','水','电','未知']  = '未知'
    is_getdamage: bool = False
    is_madedamage: bool = False
    is_dodge: bool = False
    jianshangxishu=1
    spacialstatus:Literal['麻痹','中毒','烧伤','正常'] = '正常'
    turn = 1
    is_Parasitic=0
    skill=[]
    action=0
    specialaction=0
    attacklevel=0           #能力等级
    defencelevel=0
    speedlevel=0
    attackdebuff=1.0
    defencedebuff=1.0
    speeddebuff=1.0
    def __init__(
        self,
        hp: int,
        attack: int,
        defence: int,
        dodge: float,
        experience: int,
        speed: int,
        is_man:bool
    ):
        self.hp = hp                    #最大生命值
        self.currenthp=self.hp
        self.attack = attack            #初始攻击力
        self.currentattack = self.attack
        self.defence = defence
        self.currentdefence=self.defence
        self.dodge = dodge
        self.speed = speed
        self.currentspeed=self.speed
        self.is_man = is_man
        
    def specialattribute(self,opponent:Pokemon):
        pass
    @classmethod
    def Attack(cls,me:Pokemon,opponent:Pokemon,damage:float):
        if not judgedodge(opponent.dodge):
            opponent.is_getdamage=True              #受击判定
            opponent.specialattribute(opponent)     #调用特性函数
            if judgedamage(me,opponent,damage):     #攻击判定
                me.is_madedamage = True
                me.specialattribute(opponent)       #调用特性函数 
            return True    
        else:
            dodge(me,opponent)                      #成功闪避
            return False
    def Action(self,opponent:Pokemon):
        pass

class electricalPokemon(Pokemon):
    attribute = "电"

    def specialattribute(self,opponent:Pokemon):
        if self.is_dodge:                       #再次进行攻击
            self.is_dodge=False
            print('闪避成功,触发特性 弹反,请选择一个技能进行攻击：')
            if self.is_man:                     #是玩家
                self.action = checkinput(2)
                self.Action(opponent)  
            else :                              #是电脑
                time.sleep(1)
                self.action = random.randint(1,2)
                self.Action(opponent)
            
            
class waterPokemon(Pokemon):
    attribute = "水"

    def specialattribute(self,opponent:Pokemon):
        if self.is_getdamage:
            if judgedodge(0.5):#有 50% 的几率减免 30% 的伤害
                print(f'{self.name} 触发特性激流,减免 30% 的伤害')
                self.jianshangxishu-=0.3
            self.is_getdamage=False

class firePokemon(Pokemon):
    attribute = "火"

    def specialattribute(self,opponent:Pokemon):
        if self.is_madedamage :
            if self.attacklevel < 4:
                print(f'成功命中,{self.name}增加一级攻击力')
                self.attacklevel += 1
                self.is_madedamage=False
            else :
                print('攻击力已经升到最高级')
        self.currentattack = int((self.attack + self.attacklevel*0.1*self.attack)*self.attackdebuff) #计算总攻击力   

class plantPokemon(Pokemon):
    attribute = "草"
    def specialattribute(self,opponent:Pokemon):             #吃草
        global turn
        if turn-self.turn == 1:
            self.currenthp = int(self.currenthp + self.hp * 0.1)
            if self.currenthp > self.hp:
                self.currenthp = self.hp
            print(f'{self.name} 触发特性食草,恢复10%HP!{self.currenthp}/{self.hp}')

class PikaChu(electricalPokemon):
    name='皮卡丘'
    skill=['十万伏特','电光一闪']
    def Action(self,opponent:Pokemon):
        if self.action == 1 :
            self.Thunderbolt(opponent)
        elif self.action == 2:
            self.Quick_Attack(opponent)
    def Thunderbolt(self,opponent:Pokemon):     #十万伏特
        print(f'{self.name} 使用了 十万伏特！')
        damage = 1.4*self.currentattack
        if super().Attack(self,opponent,damage):#攻击到了
            if judgedodge(0.1):                 #判定麻痹
                if is_zhengchang(opponent):
                    opponent.spacialstatus='麻痹'
                    print(f'{opponent.name} 被麻痹了')    
        
    def Quick_Attack(self,opponent:Pokemon):    #电光一闪
        print(f'{self.name} 使用了 电光一闪！')
        damage = float(self.currentattack)
        super().Attack(self,opponent,damage)
        if judgedodge(0.1):                     #判定是否进行下一次攻击
            print(f'{self.name} 再次使用了 电光一闪！')
            super().Attack(self,opponent,damage)
                
            
class SeedBomb(plantPokemon):
    name='妙蛙种子'
    skill=['种子炸弹','寄生种子']
    def Action(self,opponent:Pokemon):
        if self.action == 1 :
            self.Seed_Bomb(opponent)
        elif self.action == 2:
            self.Parasitic_Seeds(opponent)
    def Seed_Bomb(self,opponent:Pokemon): #种子炸弹
        print(f'{self.name} 使用了 种子炸弹！')
        damage=float(self.currentattack)
        if super().Attack(self,opponent,damage): #如果打到了
            if judgedodge(0.15):                                    #判定中毒
                if is_zhengchang(opponent):
                    opponent.spacialstatus='中毒'
                    print(f'{opponent.name} 中毒了')
    def Parasitic_Seeds(self,opponent:Pokemon):   #寄生种子
        print(f'{self.name} 使用了 寄生种子')
        print(f'{opponent.name}被寄生了')
        opponent.is_Parasitic=3
        

class Squirtle(waterPokemon):
    name = '杰尼龟' 
    skill=['水枪','保护']
    def Action(self,opponent: Pokemon):
        if self.action == 1:
            self.Aqua_Jet(opponent)
        elif self.action == 2:
            self.Shield(opponent)
        
    def Aqua_Jet(self,opponent:Pokemon):        #水枪
        print(f'{self.name} 使用了水枪！')
        damage = 1.5*self.currentattack
        super().Attack(self,opponent,damage)    #调用伤害函数造成伤害
    def Shield(self,opponent:Pokemon):
        print(f'{self.name} 使用了保护！')
        self.jianshangxishu-=0.5

class Charmander(firePokemon):
    name = '小火龙'
    skill=['火花','蓄能爆炎']
    def Action(self, opponent: Pokemon):
        if self.action == 1:
            self.Ember(opponent)
        elif self.action == 2:
            self.Flame_Charge(opponent)
    def Ember(self,opponent:Pokemon):
        print(f'{self.name} 使用了火花！')
        damage=self.currentattack*1
        if super().Attack(self,opponent,damage):  #如果打到了
            if judgedodge(0.1):                   #判定烧伤
                if is_zhengchang(opponent):
                    opponent.spacialstatus='烧伤'
                    print(f'{opponent.name} 烧伤了')
    def Flame_Charge(self,opponent:Pokemon): 
        if self.specialaction == 0:
            print(f'{self.name} 使用了蓄能爆炎,正在蓄力')
            self.specialaction = 1
        elif self.specialaction == 1:
            print(f'{self.name} 召唤出强大火焰')
            damage = self.currentattack*3
            opponent.dodge+=0.2                       #敌方闪避率增加 20%
            if super().Attack(self,opponent,damage):  #如果打到了
                if judgedodge(0.8):                   #判定烧伤
                    if is_zhengchang(opponent):
                        opponent.spacialstatus='烧伤'
                        print(f'{opponent.name} 烧伤了')
            opponent.dodge-=0.2                       #敌方闪避率复原
            self.specialaction = 0                    #回到未蓄力状态

def is_zhengchang(pokemon:Pokemon):
    if pokemon.spacialstatus=='正常':
        return True
    else :
        return False


def dodge(me:Pokemon,opponent:Pokemon):
    print(f'{opponent.name} 躲避了这次攻击')
    opponent.is_dodge=True              #成功闪避
    opponent.specialattribute(me)

def judgedodge(dodge:float):
    if random.random()<dodge:
        return True
    else :
        return False

def judgedamage(me:Pokemon,opponent:Pokemon,damage:float):
    kezhi = is_kezhi(me.attribute,opponent.attribute)
    if kezhi == '克制':
        damage=int(damage*2*opponent.jianshangxishu)
        return is_defence(opponent,damage)
    elif kezhi == '被克制':
        damage=int(damage/2*opponent.jianshangxishu)
        return is_defence(opponent,damage)
    elif kezhi =='没有克制关系':
        damage=int(damage)
        return is_defence(opponent,damage)

def is_kezhi(myattribute:Literal['草','火','水','电','未知'],opponentattribute:Literal['草','火','水','电','未知']) -> Literal['克制','被克制','没有克制关系']:#判断属性克制
    if myattribute == '草' :
        if opponentattribute == '水':       #草克水
            return '克制'   
        elif opponentattribute == '火':      #火克草
            return '被克制'
        else :                              #没有克制关系     
            return '没有克制关系'
    elif myattribute == '火'   :     
        if opponentattribute=='草':         #火克草
            return '克制'
        elif opponentattribute=='水':       #水克火
            return '被克制'
        else :                              #没有克制关系
            return '没有克制关系'
    elif myattribute == '水'    :
        if opponentattribute =='火':        #水克火
            return '克制'
        elif opponentattribute=='电':       #水被电克
            return '被克制'
        elif opponentattribute=='草':       #水被草克
            return '被克制'
        else:                                   #没有克制关系
            return '没有克制关系'
    elif myattribute == '电'    :   
        if opponentattribute == '水':       #电克水
            return '克制'
        elif opponentattribute == '草':     #电被草克
            return '被克制'
        else:                                   #没有克制关系
            return '没有克制关系' 
        
def is_defence(opponent:Pokemon,damage:int): #判断防御和攻击的关系
    if opponent.defence>=damage:
        print(f'{opponent.name}防住了这次攻击,剩余HP:{opponent.currenthp}/{opponent.hp}')
        return False
    else:
        
        opponent.currenthp=opponent.currenthp+opponent.defence-damage
        if opponent.currenthp<0:
            opponent.currenthp=0
        print(f'{opponent.name} 受到了 {damage-opponent.defence}点伤害！剩余HP:{opponent.currenthp}/{opponent.hp}')
        return True
def choose(player:str,pokemon:Pokemon,num:int) -> Pokemon:
    if num == 1:
        pokemon=PikaChu(80,35,5,0.3,0,90,True)
        print(f'{player}选择了 {pokemon.name}！')
        return pokemon
    elif num == 2:
        pokemon=SeedBomb(100,35,10,0.1,0,45,True)
        print(f'{player}选择了 {pokemon.name}！')
        return pokemon
    elif num == 3:
        pokemon=Squirtle(80,25,20,0.2,0,43,True)
        print(f'{player}选择了 {pokemon.name}！')
        return pokemon
    elif num == 4:
        pokemon=Charmander(80,35,15,0.1,0,65,True)
        print(f'{player}选择了 {pokemon.name}！')
        return pokemon
def checkinput(j):
    while True:
        x=input()
        res= re.match(f"[1-{j}]",x)   #匹配1-j
        if  res:
            return int(res.group())#字符串转数字
        else :
            print('非法输入，请重新输入')
def chooseyourpokemon():
    # try:
    #     with open("data.json", "r", encoding="utf-8") as pf:
    #         data: dict = json.load(pf)
    # except Exception as e:
    print("请选择 1 个宝可梦作为你的伙伴")
    print(
        "1. 皮卡丘（电属性） 2. 妙蛙种子（草属性） 3. 杰尼龟（水属性） 4. 小火龙（火属性）"
    )
    print("输入数字选择你的宝可梦：", end="")
    global MyPokemon
    global ComputerPokemon
    num = checkinput(4)
    MyPokemon=choose('你',MyPokemon,num)
    ComputerPokemon=choose('电脑',ComputerPokemon,4)
    time.sleep(2)


def Calculatedebuff(pokemon:Pokemon):            #计算负面状态
    if pokemon.spacialstatus=='麻痹':
        pokemon.speeddebuff=0.5                 #速度减半

    elif pokemon.spacialstatus=='中毒':
        pokemon.currenthp=int(pokemon.currenthp-pokemon.hp*0.125)
        print(f'{pokemon.name} 受到中毒的影响,减少{pokemon.hp*0.125}点HP,当前HP{pokemon.currenthp}/{pokemon.hp}')
        pokemon.defencedebuff=0.5                #防御减半
        time.sleep(1)

    elif pokemon.spacialstatus=='烧伤':
        pokemon.currenthp=int(pokemon.currenthp-pokemon.hp*0.1)
        print(f'{pokemon.name} 受到烧伤的影响,减少{pokemon.hp*0.1}点HP,当前HP{pokemon.currenthp}/{pokemon.hp}')
        pokemon.attackdebuff=0.5                #攻击减半
        time.sleep(1)
    elif pokemon.spacialstatus=='正常':
        pokemon.attackdebuff=1
        pokemon.defencedebuff=1
        pokemon.speeddebuff=1
def Parasitic_Seeds(me:Pokemon,opponent:Pokemon):
    if opponent.is_Parasitic:
        gethp=int(opponent.hp*0.1)
        opponent.currenthp=opponent.currenthp-gethp
        if opponent.currenthp<0:
            opponent.currenthp=0
        print(f'{opponent.name} 受到种子的影响,减少{gethp}点HP,剩余HP:{opponent.currenthp}/{opponent.hp}')
        me.currenthp+=gethp
        if me.currenthp>me.hp:
            me.currenthp=me.hp
        print(f'{me.name} 回复{gethp}点HP,剩余HP:{me.currenthp}/{me.hp}')
        opponent.is_Parasitic-=1
        


def Calculate(me:Pokemon,opponent:Pokemon):
    if me.currentspeed > opponent.currentspeed:
        host=me
        guest=opponent
    else :
        host=opponent
        guest=me
    Parasitic_Seeds(host,guest)
    Parasitic_Seeds(guest,host)
    Calculatedebuff(host)
    Calculateability(host)
    init(host)
    Calculatedebuff(guest)
    Calculateability(guest)
    init(guest)

def Calculateability(pokemon:Pokemon):           #计算能力值
    pokemon.currentattack=int((pokemon.attack+pokemon.attacklevel*0.1*pokemon.attack)*pokemon.attackdebuff)
    pokemon.currentdefence=int((pokemon.defence+pokemon.defencelevel*0.1*pokemon.defence)*pokemon.defencedebuff)
    pokemon.currentspeed=int((pokemon.speed+pokemon.speedlevel*0.1*pokemon.speed)*pokemon.speeddebuff)
def init(host:Pokemon):
    host.is_dodge=False
    host.is_getdamage=False
    host.is_madedamage=False
def startgame():
    global MyPokemon
    global ComputerPokemon
    global turn
    while MyPokemon.currenthp>0 and ComputerPokemon.currenthp>0:
        if MyPokemon.currentspeed>=ComputerPokemon.currentspeed:                  #根据速度判定谁先手
            host=MyPokemon
            guest=ComputerPokemon
        else :
            host=ComputerPokemon
            guest=MyPokemon
        print(f'----------第{turn}回合----------')
        print(f'你的 {MyPokemon.name} 的HP:{MyPokemon.currenthp}/{MyPokemon.hp},攻击力:{MyPokemon.currentattack}/{MyPokemon.attack},防御力:{MyPokemon.currentdefence}/{MyPokemon.defence}')
        print(f'对手的 {ComputerPokemon.name} 的HP:{ComputerPokemon.currenthp}/{ComputerPokemon.hp}')
        print(f'你的 {MyPokemon.name} 的技能：')
        for i in range(len(MyPokemon.skill)):
            print(f'{i+1}. {MyPokemon.skill[i]}')
        if MyPokemon.specialaction == 0:   #未在蓄力
            print('请选择一个技能进行攻击：')
            MyPokemon.action = checkinput(2)
        else :
            print('正在蓄力，无法使用其他技能')
        # print('电脑选择一个技能进行攻击：')
        if ComputerPokemon.specialaction == 0:   #未在蓄力
            print('请选择一个技能进行攻击：')
            ComputerPokemon.action = checkinput(2)
        else :
            print('正在蓄力，无法使用其他技能')
        host.jianshangxishu=1
        host.Action(guest)
        if guest.currenthp<=0:
            return host
        time.sleep(1)
        guest.jianshangxishu=1
        guest.Action(host)    
        if host.currenthp<=0:
            return guest
        time.sleep(1)
        Calculate(MyPokemon,ComputerPokemon) #结算状态
        turn+=1    
        host.specialattribute(guest)         #调用双方的特性
        guest.specialattribute(host)
        host.turn=turn
        guest.turn=turn
        time.sleep(2)
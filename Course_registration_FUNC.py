def department(dp):
    if dp=='機械':
        a='11'
    elif dp=='機シ':
        a='12'
    elif dp=='電通':
        a='13'
    elif dp=='医用':
        a='14'
    elif dp=='応化':
        a='15'
    elif dp=='原子':
        a='16'
    elif dp=='自然':
        a='17'
    elif dp=='情科':
        a='21'
    elif dp=='知能':
        a='22'
    elif dp=='通信':
        a=''
    elif dp=='建築':
        a='31'
    elif dp=='都市':
        a='32'
    elif dp=='都生':
        a='41'
    elif dp=='児童':
        a='51'
    elif dp=='環境':
        a='61'
    elif dp=='社メ':
        a='71'
    elif dp=='情シス':
        a='72'
    return a

def departmentjunp_short(dp):
    if dp=='11':
        a='機械'
    elif dp=='12':
        a='機シ'
    elif dp=='13':
        a='電通'
    elif dp=='14':
        a='医用'
    elif dp=='15':
        a='応化'
    elif dp=='16':
        a='原子'
    elif dp=='17':
        a='自然'
    elif dp=='21':
        a='情科'
    elif dp=='22':
        a='知能'
    elif dp=='31':
        a='建築'
    elif dp=='32':
        a='都市'
    elif dp=='41':
        a='都生'
    elif dp=='51':
        a='児童'
    elif dp=='61':
        a='環境'
    elif dp=='71':
        a='社メ'
    elif dp=='72':
        a='情シス'
    return a

def departmentjunp(dp):
    if dp=='11':
        a='機械工学科'
    elif dp=='12':
        a='機械システム工学科'
    elif dp=='13':
        a='電気電子通信工学科'
    elif dp=='14':
        a='医用工学科'
    elif dp=='15':
        a='応用化学科'
    elif dp=='16':
        a='原子力安善工学科'
    elif dp=='17':
        a='自然科学科'
    elif dp=='21':
        a='情報科学科'
    elif dp=='22':
        a='知能情報工学科'
    elif dp=='31':
        a='建築学科'
    elif dp=='32':
        a='都市工学科'
    elif dp=='41':
        a='都市生活学科'
    elif dp=='51':
        a='児童学科'
    elif dp=='61':
        a='環境'
    elif dp=='71':
        a='社メ'
    elif dp=='72':
        a='情シス'
    return a


def day(j):
    #これは使われていない
    if j==0:
        a='月'
    elif j==1:
        a='火'
    elif j==2:
        a='水'
    elif j==3:
        a='木'
    elif j==4:
        a='金'
    elif j==5:
        a='土'
    return a


def seme(time):
    #これも使われていない
    if time[0]=='前':
        if time[-1]=='期':
            a=5
        elif time[-1]=='前':
            a=1
        elif time[-1]=='後':
            a=2
        elif time[-1]=='中':
            a=9
    elif time[0]=='後':
        if time[-1]=='期':
            a=7
        elif time[-1]=='前':
            a=3
        elif time[-1]=='後':
            a=4
        elif time[-1]=='中':
            a=10
    return a
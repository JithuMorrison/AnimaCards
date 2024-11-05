import random as r
import colorama as col
import turtle
import colorsys
h=j=10000
phoenix1=phoenix2=pofo1=pofo2=0
leo=bg=pol=un1=un2=0
ost1=ost2=hip=1
lp1=lp2=ph1=ph2=pof1=pof2=lop1=lop2=tit1=tit2=arg1=arg2=1
sn1=sn2=kc1=kc2=sp1=sp2=bw1=bw2=sco1=sco2=hy1=hy2=an1=an2=pk1=pk2=0
fox=0
c=[]
kit=0
weadict={1:"🌧️",2:"☀️",3:"🌨️",4:"🌩️",5:"🌌"}
terdict={1:"❄️",2:"⛰",3:"🍂",4:"🏜️",5:"🌲",6:"🏞️",7:"🌋"}
a=["bull shark","bacteria","elephant","kangaroo","cheetah","leopard","jaguar","lion","parrot","porcupine","ostrich","snake","king cobra","spider","rhino","scorpion","horse","gorilla","hippo","blue glaucus","komodo dragon","orca","mandarin duck","tiger","donkey","blob fish","honey badger","mandarin fish","tarantula","polar bear","fox","arctic fox","chameleon","peregine falcon","black marlin","pronghorn","koala","panda","mudskipper","peacock","penguin","saltwater croc","great white shark","crow","salamander","ibex","camel","coyote","bat","owl","cassowary"]
an=["trex","stego","whale","black widow","titanboa","anaconda","mammoth","velociraptor","therizinosaur","wooly rhino","smilodon","thylacoleo","dunkleosteus","megalodon","titanis","argentavis"]
al=["dragon","hydra","unicorn","kitsune","phoenix","centaur"]
p=True
che=0
k=True
def leeo(leo,bg,pol):
  if leo==1:
    return 0
  if bg==1:
    return -1
  if pol==1:
    return 0.5
  else:
    return 1
def uno(un):
  if un>=1:
    return -1
  else:
    return 1

    
while k==True:


  
  if p==True:
    vi=h
    ki=j
    che=0
    print()
    print(col.Fore.CYAN+"Player1"+col.Fore.WHITE)
    list=c
    c=[]
    for i in range(3):
      rand=r.randint(0,1000)
      if rand<860:
        p=r.choice(a)
      if 865>rand>=860:
        p=r.choice(al)
      if rand>=865:
        p=r.choice(an)
      c.append(p)
    print(c)
    weather=r.randint(1,5)
    terrain=r.randint(1,7)
    if weather==1:
      weathe="rain"
    if weather==2:
      weathe="sunny"
    if weather==3:
      weathe="snow"
    if weather==4:
      weathe="lightning"
    if weather==5:
      weathe="night"
    if terrain==1:
      terrai="glacier"
    if terrain==2:
      terrai="mountain"
    if terrain==3:
      terrai="swamp"
    if terrain==4:
      terrai="desert"
    if terrain==5:
      terrai="forest"
    if terrain==6:
      terrai="river"
    if terrain==7:
      terrai="volcano"
    print(weadict[weather],end="  ")
    print(terdict[terrain])
    print("💀",sn2,kc2,pk2,sp2,bw2,sco2,hy2,"🔁",un2,"🌀",an2,"🔥",phoenix2,pofo2)
    if fox!=1:
      n=input("select a card: ")
      while n not in c:
        print("Error")
        n=input("select a card: ")
    if fox==1:
      fox=0
      n="nothing"
    if n=="crow":
      jj=r.randint(0,100)
      while n=="crow":
        c=[]
        if jj==81:
          for i in range(3):
            jjl=r.choice(al)
            c.append(jjl)
        if jj<81:
          for i in range(3):
            jjl=r.choice(a)
            c.append(jjl)
        if jj>81:
          for i in range(3):
            jjl=r.choice(an)
            c.append(jjl)
        print(c)
        n=input("select a card: ")
        while n not in c:
          print("Error")
          n=input("select a card: ")
    if n=="bull shark":
      h=h-c.count(n)*130*leeo(leo,bg,pol)*uno(un2)
    if n=="koala":
      koala=r.randint(0,10)
      h=h-c.count(n)*(((koala)**2)+7)*leeo(leo,bg,pol)*uno(un2)
    if n=="panda":
      koala=r.randint(0,10)
      h=h-c.count(n)*((koala)**2)*7*leeo(leo,bg,pol)*uno(un2)
    if n=="salamander":
      kole=[]
      typo=("fire","poison","beast","heal")
      for i in range(3):
        koal=r.choice(typo)
        kole.append(koal)
      print(kole)
      huo=input("enter type: ")
      if huo =="fire":
        pof1=256
      if huo=="poison":
        pk1=1
      if huo=="beast":
        h=h-c.count(n)*70*leeo(leo,bg,pol)*uno(un2)
      if huo=="heal":
        j=j+c.count(n)*80*leeo(leo,bg,pol)*uno(un2)
    if n=="tarantula":
      h=h-c.count(n)*25*leeo(leo,bg,pol)*uno(un2)
      kc2=sn2=sp2=bw2=sco2=0
    if n=="elephant":
      h=h-c.count(n)*350*leeo(leo,bg,pol)*uno(un2)
    if n=="orca":
      h=h-c.count(n)*1900*leeo(0,bg,pol)*uno(un2)
    if n=="blob fish":
      h=h-c.count(n)*65*leeo(leo,0,pol)*uno(un2)
    if n=="honey badger":
      h=h-c.count(n)*400*uno(un2)
    if n=="tiger":
      if leeo(leo,0,0)==0:
        h=h-c.count(n)*315*leeo(0,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*105*leeo(0,bg,pol)*uno(un2)
    if n=="mammoth":
      if leeo(0,0,pol)==0.5:
        h=h-c.count(n)*1350*leeo(leo,bg,0)*uno(un2)
      else:
        h=h-c.count(n)*350*leeo(leo,bg,0)*uno(un2)
    if n=="smilodon":
      if leeo(0,0,pol)==0.5:
        h=h-c.count(n)*700*leeo(leo,bg,0)*uno(un2)
        leo=2
      else:
        h=h-c.count(n)*350*leeo(leo,bg,0)*uno(un2)
    if n=="thylacoleo":
      if leeo(0,0,pol)==0.5:
        h=h-c.count(n)*250*leeo(leo,bg,0)*uno(un2)
      else:
        h=h-c.count(n)*750*leeo(leo,bg,0)*uno(un2)
    if n=="wooly rhino":
      h=h-c.count(n)*660*leeo(leo,bg,0)*uno(un2)
      j=j+c.count(n)*450*uno(un2)
    if n=="titanboa":
      if leeo(leo,0,0)==0 or leeo(0,bg,0)==-1:
        h=h-c.count(n)*1000*uno(un2)
      else:
        h=h-c.count(n)*40*uno(un2)
    if n=="mandarin fish":
      if leeo(0,bg,0)==-1:
        h=h-c.count(n)*555*leeo(leo,0,pol)*uno(un2)
      else:
        h=h-c.count(n)*5*leeo(leo,0,pol)*uno(un2)
    if n=="kangaroo":
      h=h-c.count(n)*160*leeo(leo,bg,pol)*uno(un2)
    if n=="gorilla":
      h=h-(c.count(n)**c.count(n))*130*leeo(leo,bg,pol)*uno(un2)
    if n=="horse":
      hoi=r.randint(0,10)
      if hoi==7:
        h=h-c.count(n)*746*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*70*leeo(leo,bg,pol)*uno(un2)
    if n=="dunkleosteus":
      hoi=r.randint(0,100)
      if hoi==81:
        h=h-c.count(n)*8100*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*1100*leeo(leo,bg,pol)*uno(un2)
    if n=="megalodon":
      h=h-c.count(n)*4000*leeo(leo,bg,pol)*uno(un2)
    if n=="fox":
      hoi=r.randint(1,2)
      if hoi==1:
        h=h-c.count(n)*140*leeo(leo,bg,pol)*uno(un2)
      else:
        fox=1
    if n=="chameleon":
      fox=1
    if n=="arctic fox":
      hoi=r.randint(1,2)
      if hoi==1:
        h=h-c.count(n)*70*leeo(leo,bg,pol)*uno(un2)
        pol=2
      else:
        fox=1
    if n=="donkey":
      hoi=r.randint(0,10)
      if hoi==5:
        j=j+c.count(n)*250*uno(un2)
      else:
        j=j+c.count(n)*70*uno(un2)
    if n=="unicorn":
      j=j+c.count(n)*8000*uno(un2)
    if n=="bacteria":
      j=j+c.count(n)*200*uno(un2)
    if n=="trex":
      h=h-c.count(n)*1280*leeo(leo,bg,pol)*uno(un2)
    if n=="komodo dragon":
      if "komodo dragon" in list:
        h=h-c.count(n)*250*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*60*leeo(leo,bg,pol)*uno(un2)
    if n=="stego":
      h=h-c.count(n)*880*leeo(leo,bg,pol)*uno(un2)
    if n=="peacock":
      if weathe=="rain":
        pea=(5,9,12,14,15)
        peac=r.choice(pea)
        h=h-c.count(n)*peac*15*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*20*leeo(leo,bg,pol)*uno(un2)
    if n=="mudskipper":
      if terrai=="swamp":
        h=h-c.count(n)*25*leeo(leo,bg,pol)*uno(un2)
        fox=1
      else:
        h=h-c.count(n)*5*leeo(leo,bg,pol)*uno(un2)
    if n=="ibex":
      if terrai=="mountain":
        h=h-c.count(n)*1250*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*50*leeo(leo,bg,pol)*uno(un2)
    if n=="camel":
      if terrai=="desert":
        h=h-c.count(n)*960*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*50*leeo(leo,bg,pol)*uno(un2)
    if n=="coyote":
      if weathe=="night":
        h=h-c.count(n)*660*leeo(leo,bg,pol)*uno(un2)
      else:
        h=h-c.count(n)*50*leeo(leo,bg,pol)*uno(un2)
    if n=="bat":
      camel=r.randint(3,7)
      if weathe=="night":
        for i in range(camel):
          h=h-c.count(n)*90*leeo(leo,bg,pol)*uno(un2)
      else:
        for i in range(camel):
          h=h-c.count(n)*20*leeo(leo,bg,pol)*uno(un2)
    if n=="owl":
      camel=r.randint(0,1)
      if weathe=="night":
        if camel==1:
          h=h-c.count(n)*800*leeo(leo,bg,pol)*uno(un2)
        else:
          h=h-c.count(n)*400*leeo(leo,bg,pol)*uno(un2)
      else:
        for i in range(camel):
          j=j+c.count(n)*50*leeo(leo,bg,pol)*uno(un2)
    if n=="penguin":
      if terrai=="glacier":
        h=h-c.count(n)*400*leeo(leo,bg,0)*uno(un2)
        pol=2
      else:
        h=h-c.count(n)*40*leeo(leo,bg,0)*uno(un2)
    if n=="saltwater croc":
      h=h-c.count(n)*395*leeo(leo,bg,pol)*uno(un2)
    if n=="great white shark":
      h=h-c.count(n)*400*leeo(leo,bg,pol)*uno(un2)
    if n=="whale":
      h=h-c.count(n)*950*leeo(leo,bg,pol)*uno(un2)
    if n=="rhino":
      h=h-c.count(n)*220*leeo(leo,bg,pol)*uno(un2)
      j=j+c.count(n)*150*uno(un2)
    if n=="snake":
      h=h-c.count(n)*15*leeo(leo,bg,pol)*uno(un2)
      sn1=1
    if n=="anaconda":
      h=h-c.count(n)*6*leeo(leo,bg,pol)*uno(un2)
      an1=1
    if n=="spider":
      h=h-c.count(n)*15*leeo(leo,bg,pol)*uno(un2)
      sp1=1
    if n=="black widow":
      h=h-c.count(n)*25*leeo(leo,bg,pol)*uno(un2)
      bw1=1
    if n=="scorpion":
      h=h-c.count(n)*10*leeo(leo,bg,pol)*uno(un2)
      sco1=1
    if n=="hydra":
      h=h-c.count(n)*1000*leeo(leo,bg,pol)*uno(un2)
      hy1=1
    if n=="phoenix":
      ph1=4096
    if n=="king cobra":
      h=h-c.count(n)*55*leeo(leo,bg,pol)*uno(un2)
      kc1=1
    if n=="cheetah":
      h=h-c.count(n)*47*leeo(leo,bg,pol)*uno(un2)
      che=1
    if n=="pronghorn":
      pro=r.randint(0,2)
      spe=r.randint(55,60)
      h=h-c.count(n)*((2*pro*spe)+160)*leeo(leo,bg,pol)*uno(un2)
    if n=="peregine falcon":
      hoi=r.randint(1,3)
      hei=r.randint(0,2)
      spe=r.randint(232,242)
      if hoi==1:
        h=h-c.count(n)*(hei*spe+5)*leeo(leo,bg,pol)*uno(un2)
      else:
        che=1
    if n=="black marlin":
      hoi=r.randint(1,3)
      hei=r.randint(0,2)
      spe=r.randint(72,82)
      if hoi>1:
        h=h-c.count(n)*((2-hei)*spe+126)*leeo(leo,bg,pol)*uno(un2)
      else:
        che=1
    if n=="kitsune":
      h=h-c.count(n)*200*leeo(leo,bg,pol)*uno(un2)
      kit=10
    if n=="leopard":
      h=h-c.count(n)*31*leeo(leo,bg,pol)*lp1*uno(un2)
      if lp1<14:
        lp1+=c.count(n)*2
    if n=="cassowary":
      h=h-c.count(n)*121*leeo(leo,bg,pol)*lop1*uno(un2)
      if lop1<14:
        lop1+=c.count(n)*3
    if n=="titanis":
      h=h-c.count(n)*441*leeo(leo,bg,pol)*tit1*uno(un2)
      if tit1<14:
        tit1+=c.count(n)*3
    if n=="argentavis":
      h=h-c.count(n)*361*leeo(leo,bg,pol)*arg1*uno(un2)
      if arg1<14:
        arg1+=c.count(n)*3
    if n=="lion":
      leo=2
      h=h-c.count(n)*95*uno(un2)
    if n=="centaur":
      un1=6
      h=h-c.count(n)*1000*leeo(leo,bg,pol)
    if n=="polar bear":
      pol=2
      h=h-c.count(n)*150*uno(un2)
    if n=="blue glaucus":
      bg=2
      h=h-c.count(n)*1*uno(un2)
    if n=="jaguar":
      h=h-c.count(n)*150*leeo(leo,bg,pol)*uno(un2)
    if n=="parrot":
      ga=c.count(n)*(r.randint(3,7))
      for i in range(ga):
        h=h-c.count(n)*25*leeo(leo,bg,pol)*uno(un2)
        if i<(ga-1):
          print("My health:",j,"Enemy health:",h) 
    if n=="velociraptor":
      for i in range(4):
        h=h-c.count(n)*200*leeo(leo,bg,pol)*uno(un2)
        if i<3:
          print("My health:",j,"Enemy health:",h) 
    if n=="therizinosaur":
      for i in range(4):
        j=j+c.count(n)*200*uno(un2)
        if i<3:
          print("My health:",j,"Enemy health:",h) 
    if n=="mandarin duck":
      ga=c.count(n)*(r.randint(3,7))
      for i in range(ga):
        j=j+c.count(n)*35*uno(un2)
        if i<(ga-1):
          print("My health:",j,"Enemy health:",h)
    if n=="dragon":
      h=h-c.count(n)*8000*leeo(leo,bg,pol)*uno(un2)
    if n=="porcupine":
      go=c.count(n)*(r.randint(55,85))
      h=h-c.count(n)*go*leeo(leo,bg,pol)*uno(un2)
    if n=="hippo":
      h=h-c.count(n)*180*leeo(leo,bg,pol)*(hip**2)*uno(un2)
      hip+=1
    if n!="hippo":
      hip=1
    if n=="ostrich":
      h=h-c.count(n)*50*leeo(leo,bg,pol)*(ost1**2)*uno(un2)
      ost1+=1
    leo-=1 
    bg-=1
    pol-=1
    if un2>0:
      un2-=1
    if n!="ostrich":
      ost1=1
    if sn1>=1 and sn1<8:
      sn1+=1
      h=h-15*uno(un2)
    if sn2>=1 and sn2<8:
      sn2+=1
      j=j-15
    if pk1>=1 and pk1<8:
      pk1+=1
      h=h-15*uno(un2)
    if pk2>=1 and pk2<8:
      pk2+=1
      j=j-15
    if an1>=1 and an1<8:
      an1+=1
      h=h-100*uno(un2)
    if sp1>=1 and sp1<8:
      sp1+=1
      h=h-(sp1*15)*uno(un2)
    if sp2>=1 and sp2<8:
      sp2+=1
      j=j-(sp2*15)
    if bw1>=1:
      bw1+=1
      h=h-(bw1*25)*uno(un2)
    if bw2>=1:
      bw2+=1
      j=j-(bw2*25)
    if 17>sco1>=1:
      sco1*=2
      h=h-(sco1*10)*uno(un2)
    if 17>sco2>=1:
      sco2*=2
      j=j-(sco2*10)
    if hy1>=1:
      hy1*=2
      h=h-(hy1*500)*uno(un2)
    if hy2>=1:
      hy2*=2
      j=j-(hy2*500)
    if ph1!=1:
      h=h-(ph1)*uno(un2)
      ph1=ph1//2
      phoenix1=1
    if ph2!=1:
      j=j-(ph2)
      ph2=ph2//2
      phoenix2=1
    if ph1==1:
      phoenix1=0
    if ph2==1:
      phoenix2=0
    if pof1!=1:
      h=h-(pof1)*uno(un2)
      pof1=pof1//2
      pofo1=1
    if pof2!=1:
      j=j-(pof2)
      pof2=pof2//2
      pofo2=1
    if pof1==1:
      pofo1=0
    if pof2==1:
      pofo2=0
    if kc1==1:
      h=h-35*uno(un2)
    if kc2==1:
      j=j-35
    if sn1==8:
      sn1=0
    if sn2==8:
      sn2=0
    if sp1==8:
      sp1=0
    if sp2==8:
      sp2=0
    if an1==8:
      an1=0
    if an2==8:
      an2=0
    if sco1==16:
      sco1=0
    if sco2==16:
      sco2=0
    h=round(h)
    j=round(j)
    print("My health:",j,"Enemy health:",h)
    print("damage:",col.Fore.RED+str(vi-h)+col.Fore.WHITE,"    heal:",col.Fore.GREEN+str(j-ki)+col.Fore.WHITE)
    if che==1 or kit>=1:
      p=True
      if kit>=1:
        kit-=1
    else:
      p=False    
  if h<=0 or j<=0:
    break


    
  if p==False:
    vi=j
    ki=h
    che=0
    print()
    print(col.Fore.GREEN+"Player2"+col.Fore.WHITE)
    list=c
    c=[]
    for i in range(3):
      rand=r.randint(0,1000)
      if rand<860:
        p=r.choice(a)
      if 865>rand>=860:
        p=r.choice(al)
      if rand>=865:
        p=r.choice(an)
      c.append(p)
    print(c)
    weather=r.randint(1,5)
    terrain=r.randint(1,7)
    if weather==1:
      weathe="rain"
    if weather==2:
      weathe="sunny"
    if weather==3:
      weathe="snow"
    if weather==4:
      weathe="lightning"
    if weather==5:
      weathe="night"
    if terrain==1:
      terrai="glacier"
    if terrain==2:
      terrai="mountain"
    if terrain==3:
      terrai="swamp"
    if terrain==4:
      terrai="desert"
    if terrain==5:
      terrai="forest"
    if terrain==6:
      terrai="river"
    if terrain==7:
      terrai="volcano"
    print(weadict[weather],end="  ")
    print(terdict[terrain])
    print("💀",sn1,kc1,pk1,sp1,bw1,sco1,hy1,"🔁",un1,"🌀",an1,"🔥",phoenix1,pofo1)
    if fox!=1:
      n=input("select a card: ")
      while n not in c:
        print("Error")
        n=input("select a card: ")
    if fox==1:
      fox=0
      n="nothing"
    if n=="crow":
      jj=r.randint(0,100)
      while n=="crow":
        c=[]
        if jj==81:
          for i in range(3):
            jjl=r.choice(al)
            c.append(jjl)
        if jj<81:
          for i in range(3):
            jjl=r.choice(a)
            c.append(jjl)
        if jj>81:
          for i in range(3):
            jjl=r.choice(an)
            c.append(jjl)
        print(c)
        n=input("select a card: ")
        while n not in c:
          print("Error")
          n=input("select a card: ")
    if n=="bull shark":
      j=j-c.count(n)*130*leeo(leo,bg,pol)*uno(un1)
    if n=="koala":
      koala=r.randint(0,10)
      j=j-c.count(n)*(((koala)**2)+7)*leeo(leo,bg,pol)*uno(un1)
    if n=="panda":
      koala=r.randint(0,10)
      j=j-c.count(n)*((koala)**2)*7*leeo(leo,bg,pol)*uno(un1)
    if n=="salamander":
      kole=[]
      typo=("fire","poison","beast","heal")
      for i in range(3):
        koal=r.choice(typo)
        kole.append(koal)
      print(kole)
      huo=input("enter type: ")
      if huo =="fire":
        pof2=256
      if huo=="poison":
        pk2=1
      if huo=="beast":
        j=j-c.count(n)*70*leeo(leo,bg,pol)*uno(un2)
      if huo=="heal":
        h=h+c.count(n)*80*leeo(leo,bg,pol)*uno(un2)
    if n=="tarantula":
      j=j-c.count(n)*25*leeo(leo,bg,pol)*uno(un1)
      kc1=sn1=sp1=bw1=sco1=0
    if n=="elephant":
      j=j-c.count(n)*350*leeo(leo,bg,pol)*uno(un1)
    if n=="orca":
      j=j-c.count(n)*1900*leeo(0,bg,pol)*uno(un1)
    if n=="blob fish":
      j=j-c.count(n)*65*leeo(leo,0,pol)*uno(un1)
    if n=="honey badger":
      j=j-c.count(n)*400*uno(un1)
    if n=="tiger":
      if leeo(leo,0,0)==0:
        j=j-c.count(n)*315*leeo(0,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*105*leeo(0,bg,pol)*uno(un1)
    if n=="mammoth":
      if leeo(0,0,pol)==0.5:
        j=j-c.count(n)*1350*leeo(leo,bg,0)*uno(un1)
      else:
        j=j-c.count(n)*350*leeo(leo,bg,0)*uno(un1)
    if n=="smilodon":
      if leeo(0,0,pol)==0.5:
        j=j-c.count(n)*700*leeo(leo,bg,0)*uno(un1)
        leo=2
      else:
        j=j-c.count(n)*350*leeo(leo,bg,0)*uno(un1)
    if n=="thylacoleo":
      if leeo(0,0,pol)==0.5:
        j=j-c.count(n)*250*leeo(leo,bg,0)*uno(un1)
      else:
        j=j-c.count(n)*750*leeo(leo,bg,0)*uno(un1)
    if n=="wooly rhino":
      j=j-c.count(n)*660*leeo(leo,bg,0)*uno(un1)
      h=h+c.count(n)*450*uno(un1)
    if n=="titanboa":
      if leeo(leo,0,0)==0 or leeo(0,bg,0)==-1:
        j=j-c.count(n)*1000*uno(un1)
      else:
        j=j-c.count(n)*40*uno(un1)
    if n=="mandarin fish":
      if leeo(0,bg,0)==-1:
        j=j-c.count(n)*555*leeo(leo,0,pol)*uno(un1)
      else:
        j=j-c.count(n)*5*leeo(leo,0,pol)*uno(un1)
    if n=="kangaroo":
      j=j-c.count(n)*160*leeo(leo,bg,pol)*uno(un1)
    if n=="gorilla":
      j=j-(c.count(n)**c.count(n))*130*leeo(leo,bg,pol)*uno(un1)
    if n=="horse":
      hoi=r.randint(0,10)
      if hoi==7:
        j=j-c.count(n)*746*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*70*leeo(leo,bg,pol)*uno(un1)
    if n=="dunkleosteus":
      hoi=r.randint(0,100)
      if hoi==81:
        j=j-c.count(n)*8100*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*1100*leeo(leo,bg,pol)*uno(un1)
    if n=="megalodon":
      j=j-c.count(n)*4000*leeo(leo,bg,pol)*uno(un1)
    if n=="fox":
      hoi=r.randint(1,2)
      if hoi==1:
        j=j-c.count(n)*140*leeo(leo,bg,pol)*uno(un1)
      else:
        fox=1
    if n=="chameleon":
      fox=1
    if n=="arctic fox":
      hoi=r.randint(1,2)
      if hoi==1:
        j=j-c.count(n)*70*leeo(leo,bg,pol)*uno(un1)
        pol=2
      else:
        fox=1
    if n=="donkey":
      hoi=r.randint(0,10)
      if hoi==5:
        h=h+c.count(n)*250*uno(un1)
      else:
        h=h+c.count(n)*70*uno(un1)
    if n=="unicorn":
      h=h+c.count(n)*8000*uno(un1)
    if n=="bacteria":
      h=h+c.count(n)*200*uno(un1)
    if n=="trex":
      j=j-c.count(n)*1280*leeo(leo,bg,pol)*uno(un1)
    if n=="komodo dragon":
      if "komodo dragon" in list:
        j=j-c.count(n)*250*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*60*leeo(leo,bg,pol)*uno(un1)
    if n=="stego":
      j=j-c.count(n)*880*leeo(leo,bg,pol)*uno(un1)
    if n=="peacock":
      if weathe=="rain":
        pea=(5,9,12,14,15)
        peac=r.choice(pea)
        j=j-c.count(n)*peac*15*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*20*leeo(leo,bg,pol)*uno(un1)
    if n=="mudskipper":
      if terrai=="swamp":
        j=j-c.count(n)*25*leeo(leo,bg,pol)*uno(un1)
        fox=1
      else:
        j=j-c.count(n)*5*leeo(leo,bg,pol)*uno(un1)
    if n=="ibex":
      if terrai=="mountain":
        j=j-c.count(n)*1250*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*50*leeo(leo,bg,pol)*uno(un1)
    if n=="camel":
      if terrai=="desert":
        j=j-c.count(n)*960*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*50*leeo(leo,bg,pol)*uno(un1)
    if n=="coyote":
      if weathe=="night":
        j=j-c.count(n)*660*leeo(leo,bg,pol)*uno(un1)
      else:
        j=j-c.count(n)*50*leeo(leo,bg,pol)*uno(un1)
    if n=="bat":
      camel=r.randint(3,7)
      if weathe=="night":
        for i in range(camel):
          j=j-c.count(n)*90*leeo(leo,bg,pol)*uno(un1)
      else:
        for i in range(camel):
          j=j-c.count(n)*20*leeo(leo,bg,pol)*uno(un1)
    if n=="owl":
      camel=r.randint(0,1)
      if weathe=="night":
        if camel==1:
          j=j-c.count(n)*800*leeo(leo,bg,pol)*uno(un1)
        else:
          j=j-c.count(n)*400*leeo(leo,bg,pol)*uno(un1)
      else:
        for i in range(camel):
          h=h+c.count(n)*50*leeo(leo,bg,pol)*uno(un1)
    if n=="penguin":
      if terrai=="glacier":
        j=j-c.count(n)*400*leeo(leo,bg,0)*uno(un1)
        pol=2
      else:
        j=j-c.count(n)*40*leeo(leo,bg,0)*uno(un1)
    if n=="saltwater croc":
      j=j-c.count(n)*395*leeo(leo,bg,pol)*uno(un1)
    if n=="great white shark":
      j=j-c.count(n)*400*leeo(leo,bg,pol)*uno(un1)
    if n=="whale":
      j=j-c.count(n)*950*leeo(leo,bg,pol)*uno(un1)
    if n=="rhino":
      j=j-c.count(n)*220*leeo(leo,bg,pol)*uno(un1)
      h=h+c.count(n)*150*uno(un1)
    if n=="snake":
      j=j-c.count(n)*15*leeo(leo,bg,pol)*uno(un1)
      sn2=1
    if n=="anaconda":
      j=j-c.count(n)*6*leeo(leo,bg,pol)*uno(un1)
      an2=1
    if n=="spider":
      j=j-c.count(n)*15*leeo(leo,bg,pol)*uno(un1)
      sp2=1
    if n=="black widow":
      j=j-c.count(n)*25*leeo(leo,bg,pol)*uno(un1)
      bw2=1
    if n=="scorpion":
      j=j-c.count(n)*10*leeo(leo,bg,pol)*uno(un1)
      sco2=1
    if n=="hydra":
      j=j-c.count(n)*1000*leeo(leo,bg,pol)*uno(un1)
      hy2=1
    if n=="phoenix":
      ph2=4096
    if n=="king cobra":
      j=j-c.count(n)*55*leeo(leo,bg,pol)*uno(un1)
      kc2=1
    if n=="cheetah":
      j=j-c.count(n)*47*leeo(leo,bg,pol)*uno(un1)
      che=1
    if n=="pronghorn":
      pro=r.randint(0,2)
      spe=r.randint(55,60)
      j=j-c.count(n)*((2*pro*spe)+160)*leeo(leo,bg,pol)*uno(un1)
    if n=="peregine falcon":
      hoi=r.randint(1,3)
      hei=r.randint(0,2)
      spe=r.randint(232,242)
      if hoi==1:
        j=j-c.count(n)*(hei*spe+5)*leeo(leo,bg,pol)*uno(un1)
      else:
        che=1
    if n=="black marlin":
      hoi=r.randint(1,3)
      hei=r.randint(0,2)
      spe=r.randint(72,82)
      if hoi>1:
        j=j-c.count(n)*((2-hei)*spe+126)*leeo(leo,bg,pol)*uno(un1)
      else:
        che=1
    if n=="kitsune":
      j=j-c.count(n)*200*leeo(leo,bg,pol)*uno(un1)
      kit=10
    if n=="leopard":
      j=j-c.count(n)*31*leeo(leo,bg,pol)*lp2*uno(un1)
      if lp2<14:
        lp2+=c.count(n)*2
    if n=="cassowary":
      j=j-c.count(n)*121*leeo(leo,bg,pol)*lop2*uno(un1)
      if lop2<14:
        lop2+=c.count(n)*3
    if n=="titanis":
      j=j-c.count(n)*441*leeo(leo,bg,pol)*tit2*uno(un1)
      if tit2<14:
        tit2+=c.count(n)*3
    if n=="argentavis":
      j=j-c.count(n)*361*leeo(leo,bg,pol)*arg2*uno(un1)
      if arg2<14:
        arg2+=c.count(n)*3
    if n=="lion":
      leo=2
      j=j-c.count(n)*95*uno(un1)
    if n=="centaur":
      un2=6
      j=j-c.count(n)*1000*leeo(leo,bg,pol)
    if n=="polar bear":
      pol=2
      j=j-c.count(n)*150*uno(un1)
    if n=="blue glaucus":
      bg=2
      j=j-c.count(n)*1*leeo(leo,bg,pol)*uno(un1)
    if n=="jaguar":
      j=j-c.count(n)*150*leeo(leo,bg,pol)*uno(un1)
    if n=="parrot":
      ga=c.count(n)*(r.randint(3,7))
      for i in range(ga):
        j=j-c.count(n)*25*leeo(leo,bg,pol)*uno(un1)
        if i<(ga-1):
          print("My health:",h,"Enemy health:",j) 
    if n=="velociraptor":
      for i in range(4):
        j=j-c.count(n)*200*leeo(leo,bg,pol)*uno(un1)
        if i<3:
          print("My health:",h,"Enemy health:",j) 
    if n=="therizinosaur":
      for i in range(4):
        h=h+c.count(n)*200*uno(un1)
        if i<3:
          print("My health:",h,"Enemy health:",j) 
    if n=="mandarin duck":
      ga=c.count(n)*(r.randint(3,7))
      for i in range(ga):
        h=h+c.count(n)*35*uno(un1)
        if i<(ga-1):
          print("My health:",h,"Enemy health:",j)
    if n=="dragon":
      j=j-c.count(n)*8000*leeo(leo,bg,pol)*uno(un1)
    if n=="porcupine":
      go=c.count(n)*(r.randint(55,85))
      j=j-c.count(n)*go*leeo(leo,bg,pol)*uno(un1)
    if n=="hippo":
      j=j-c.count(n)*180*leeo(leo,bg,pol)*(hip**2)*uno(un1)
      hip+=1
    if n!="hippo":
      hip=1
    if n=="ostrich":
      j=j-c.count(n)*50*leeo(leo,bg,pol)*(ost2**2)*uno(un1)
      ost2+=1
    leo-=1 
    bg-=1
    pol-=1
    if un1>0:
      un1-=1
    if n!="ostrich":
      ost2=1
    if sn1>=1 and sn1<8:
      sn1+=1
      h=h-15
    if sn2>=1 and sn2<8:
      sn2+=1
      j=j-15*uno(un1)
    if pk1>=1 and pk1<8:
      pk1+=1
      h=h-15
    if pk2>=1 and pk2<8:
      pk2+=1
      j=j-15*uno(un1)
    if an2>=1 and an2<8:
      an2+=1
      j=j-100*uno(un1)
    if sp1>=1 and sp1<8:
      sp1+=1
      h=h-(sp1*15)
    if sp2>=1 and sp2<8:
      sp2+=1
      j=j-(sp2*15)*uno(un1)
    if kc1==1:
      h=h-35
    if kc2==1:
      j=j-35*uno(un1)
    if bw1>=1:
      bw1+=1
      h=h-(bw1*25)
    if bw2>=1:
      bw2+=1
      j=j-(bw2*25)*uno(un1)
    if 17>sco1>=1:
      sco1*=2
      h=h-(sco1*10)
    if 17>sco2>=1:
      sco2*=2
      j=j-(sco2*10)*uno(un1)
    if hy1>=1:
      hy1*=2
      h=h-(hy1*500)
    if hy2>=1:
      hy2*=2
      j=j-(hy2*500)*uno(un1)
    if ph1!=1:
      h=h-(ph1)
      ph1=ph1//2
      phoenix1=1
    if ph2!=1:
      j=j-(ph2)*uno(un1)
      ph2=ph2//2
      phoenix2=1
    if ph1==1:
      phoenix1=0
    if ph2==1:
      phoenix2=0
    if pof1!=1:
      h=h-(pof1)*uno(un1)
      pof1=pof1//2
      pofo1=1
    if pof2!=1:
      j=j-(pof2)
      pof2=pof2//2
      pofo2=1
    if pof1==1:
      pofo1=0
    if pof2==1:
      pofo2=0
    if sn1==8:
      sn1=0
    if sn2==8:
      sn2=0
    if sp1==8:
      sp1=0
    if sp2==8:
      sp2=0
    if an1==8:
      an1=0
    if an2==8:
      an2=0
    if sco1==16:
      sco1=0
    if sco2==16:
      sco2=0
    h=round(h)
    j=round(j)
    print("My health:",h,"Enemy health:",j)
    print("damage:",col.Fore.RED+str(vi-j)+col.Fore.WHITE,"    heal:",col.Fore.GREEN+str(h-ki)+col.Fore.WHITE)
    if che==1 or kit>=1:
      p=False
      if kit>=1:
        kit-=1
    else:
      p=True     
  if h<=0 or j<=0:
    break




    
if h<=0 and p==False:
  print("player 1 wins")
else:
  print("player 2 wins")

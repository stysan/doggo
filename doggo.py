# importing turtle and asking for directory
import turtle as t
code = open(input("Directory: "), mode='r').read().split("\n")
line = 0
t.reset()
t.tracer(0)
# running
for i in code:
    line += 1
    command = i.split()
    try:
        # comment or blank
        if i.startswith("---") or i == "": pass

        # command
        if command[0] == "go":
            if command[1] == "forward": t.forward(int(command[2]))
            elif command[1] == "backward": t.backward(int(command[2]))
            elif command[1] == "to": t.goto(int(command[2]), int(command[3]))
            
        elif command[0] == "turn":
            if command[1] == "left": t.left(int(command[2]))
            elif command[1] == "right": t.right(int(command[2]))
            
        elif command[0] == "turtle" or command[0] == "pen":
            if command[1] == "up": t.up()
            elif command[1] == "down": t.down()
            elif command[1] == "color": t.color(str(command[2]))
            elif command[1] == "hide": t.hideturtle()
            elif command[1] == "show": t.showturtle()
            
        elif command[0] == "fill":
            if command[1] == "color": t.fillcolor(str(command[2]))
            elif command[1] == "start": t.begin_fill()
            elif command[1] == "end": t.end_fill()
            
        elif command[0] == "label":
            command = i.split(maxsplit=1)
            t.write(str(command[1]))
            
        elif command[0] == "ishowspeed": t.speed(int(command[1]))
        
    # houston, we have a problem
    except:
        input(f"error on line {line} go brr\n\nprobably not enough args or not integer in args i don't know!\nim just guessing")
        quit()

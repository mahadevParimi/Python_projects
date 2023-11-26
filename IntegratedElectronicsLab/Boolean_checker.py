class lineDraw:
    def pipe_line(self,char):
        pipe_place = [0,5,15,25,35,42]
        for i in range(1,44):
            if i-1 in pipe_place:
                print("|",end="")
            else:
                print(char,end="")
        print("")

    def dash_pipe(self):
        print("|"+"_"*41+"|")

    def dash_line(self):
        print("_"*43)
        
print("\nExpression 1 : abć + bć + áb")
print("Expression 2 : b^ac\n")

border = lineDraw()
border.dash_line()
print("| no | A B C D | W x Y Z | W X Y Z | x==X |")
border.pipe_line("_")

val = [0,1]
i = 0

for a in val:
    for b in val:
        for c in val:
            for d in val: 
                w = a*b*c 
                x = (not b)*c*a | (not c)*b | (not a)*b 
                X = b^(a*c)
                y = a^c
                z = d
                print("|","0"+str(i)if i <= 9 else i,"|",a,b,c,d,"|",w,x,y,z,"|",w,X,y,z,"|",x == X, "|")
                i += 1
border.dash_pipe()
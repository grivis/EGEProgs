# program recurs;
# uses graph;
# var x,y,r,d,m:integer;
# procedure ris(x,y,r:integer);
# var i:integer;
# begin
#    if r<10 then exit;
#    circle(x,y,r);
#    for i:=1 to 1000 do; { просто цикл задержки }
#    ris(x+r,y,r*3 div 5);
#    ris(x-r,y,r*3 div 5);
# end ;
# begin {начало основной программы}
#    d:=detect;
#    initgraph(d,m,'e:\bp\bgi');
#    x:=320;
#    y:=240;
#    r:=120;
#    ris(x,y,r);
#    readln ;
# end.
import turtle

window = turtle.Screen()
window.title('Recursive Circles')
window.bgcolor('lightblue')

andy = turtle.Turtle()
andy.color('red')

def plotcircle(x, y, r):
    if r<10: return
    andy.penup()
    andy.goto(x, y)
    andy.pendown()
    andy.circle(r)
    # andy.penup()
    # andy.goto(x +r, y)
    # andy.pendown()
    # andy.circle(r*3 // 5)
    # andy.penup()
    # andy.goto(x - r, y)
    # andy.pendown()
    # andy.circle(r * 3 // 5)
    plotcircle(x+r, y, r * 3 // 5)
    plotcircle(x - r, y, r * 3 // 5)

x = 0
y = 0
r = 50
plotcircle(x, y, r)
window.exitonclick()
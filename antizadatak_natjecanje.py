import turtle
import math

s = turtle.getscreen()
t = turtle.getturtle()
t.speed(20)

def iks(a):
    dijagonala = a * math.sqrt(2)
    t.penup()
    t.forward(a / 2)
    t.left(90)
    t.forward(a / 2)
    t.right(45)
    t.pendown()
    t.back(dijagonala)
    t.penup()
    t.right(45)
    t.forward(a)
    t.right(45)
    t.pendown()
    t.back(dijagonala)
    t.penup()
    t.right(45)
    t.forward(a / 2)
    t.left(90)
    t.forward(a / 2)
    return

def kvadrat(a):
    t.penup()
    t.forward(a / 2)
    t.pendown()
    t.right(90)
    for i in range(2):
        t.forward(a / 2)
        t.right(90)
        t.forward(a)
        t.right(90)
        t.forward(a / 2)
    t.left(90)
    t.penup()
    t.back(a / 2)
    t.pendown()
    return

def mreza(n, m, d):
    #n je broj redaka, m je broj stupaca, d je duljina stranice kvadrata
    for k in range(2):
        for j in range(n):        
            for i in range(m):
                kvadrat(d)
                t.penup()
                t.forward(d)
                t.pendown()
            t.penup()
            t.back(m * d)
            t.left(90)
            t.forward(d)
            t.right(90)
            t.pendown()
        t.penup()
        t.left(90)
        t.forward(10)
        t.right(90)
        t.pendown()
    t.penup()
    t.left(90)
    t.back(2 * 10 + 2 * n * d)
    t.right(90)
    t.pendown()
    return

def ucrtaj_brodove(tomek, medo, n, m, d):
    mreza(n, m, d)
    t.penup()
    t.left(90)
    for lista in tomek:
        t.forward((lista[0] - 1) * d)
        t.right(90)
        t.forward((lista[1] - 1) * d)
        t.begin_fill()               
        kvadrat(d)
        t.end_fill()
        t.penup()
        if lista[2] == 'V':
            for i in range(lista[3] - 1):
                t.forward(d)
                t.begin_fill()               
                kvadrat(d)
                t.end_fill()
                t.penup()
            t.back((lista[3] - 1) * d)
        elif lista[2] == 'O':
            t.left(90)
            for i in range(lista[3] - 1):
                t.forward(d)
                t.begin_fill()               
                kvadrat(d)
                t.end_fill()
                t.penup()
            t.back((lista[3] - 1) * d)
            t.right(90)
        else:
            return 'Smjer nije dobar'
        t.back((lista[1] - 1) * d)
        t.left(90)
        t.back((lista[0] - 1) * d)
    #pos = t.setpos()
    t.forward((2 * n - 1) * d + 10)
    t.right(180)
    for lista in medo:
        t.forward((lista[0] - 1) * d)
        t.left(90)
        t.forward((lista[1] - 1) * d)
        t.begin_fill()               
        kvadrat(d)
        t.end_fill()
        t.penup()
        if lista[2] == 'V':
            for i in range(lista[3] - 1):
                t.forward(d)
                t.begin_fill()               
                kvadrat(d)
                t.end_fill()
                t.penup()
            t.back((lista[3] - 1) * d)
        elif lista[2] == 'O':
            t.left(90)
            for i in range(lista[3] - 1):
                 t.forward(d)
                 t.begin_fill()               
                 kvadrat(d)
                 t.end_fill()
                 t.penup()
            t.back((lista[3] - 1) * d)
            t.right(90)
        else:
            return 'Smjer nije dobar'
        t.back((lista[1] - 1) * d)
        t.right(90)
        t.back((lista[0] - 1) * d)

    t.right(180)
    t.back((2 * n - 1) * d + 10)
    t.right(90)
    return

def provjera(l, tomek, medo):
    pog_t = []
    pog_m = []
    pogodak = 0
    red = "T" # ili "T" ili "M"
    for lista in l:
        pogodak = 0
        if red == "T":
            for lista2 in medo:
                if lista2[2] == "O":
                    if (lista[1] == lista2[1]) and (lista[0] <= lista2[0]) and (lista[0] >= lista2[0] - lista2[3] + 1):
                        pog_t.append(lista)
                        pogodak = 1
                else:
                    if (lista[0] == lista2[0]) and (lista[1] >= lista2[1]) and (lista[1] <= lista2[1] + lista2[3] - 1):
                        pog_t.append(lista)
                        pogodak = 1
            if pogodak == 0:
                red = "M"
        if red == "M":
            for lista2 in tomek:
                if lista2[2] == "O":
                    if (lista[1] == lista2[1]) and (lista[0] >= lista2[0]) and (lista[0] <= lista2[0] + lista2[3] - 1):
                        pog_m.append(lista)
                        pogodak = 1
                else:
                    if (lista[0] == lista2[0]) and (lista[1] >= lista2[1]) and (lista[1] <= lista2[1] + lista2[3] - 1):
                        pog_m.append(lista)
                        pogodak = 1
            if pogodak == 0:
                red = "T"
    return [pog_t, pog_m]

def brodovi(n, m, d, tomek, medo, l):
    lista_pogodenih = provjera(l, tomek, medo)
    ucrtaj_brodove(tomek, medo, n, m, d)
    for lista in lista_pogodenih[1]:
        t.penup()
        t.forward(d * (lista[1] - 1))
        t.left(90)
        t.forward(d * (lista[0] - 1))
        t.pendown()
        t.color('white')
        t.begin_fill()               
        kvadrat(d)
        t.end_fill()
        t.color('black')
        kvadrat(d)
        iks(d)
        t.penup()
        t.back(d * (lista[0] - 1))
        t.right(90)
        t.back(d * (lista[1] - 1))
    t.left(90)
    t.penup()
    t.forward((2 * n - 1) * d + 10)
    t.right(180)
    for lista in lista_pogodenih[0]:
        t.forward(d * (lista[0] - 1))
        t.left(90)
        t.forward(d * (lista[1] - 1))
        t.pendown()
        t.color('white')
        t.begin_fill()               
        kvadrat(d)
        t.end_fill()
        t.color('black')
        kvadrat(d)
        iks(d)
        t.penup()
        t.back(d * (lista[1] - 1))
        t.right(90)
        t.back(d * (lista[0] - 1))
    t.forward((2 * n - 1) * d + 10)
    t.left(90)
    return
        

import turtle
import math
import random

s = turtle.getscreen()
t = turtle.getturtle()
t.speed(20)


def brodovi(n, m, d, dat_kev, dat_lada):
    
    mreza(n, m, d) #crtamo mrežu
    t.left(90)
    #ovdje u listu upisujemo brodove iz datoteke
    #kevinovi brodovi dolje, ladini gore
    kev = open(dat_kev, 'r')   
    line = kev.readline()
    kev_b = []
    mala = []
    for i in range(len(line)):
        if line[i].isdigit() == True:
            mala.append(int(line[i]))
        elif line[i].isupper() == True:
            mala.append(line[i])
        elif line[i] == "]":
            kev_b.append(mala)
            mala = []
            
    lada = open(dat_lada, 'r')
    line = lada.readline()
    lada_b = []
    for i in range(len(line)):
        if line[i].isdigit() == True:
            mala.append(int(line[i]))
        elif line[i].isupper() == True:
            mala.append(line[i])
        elif line[i] == "]":
            lada_b.append(mala)
            mala = []

    #brojimo duljine brodova da imamo counter
    #da znamo kada igra staje
    counter_k, counter_l = 0, 0      
    for brod in kev_b:
        counter_k += brod[-1]

    for brod in lada_b:
        counter_l += brod[-1]

    #Ovdje nasumično biramo tko prvi ide
    novcic = random.randint(1, 2)
    if novcic == 1:
        print("Igru započinje Lada")
        potez = "L"
    else:
        print("Igru započinje Kevin")
        potez = "K"

    pokusaji_lada, pokusaji_kevin = [], []    
    #ovdje kreće igra       
    while counter_k > 0 and counter_l > 0:
        if potez == "L":
            pokusaj = input("Lado biraj poziciju: ")
            if pokusaj in pokusaji_lada:
                print("Već ste pokušali ovu poziciju. Pokušajte ponovo")
            else:
                pokusaji_lada.append(pokusaj)
                pogodak = 0 
                for brod in kev_b:   
                    if brod[2] == "O":
                        if (int(pokusaj[2]) == brod[1]) and (int(pokusaj[0]) >= brod[0]) and (int(pokusaj[0]) <= brod[0] + brod[3] - 1):
                            pogodak = 1
                    else:
                        if (int(pokusaj[0]) == brod[0]) and (int(pokusaj[2]) >= brod[1]) and (int(pokusaj[2]) <= brod[1] + brod[3] - 1):
                            pogodak = 1
                if pogodak == 0:
                    print("Promašaj")
                    ucrtaj_brod(potez, pokusaj, pogodak, n, d)
                    potez = "K"
                else:
                    print("Lada je pogodila brod")
                    counter_k -= 1
                    ucrtaj_brod(potez, pokusaj, pogodak, n, d)
        else:
            pokusaj = input("Kevine biraj poziciju: ")
            if pokusaj in pokusaji_kevin:
                print("Već ste pokušali ovu poziciju. Pokušajte ponovo")
            else:
                pokusaji_kevin.append(pokusaj)
                pogodak = 0
                for brod in lada_b:               
                    if brod[2] == "O":
                        if (int(pokusaj[2]) == brod[1]) and (int(pokusaj[0]) <= brod[0]) and (int(pokusaj[0]) >= brod[0] - brod[3] + 1):
                            pogodak = 1
                    else:
                        if (int(pokusaj[0]) == brod[0]) and (int(pokusaj[2]) >= brod[1]) and (int(pokusaj[2]) <= brod[1] + brod[3] - 1):
                            pogodak = 1
                        
                if pogodak == 0:
                    print("Promašaj")
                    ucrtaj_brod(potez, pokusaj, pogodak, n, d)
                    potez = "L"
                else:
                    print("Kevin je pogodio brod")
                    counter_l -= 1
                    ucrtaj_brod(potez, pokusaj, pogodak, n, d)
    if counter_k == 0:
        pobjednik = "Lada"
    elif counter_l == 0:
        pobjednik = "Kevin"
    return "Pobjednik je " + pobjednik

def ucrtaj_brod(potez, pokusaj, pogodak, n, d):
    t.penup()
    #t.left(90)
    if potez == "L":
        t.forward((int(pokusaj[0]) - 1) * d)
        t.right(90)
        t.forward((int(pokusaj[2]) - 1) * d)
        if pogodak == 1:
            t.begin_fill()               
            kvadrat(d)
            t.end_fill()
            t.penup()
        else:
            iks(d)
            t.penup()
        t.back((int(pokusaj[2]) - 1) * d)
        t.left(90)
        t.back((int(pokusaj[0]) - 1) * d)
    else:
        t.forward((2 * n - 1) * d + 10)
        t.right(180)
        t.forward((int(pokusaj[0]) - 1) * d)
        t.left(90)
        t.forward((int(pokusaj[2]) - 1) * d)
        if pogodak == 1:
            t.begin_fill()               
            kvadrat(d)
            t.end_fill()
            t.penup()
        else:
            iks(d)
            t.penup()
        t.back((int(pokusaj[2]) - 1) * d)
        t.right(90)
        t.back((int(pokusaj[0]) - 1) * d)
        t.right(180)
        t.back((2 * n - 1) * d + 10)
    return

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
    

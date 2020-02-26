import pygame
from pygame.locals import *
import time
import random
window_size = (500,500)




pygame.init()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("TicTacToe")
run = True
Numbers = []
sortType = 3
doSort = False
setValue = True
for i in range(window_size[0]):
    Numbers.append(random.randint(0,window_size[1]))


        






def doRender(count, j):
    window.fill((0,0,0))
    w,h  = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont("comicsansms",100)

    global Numbers

    for x in range(len(Numbers)):
        if x == count:
            pygame.draw.line(window,(250,0,0),(x,window_size[1]),(x,Numbers[x]))
        elif x == j:
            pygame.draw.line(window,(0,250,0),(x,window_size[1]),(x,Numbers[x]))
        else:
            pygame.draw.line(window,(200,200,200),(x,window_size[1]),(x,Numbers[x]))
    
    

    #font = pygame.font.SysFont("comicsansms",40)
    #text = font.render("Press R to reset...",True,color)
    #pos = (w/2,(h/2) + 70)
    #textRect = text.get_rect()
    #textRect.center = pos
    #pygame.display.get_surface().blit(text,textRect)
    pygame.display.update()

def doEvent():
    global run
    global sortType
    global doSort
    global Numbers

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            run = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print ("You pressed the left mouse button at (%d, %d)" % event.pos)
            w,h  = pygame.display.get_surface().get_size()
            x,y = event.pos

            cellPos =  (int(x / (w/3)),int(y / (h/3)))
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_RETURN:
            print("Sorting....")
            doSort = True
            setValue = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_1 and not doSort:
            sortType = 0
            print("Setting Sorter to Selection Sort....")
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_2 and not doSort:
            sortType = 1
            print("Setting Sorter to Insertion Sort....")
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_3 and not doSort:
            sortType = 2
            print("Setting Sorter to Bubble Sort....")
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_4 and not doSort:
            sortType = 3
            print("Setting Sorter to Merge Sort....")
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_r:
            Numbers = []
            sortType = 3
            doSort = False
            setValue = True
            for i in range(window_size[0]):
                Numbers.append(random.randint(0,window_size[1]))
            print("Reseting...")
            doRender(0,0)

count = 0
def doLogic():
    global Numbers
    global doSort
    global min_index
    global count
    global setValue

    if(doSort):
        if sortType == 0:
            #SelectionSort
            if setValue:
                count = 0
            min_index = 0
            if count <= len(Numbers) - 1:
                min_index = count
                for j in range(count+1,len(Numbers)):
                    if(Numbers[j] < Numbers[min_index]):
                        min_index = j
                    doRender(count,j)
                Swap(min_index,count)
                
                count = count + 1
        elif sortType == 1:
            #InsertionSort
            if setValue:
                count = 1
            if count < len(Numbers):
                j = count
                while(j > 0 and Numbers[j-1] > Numbers[j]):
                    Swap(j,j-1)
                    doRender(count,j)
                    j = j-1
                count = count + 1
        elif sortType == 2:
            #BubbleSort
            if count < len(Numbers)-1:
                for j in range(len(Numbers)-count -1):
                    if Numbers[j] > Numbers[j+1]:
                        Swap(j,j+1)
                    doRender(count,j)
                count = count + 1
        elif sortType == 3:
            #MergeSort
            MergeSort(Numbers,0,len(Numbers)-1)
            doSort = False
        setValue = False
        
        #print(Numbers)

def MergeSort(arr,l,r):
    if l < r:
        m = int(l + (r-l)/2)
        MergeSort(arr,l,m)
        MergeSort(arr,m+1,r)

        Merge(arr,l,m,r)

        doRender(l,r)

def Merge(arr,l,m,r):

    n1 = m-l+1
    n2 = r-m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l+i]
    for j in range(n2):
        R[j] = arr[m+1+j]

    i = 0 
    j = 0
    k = l

    while i < n1 and j < n2:
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i=i+1
        else:
            arr[k] = R[j]
            j=j+1
        k = k+1

    while i < n1:
        arr[k] = L[i]
        i=i+1
        k = k+1
    while j < n2:
        arr[k] = R[j]
        j=j+1
        k = k+1

def Swap(indexA, indexB):
    global Numbers
    temp = Numbers[indexA]
    Numbers[indexA] = Numbers[indexB]
    Numbers[indexB] = temp

doRender(0,0)
while run:
    doEvent()
    doLogic()
    #doRender()
pygame.quit()
try:
    exit()
except:
    print("An exception occurred.")



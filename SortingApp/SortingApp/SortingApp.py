import pygame
import winsound
from pygame.locals import *
import time
import random
import math
import colorsys
 


# Variables
FULLSCREEN = True
window_size = (500,500)
Line_Width = 10



pygame.init()
if FULLSCREEN:
    window = pygame.display.set_mode(flags = pygame.FULLSCREEN)
else:
    window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Sorting App")

Width,Height= pygame.display.get_surface().get_size()

Height_Padding = 50
Line_Start = (Height - Height_Padding)

Text_Pos = (math.floor(Width/2),(Height - math.floor((Height_Padding/2))))



run = True
Numbers = []
sortType = 0
doSort = False
setValue = True
mute = False

for i in range(math.floor(Width/Line_Width)):
    Numbers.append(random.randint(0,Line_Start))


        




font = pygame.font.SysFont("comicsansms",30)
cachedText = {}

def doRender():
    window.fill((0,0,0))
    

    global Numbers
    hsv_to_rgb = colorsys.hsv_to_rgb
    drawLine = pygame.draw.line
    length = len(Numbers)
    for x in range(length):
        h = Numbers[x]/(Line_Start)
        s = 1.0
        v = 1.0
        color = hsv_to_rgb(h,s,v)        
        r,g,b = color
        drawLine(window,(r*255,g*255,b*255),((x*Line_Width),Line_Start),(x*Line_Width,Numbers[x]),Line_Width)
        #if x == count:
        #    pygame.draw.line(window,(250,0,0),(x,Height-Hight_Padding),(x,Numbers[x]))
        #elif x == j:
        #    pygame.draw.line(window,(0,250,0),(x,Height-Hight_Padding),(x,Numbers[x]))
        #else:
        #    pygame.draw.line(window,(200,200,200),(x,Height-Hight_Padding),(x,Numbers[x]))
    
    
    sorterText = ""

    global sortType
    if(sortType == 0):
        sorterText = "Current Sorter: Selection Sort"
    elif(sortType == 1):
        sorterText = "Current Sorter: Insertion Sort"
    elif(sortType == 2):
        sorterText = "Current Sorter: Bubble Sort"
    elif(sortType == 3):
        sorterText = "Current Sorter: Merge Sort"
    elif(sortType == 4):
        sorterText = "Current Sorter: Quick Sort"
    elif(sortType == 5):
        sorterText = "Current Sorter: Heap Sort"
    elif(sortType == 6):
        sorterText = "Current Sorter: Shell Sort"
    global font
    global cachedText
    if sortType not in cachedText:
        cachedText[sortType] = font.render(sorterText,True,(200,200,200))
    text = cachedText[sortType]
    textRect = text.get_rect()
    textRect.center = Text_Pos
    pygame.display.get_surface().blit(text,textRect)
    pygame.display.update()

def doEvent():
    global run
    global sortType
    global doSort
    global setValue
    global Numbers

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print ("You pressed the left mouse button at (%d, %d)" % event.pos)
            w,h  = pygame.display.get_surface().get_size()
            x,y = event.pos
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_RETURN:
            print("Sorting....")
            doSort = True
            setValue = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_1 and not doSort:
            sortType = 0
            print("Setting Sorter to Selection Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_2 and not doSort:
            sortType = 1
            print("Setting Sorter to Insertion Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_3 and not doSort:
            sortType = 2
            print("Setting Sorter to Bubble Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_4 and not doSort:
            sortType = 3
            print("Setting Sorter to Merge Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_5 and not doSort:
            sortType = 4
            print("Setting Sorter to Quick Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_6 and not doSort:
            sortType = 5
            print("Setting Sorter to Heap Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_7 and not doSort:
            sortType = 6
            print("Setting Sorter to Shell Sort....")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_r:
            Numbers = []
            doSort = False
            setValue = True
            for i in range(math.floor(Width/Line_Width)):
                Numbers.append(random.randint(0,Line_Start))
            print("Reseting...")
            doRender()
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_ESCAPE:
            run = False

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
            count = SelectiveSort(Numbers,count,setValue)
        elif sortType == 1:
            #InsertionSort
            count = InsertionSort(Numbers,count, setValue)
        elif sortType == 2:
            #BubbleSort
            count = BubbleSort(Numbers,count, setValue)
        elif sortType == 3:
            #MergeSort
            MergeSort(Numbers,0,len(Numbers)-1)
            doSort = False
        elif sortType == 4:
            #QuickSort
            QuickSort(Numbers,0,len(Numbers)-1)
            doSort = False
        elif sortType == 5:
            #HeapSort
            HeapSort(Numbers,len(Numbers))
            doSort = False
        elif sortType == 6:
            #ShellSort
            ShellSort(Numbers,len(Numbers))

        setValue = False
        
        #print(Numbers)


def PlayBeep(index):
    if mute:
        return
    winsound.Beep(starting_frq + index,100)

def SelectiveSort(Numbers,count, setValue):
    if setValue:
        count = 0
    min_index = 0
    if count != None and count <= len(Numbers) - 1:
        min_index = count
        for j in range(count+1,len(Numbers)):
            if(Numbers[j] < Numbers[min_index]):
                min_index = j        
        Swap(min_index,count) 
        doRender()
        return count + 1
    global doSort
    doSort = False

def BubbleSort(Numbers,count, setValue):
    if setValue:
        count = 0
    if count != None and count < len(Numbers)-1:
        for j in range(len(Numbers)-count -1):
            if Numbers[j] > Numbers[j+1]:
                Swap(j,j+1)
        doRender()
        return count + 1
    global doSort
    doSort = False

def InsertionSort(Numbers,count, setValue):
    if setValue:
        count = 1
    if count != None and count < len(Numbers):
        j = count
        while(j > 0 and Numbers[j-1] > Numbers[j]):
            Swap(j,j-1)
            j = j-1
        doRender()
        return count + 1
    global doSort
    doSort = False

def MergeSort(arr,l,r):
    if l < r:
        m = int(l + (r-l)/2)       
        MergeSort(arr,l,m)       
        MergeSort(arr,m+1,r)
        Merge(arr,l,m,r)
        doRender()
        
    

        

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
    


def QuickSort(arr, l, h):
    if l < h:
        pi = Partition(arr,l,h)
        QuickSort(arr,l,pi-1)
        QuickSort(arr,pi+1,h)
        doRender()

def Partition(arr,l,h):
    pivot = arr[h]
    i = (l-1)
    for j in range(l,h):
        if arr[j] < pivot:
            i = i + 1
            Swap(i,j)
    Swap(i+1,h)
    return i+1

def HeapSort(arr,n):
    for i in range(math.floor(n/ 2)-1,-1,-1):
        Heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        Swap(0,i)
        Heapify(arr,i,0)
        doRender()

def Heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    
    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        Swap(i,largest)
        
        Heapify(arr,n,largest)
        
    

    
def ShellSort(arr, n):
    gap = math.floor(n/2)
    while gap > 0:
        
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = temp
        doRender()
        gap = math.floor(gap/2)
        
    global doSort
    doSort = False

def Swap(indexA, indexB):
    global Numbers
    temp = Numbers[indexA]
    Numbers[indexA] = Numbers[indexB]
    Numbers[indexB] = temp

doRender()
while run:
    doEvent()
    doLogic()
    #doRender()
pygame.quit()
try:
    exit()
except:
    print("An exception occurred.")



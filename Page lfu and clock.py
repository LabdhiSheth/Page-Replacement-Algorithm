#importing the libraries
from tkinter import *
import tkinter.font as font

#lfu algorithm
def create_window_lfu():
    window_lfu = Toplevel(root)

    global a, n, m
    num = Entry(window_lfu)
    page_no = Entry(window_lfu)
    frame = Entry(window_lfu)

    #to assign the size
    def n_assignment():
        global n
        n = int(num.get())
        print("Size of the Reference String : ",n)

    #to asssign the pages
    def pages():
        global a
        a = page_no.get()
        a = list(a)
        for i in range(0, len(a)):
            a[i] = int(a[i])
        print("Page numbers : ",a)

    #to assign the frame size
    def frame_no():
        global m
        m = int(frame.get())
        print("Frame size : ",m)

    #to call the functions
    def lfu_accept():
        global a, n, m
        a = []

        buttonfont = font.Font(family='Helvetica', size=10)

        lfu_stat = Label(window_lfu, text="\n",fg = '#e84854',bg = '#99b898')
        lfu_stat['font'] = myFont1
        lfu_stat.grid(column=0, row=3)
        print("LFU Algorithm - ")

        num_l = Label(window_lfu, text="Enter the size of reference string : ",fg = '#e84854',bg = '#99b898')
        num_l['font'] = myFont1
        num_l.grid(column=0, row=4)
        num.grid(column=1, row=4)
        btn = Button(window_lfu, text="submit", command=n_assignment,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=2, row=4)

        page_l = Label(window_lfu, text="Enter the page numbers : ",fg = '#e84854',bg = '#99b898')
        page_l['font'] = myFont1
        page_l.grid(column=0, row=5)
        page_no.grid(column=1, row=5)
        btn = Button(window_lfu, text="submit", command=pages,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=2, row=5)

        frame_l = Label(window_lfu, text="Enter the frame size : ",fg = '#e84854',bg = '#99b898')
        frame_l['font'] = myFont1
        frame_l.grid(column=0, row=6)
        frame.grid(column=1, row=6)
        btn = Button(window_lfu, text="submit", command=frame_no,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=2, row=6)

        space = Label(window_lfu, text="\n", bg='#99b898').grid(column=0, row=7)

        btn = Button(window_lfu, text="Show result", command = lfu,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=0, row=8)
        reset = Button(window_lfu,text = "reset",command = reset_val,bg='#feceab',fg='#2a363b')
        reset['font'] = buttonfont
        reset.grid(column = 1,row = 8)

        space = Label(window_lfu, text="\n", bg='#99b898').grid(column=0, row=9)

    #to reset the values
    def reset_val():
        num.delete(0,END)
        page_no.delete(0,END)
        frame.delete(0,END)

    #to quit the window
    def quit():
        window_lfu.destroy()

    #main code of lfu
    def lfu():
        global a, n, m
        x = 0
        page_faults = 0
        page = []
        time = {}
        b = a
        #print("b ", b)
        for i in range(m):
            page.append(-1)

        for i in a:
            time[i] = 0

        for i in range(n):
            flag = 0
            for j in range(m):
                if (page[j] == a[i]):
                    flag = 1
                    time[a[i]] += 1
                    break

            if flag == 0:
                rpage = -1
                if page[x] != -1:

                    t = []
                    for k in page:
                        t.append(time[k])

                    minis = min(t)

                    gpage = []
                    for k in page:
                        if time[k] == minis:
                            gpage.append(k)

                    maxi = -1
                    flag = 0

                    for k in gpage:
                        for n in range(0, i):
                            if (k == b[n]):
                                if maxi == -1:
                                    maxi = n
                                    rpage = k
                                elif n < maxi:
                                    maxi = n
                                    rpage = k
                        flag = 1

                    if (flag == 1):
                        b[maxi] = -1
                        x = page.index(rpage)

                if rpage != -1:
                    time[rpage] = 0

                page[x] = a[i]
                x = (x + 1) % m
                time[a[i]] += 1
                page_faults += 1
                row_id = 8
                column_id = 0
                print("\n{0} ->".format(a[i]))
                for j in range(m):
                    if page[j] != -1:
                        print(page[j])
                    else:
                        print("--")
            else:
                print("\n{0} -> No Page Fault".format(a[i]))

        faults = Label(window_lfu, text="\n Result : \nTotal page faults are : " + str(page_faults),fg = '#e84854',bg = '#99b898')
        faults['font'] = myFont1
        faults.grid(column=0, row=9)
        freq_time = Label(window_lfu, text="\n Frequencies of pages : " + str(time),fg = '#e84854',bg = '#99b898')
        freq_time['font'] = myFont1
        freq_time.grid(column=0, row=10)

        stop = Button(window_lfu, text="EXIT", command=quit, bg='#feceab', fg='#2a363b')
        stop['font'] = buttonfont
        stop.grid(column=0, row=11)

        space = Label(window_lfu, text="\n",bg='#99b898').grid(column = 0, row = 12)

    window_lfu.configure(bg='#99b898')
    myFont = font.Font(family='Helvetica', size=30, weight='bold')
    lbl = Label(window_lfu,text = "\nLeast frequently Used Algorithm\n",fg = '#28363b',bg = '#99b898')
    lbl['font'] = myFont
    lbl.grid(column = 0,row = 0)

    myFont1 = font.Font(family='Helvetica', size=18, weight='bold')
    desc = Label(window_lfu,text = " In current stack at any iteration we choose that element  \nfor replacement which has smallest count in \nthe incoming page stream.\n",fg = '#e84854',bg = '#99b898')
    desc['font'] = myFont1
    desc.grid(column = 0,row = 1)

    lfu_btn = Button(window_lfu, text="Click here to calculate", command=lfu_accept, bg = '#28363b',fg = '#e84854',padx = 10, pady = 5,relief = RAISED)
    lfu_btn['font'] = myFont1
    lfu_btn.grid(column=0, row=2)

    space = Label(window_lfu, text="\n\n", bg='#99b898').grid(column=0, row = 3)



#clock replacement -
def create_window_clock():
    window_clock = Toplevel(root)

    global strdd, frames
    str_in = Entry(window_clock)
    frames_no = Entry(window_clock)

    #accept the page numbers
    def str_accept():
        global strdd
        strdd = str_in.get()
        strdd = list(strdd)
        for i in range(0, len(strdd)):
            strdd[i] = int(strdd[i])
        print("Pages numbers are : ",strdd)

    #accept the page size
    def frame_accept():
        global frames
        frames = int(frames_no.get())
        print("Frame Size : ",frames)

    #call the functions
    def clock_accept():

        print("Clock Replacement Algorithm - \n")

        space = Label(window_clock, text="\n", bg='#99b898').grid(column=0, row=3)

        page_l = Label(window_clock, text="Enter the page numbers : ",fg = '#e84854',bg = '#99b898')
        page_l['font'] = myFont1
        page_l.grid(column=0, row=4)
        str_in.grid(column=1, row=4)
        btn = Button(window_clock, text="submit", command=str_accept,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=2, row=4)

        frame_l = Label(window_clock, text="Enter the frame size : ",fg = '#e84854',bg = '#99b898')
        frame_l['font'] = myFont1
        frame_l.grid(column=0, row=5)
        frames_no.grid(column=1, row=5)
        btn = Button(window_clock, text="submit", command=frame_accept,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=2, row=5)

        space = Label(window_clock, text="\n", bg='#99b898').grid(column=0, row=6)

        btn = Button(window_clock, text="Show result", command=clock,bg='#feceab',fg='#2a363b')
        btn['font'] = buttonfont
        btn.grid(column=0, row=7)
        reset = Button(window_clock, text="reset", command=reset_clock,bg='#feceab',fg='#2a363b')
        reset['font'] = buttonfont
        reset.grid(column=1, row=7)

        space = Label(window_clock, text="\n", bg='#99b898').grid(column=0, row=8)

    #reset the values
    def reset_clock():
        str_in.delete(0, END)
        frames_no.delete(0, END)

    #quit the window
    def quit_c():
        window_clock.destroy()

    #main code
    def clock():
        global strdd, frames
        pointer = 0
        i = 0
        l = 0
        x = 0
        pf = 0
        arr = []
        for i in range(0, frames):
            arr.append(-1)
        second_chance = [True for i in range(frames)]

        l = len(strdd)
        for i in range(0, l):
            x = int(strdd[i])
            if (not findAndUpdate(x, arr, second_chance)):
                pointer = replaceAndUpdate(x, arr, second_chance, pointer)
                pf = pf + 1

        result = Label(window_clock,text = "\nTotal number of page faults are : "+ str(pf)+"\n",fg = '#e84854',bg = '#99b898')
        result['font'] = myFont1
        result.grid(column = 0,row = 8)

        stop = Button(window_clock, text="EXIT", command=quit_c, bg='#feceab', fg='#2a363b')
        stop['font'] = buttonfont
        stop.grid(column=0, row=9)

        space = Label(window_clock, text="\n", bg='#99b898').grid(column=0, row=10)

    def findAndUpdate(x, arr, second_chance):
        global strdd, frames
        i = 0

        for i in range(0, frames):
            if (arr[i] == x):
                second_chance.append(True)
                return True
        else:
            return False

    def replaceAndUpdate(x, arr, second_chance, pointer):
        global strdd, frames
        while (True):

            if (not second_chance[pointer]):
                print("\n{0} ->".format((arr[pointer])))
                arr[pointer] = x
                return ((pointer + 1) % frames)

            second_chance[pointer] = False
            pointer = ((pointer + 1) % frames)

    myFont = font.Font(family='Helvetica', size=30, weight='bold')
    window_clock.configure(bg='#99b898')

    heading = Label(window_clock,text = "\nClock replacement Algorithm\n",fg = '#28363b',bg = '#99b898')
    heading['font'] = myFont
    heading.grid(column = 0,row = 0)

    about = Label(window_clock,text = "Clock is a more efficient version of FIFO than Second-chance because pages "
                                      "\ndon't have to be constantly pushed to the back of the list,"
                                      "\n but it performs the same general function as Second-Chance.The clock "
                                      "\nalgorithm keeps a circular list of pages in memory, with the 'hand' pointing "
                                      "\nto the last examined page frame in the list.\n",fg = '#e84854',bg = '#99b898')
    about['font'] = myFont1
    about.grid(column = 0,row = 1)

    clock_btn = Button(window_clock, text="Click here to calculate", command=clock_accept,bg = '#28363b',fg = '#e84854',padx = 10, pady = 5,relief = RAISED)
    clock_btn['font'] = buttonfont
    clock_btn.grid(column=0, row=2)

    space = Label(window_clock, text="\n\n", bg='#99b898').grid(column=0, row=3)

#main
root = Tk()
root.title("Page Replacement Algorithms")
root.geometry('852x600')
root.configure(bg = '#28363b')

font1 = font.Font(family='Helvetica', size=40, weight='bold')
title = Label(root,text = "\n Page Replacement Algorithm \n  ",bg = '#28363b', fg = "#e84854")
title['font'] = font1
title.grid(column = 0,row = 0)

myFont = font.Font(family='Helvetica', size=20)
about = Label(root,text = "Page replacement is a process of swapping out an existing page from \nthe frame of a main memory and replacing it with the required page.",bg = '#28363b',fg = '#99b898')
about['font'] = myFont
about.grid(column = 0,row = 1)

myFont1 = font.Font(family='Helvetica', size=20,weight = 'bold')
option = Label(root,text = "\nWhich algorithm do you wish to perform ?\n",bg = '#28363b', fg = "#e84854")
option['font'] = myFont1
option.grid(column = 0,row = 2)

buttonfont = font.Font(family='Helvetica', size=14,weight = 'bold')
lfu = Button(root, text="Least Frequently used Algorithm", command=create_window_lfu,fg = '#28363b',bg = '#99b898',padx = 5, pady = 5,relief = RAISED)
lfu['font'] = buttonfont
lfu.grid(column = 0,row = 3)

lbl = Label(root, text = "\nOR\n",bg = '#28363b',fg = '#99b898')
lbl['font'] = myFont
lbl.grid(column = 0,row = 4)

clock = Button(root, text="Clock Replacement Algorithm", command=create_window_clock,fg = '#28363b',bg = '#99b898',padx = 10, pady = 5,relief = RAISED)
clock['font'] = buttonfont
clock.grid(column = 0,row = 5)

root.mainloop()
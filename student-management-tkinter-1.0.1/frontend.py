from tkinter import *
# import backend
import backendtxt as backend
   
'''0: no select
    1: select DanhSach
    2: select Diem
    3: select Truong
'''
selected_view = 0

def get_selected_row(event):
    ''' get_selected_row function to get content of the selected row.
    
        Arguments
        ---------
        event: a virtual interrupt.
    '''
    global selected_tuple
    if lb1.curselection() != ():
 
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        clear_entries()
        insert_entries()

def view_command():
    if selected_view == 1:
        viewds_command()
    elif selected_view == 2:
        viewdiem_command()
    elif selected_view == 3:
        viewtruong_command()

def viewds_command():
    ''' view_command function to show the output database.
    
    '''
    global selected_view
    selected_view = 1
    lb1.delete(0,END)
    lst = []  
    for row in backend.view_ds():
        #row = list(str(i).strip() for i in row)
        row = list(row)
        if int(row[3]) == 0:
            row[3] ='Nam'
        else:
            row[3] = 'Nu'
        
        # newRow = (str(row[0]).strip()+' '*(7-len(str(row[0]).strip())),\
        # row[1].strip()+' ',\
        # row[2].strip() + (23-len(row[1].strip()+' ')-len(row[2].strip()))* ' ',\
        # sex +' '*(4-len(sex)),row[4],row[5].strip())
        lb1.insert(END,row)
    view_entries()

def viewdiem_command():
    ''' view_command function to show the output database.
    
    '''
    global selected_view
    selected_view = 2
    lb1.delete(0,END)  
    for row in backend.view_diem():
        lb1.insert(END,row)
    view_entries()

def viewtruong_command():
    ''' view_command function to show the output database.
    
    '''
    global selected_view
    selected_view = 3
    lb1.delete(0,END)  
    for row in backend.view_truong():
        lb1.insert(END,row)
    view_entries()

def remove_entries():
    l1.grid_remove()
    l2.grid_remove()
    l3.grid_remove()
    l4.grid_remove()
    l5.grid_remove()
    l6.grid_remove()
    e1.grid_remove()
    e2.grid_remove()
    e3.grid_remove()
    e4.grid_remove()
    e5.grid_remove()
    e6.grid_remove()

    l7.grid_remove()
    l8.grid_remove()
    l9.grid_remove()
    e7.grid_remove()
    e8.grid_remove()
    e9.grid_remove()

    l10.grid_remove()
    l11.grid_remove()
    e10.grid_remove()
    e11.grid_remove()

def view_entries():
    remove_entries()
    if selected_view == 1:
        l1.grid(row=1,column=0)
        l2.grid(row=1,column=2)
        l3.grid(row=2,column=0)
        l4.grid(row=2,column=2)
        l5.grid(row=3,column=0)
        l6.grid(row=3,column=2)

        e1.grid(row=1,column=1)
        e2.grid(row=1,column=3)
        e3.grid(row=2,column=1)
        e4.grid(row=2,column=3)
        e5.grid(row=3,column=1)
        e6.grid(row=3,column=3)
    elif selected_view == 2:
        l7.grid(row=1,column=0)
        l8.grid(row=1,column=2)
        l9.grid(row=2,column=0)
        e7.grid(row=1,column=1)
        e8.grid(row=1,column=3)
        e9.grid(row=2,column=1)

    elif selected_view == 3:
        l10.grid(row=1,column=0)
        l11.grid(row=1,column=2)
        e10.grid(row=1,column=1)
        e11.grid(row=1,column=3)

def phai_s_to_i(phai):
    result = 0
    if phai.strip() == "Nu":
        result = 1
    return result

def add_before_command():
    ''' Chèn trước
    
    '''
    index = lb1.curselection()[0]
    if selected_view == 1:
        backend.insert_ds(index,mahs.get(),ho.get(),ten.get(),phai_s_to_i(phai.get()),ngaysinh.get(),matruong.get(),"truoc")
    elif selected_view == 2:
        backend.insert_diem(index,mahs1.get(),mon.get(),diem.get(),"truoc")
    elif selected_view == 3:
         backend.insert_truong(index,matruong1.get(),tentruong.get(),"truoc")
    clear_entries()
    view_command()

def add_after_command():
    ''' Chèn sau
    
    '''
    index = lb1.curselection()[0]
    if selected_view == 1:
        backend.insert_ds(index,mahs.get(),ho.get(),ten.get(),phai_s_to_i(phai.get()),ngaysinh.get(),matruong.get(),"sau")
    elif selected_view == 2:
        backend.insert_diem(index,mahs1.get(),mon.get(),diem.get(),"sau")
    elif selected_view == 3:
         backend.insert_truong(index,matruong1.get(),tentruong.get(),"sau")
    clear_entries()
    view_command()
    
    clear_entries()
    view_command()
    
def delete_command():
    ''' Xóa bản ghi
    
    '''
    if selected_view == 0 or len(lb1.curselection()) == 0:
        return
    index = lb1.curselection()[0]
    selected_tuple = lb1.get(index)
    backend.delete(selected_tuple[0], selected_view, selected_tuple[1])
    clear_entries()
    view_command()

def delete_data_command():
    ''' xoa database.
    
    '''
    backend.delete_data()
    view_command()

def clear_entries():
    ''' clear_entries function to clear content of entries.
    
    '''

    if selected_view == 1:
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
    elif selected_view == 2:
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
    elif selected_view == 3:
        e10.delete(0,END)
        e11.delete(0,END)

def insert_entries():
    ''' insert_entries function to insert content of entries.
    
    '''

    if selected_view == 1:
        e1.insert(END,selected_tuple[0].strip())
        e2.insert(END,selected_tuple[1].strip())
        e3.insert(END,selected_tuple[2].strip())
        e4.insert(END,selected_tuple[3].strip())
        e5.insert(END,selected_tuple[4].strip())
        e6.insert(END,selected_tuple[5].strip())
    elif selected_view == 2:
        e7.insert(END,selected_tuple[0])
        e8.insert(END,selected_tuple[1])
        e9.insert(END,selected_tuple[2])
    elif selected_view == 3:
        e10.insert(END,selected_tuple[0].strip())
        e11.insert(END,selected_tuple[1].strip())

def view_item5_command():
    # viet ra file: "item5.txt"
    output_file = backend.view_item5()

    # doc noi dung file
    list_data = backend.read_file_data(output_file)
    
    # khai báo Tinker Window listbox mới
    item5Window = Tk()
    item5Window.title("Yêu cầu số 5 - Danh sach từng HS và điểm")
    item5Window.geometry('1200x400')

    listbox = Listbox(item5Window)
    listbox.pack(fill=BOTH, expand=True)
    listbox.config(font=("Courier", 10))
    fixedlen = 12
    margin = " "
    # loop và display từng record trong file txt
    for i in list_data:
        info = [x.strip() for x in i.split(',')]
        item = ("{:<3s}"+(fixedlen-len(info[0]))*margin \
        + "{:<2s}"+(15-len(info[1]))*margin \
        + "{:<2s}"+(fixedlen-len(info[2]))*margin \
        + "{:<1s}"+(fixedlen-len(info[3]))*margin \
        + "{:<3s}"+(15-len(info[4]))*margin \
        + "{:<1s}"+(fixedlen-len(info[5]))*margin \
        + "{:<1s}"+(fixedlen-len(info[6]))*margin \
        + "{:<1s}"+(fixedlen-len(info[7]))*margin \
        + "{:<1s}"+(fixedlen-len(info[8]))*margin \
        + "{:<3s}"+(fixedlen-len(info[9]))*margin \
        + "{:<5s}").format(info[0],info[1],info[2],info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10])
        #print(item)
        listbox.insert(END, item)

    item5Window.mainloop() 

def view_item6_command():
    # viet ra file: "item5.txt"
    output_file = backend.view_item6()

    # doc noi dung file
    list_data = backend.read_file_data(output_file)
    
    # khai báo Tinker Window listbox mới
    item6Window = Tk()
    item6Window.title("Yêu cầu số 6 - Học sinh có điểm Toán lớn hơn điểm Văn ")
    item6Window.geometry('1200x400')

    listbox = Listbox(item6Window)
    listbox.pack(fill=BOTH, expand=True)
    listbox.config(font=("Courier", 10))
    fixedlen = 12
    margin = " "
    # loop và display từng record trong file txt
    for i in list_data:
        info = [x.strip() for x in i.split(',')]
        item = ("{:<3s}"+(fixedlen-len(info[0]))*margin \
        + "{:<2s}"+(15-len(info[1]))*margin \
        + "{:<2s}"+(fixedlen-len(info[2]))*margin \
        + "{:<1s}"+(fixedlen-len(info[3]))*margin \
        + "{:<3s}"+(15-len(info[4]))*margin \
        + "{:<1s}"+(fixedlen-len(info[5]))*margin \
        + "{:<1s}"+(fixedlen-len(info[6]))*margin \
        + "{:<5s}").format(info[0],info[1],info[2],info[3], info[4], info[5], info[6], info[7])
        #print(item)
        listbox.insert(END, item)

    item6Window.mainloop() 

def view_item7_command():
    # viet ra file: "item5.txt"
    output_file = backend.view_item7()

    # doc noi dung file
    list_data = backend.read_file_data(output_file)
    
    # khai báo Tinker Window listbox mới
    item7Window = Tk()
    item7Window.title("Yêu cầu số 7 - Học sinh Kém")
    item7Window.geometry('1200x400')

    listbox = Listbox(item7Window)
    listbox.pack(fill=BOTH, expand=True)
    listbox.config(font=("Courier", 10))
    fixedlen = 12
    margin = " "
    # loop và display từng record trong file txt
    for i in list_data:
        info = [x.strip() for x in i.split(',')]
        item = ("{:<3s}"+(fixedlen-len(info[0]))*margin \
        + "{:<2s}"+(15-len(info[1]))*margin \
        + "{:<2s}"+(fixedlen-len(info[2]))*margin \
        + "{:<1s}"+(fixedlen-len(info[3]))*margin \
        + "{:<3s}"+(15-len(info[4]))*margin \
        + "{:<1s}"+(fixedlen-len(info[5]))*margin \
        + "{:<1s}"+(fixedlen-len(info[6]))*margin \
        + "{:<1s}"+(fixedlen-len(info[7]))*margin \
        + "{:<3s}"+(fixedlen-len(info[8]))*margin \
        + "{:<5s}").format(info[0],info[1],info[2],info[3], info[4], info[5], info[6], info[7], info[8], info[9])
        #print(item)
        listbox.insert(END, item)

    item7Window.mainloop() 

def view_item8_command():
    # viet ra file: "item5.txt"
    output_file = backend.view_item8()

    # doc noi dung file
    list_data = backend.read_file_data(output_file)
    
    # khai báo Tinker Window listbox mới
    item8Window = Tk()
    item8Window.title("Yêu cầu số 8 - Học Sinh thủ khoa  của từng trường có tổng điểm cao nhất")
    item8Window.geometry('1200x400')

    listbox = Listbox(item8Window)
    listbox.pack(fill=BOTH, expand=True)
    listbox.config(font=("Courier", 10))
    fixedlen = 12
    margin = " "
    # loop và display từng record trong file txt
    for i in list_data:
        info = [x.strip() for x in i.split(',')]
        item = ("{:<3s}"+(fixedlen-len(info[0]))*margin \
        + "{:<2s}"+(15-len(info[1]))*margin \
        + "{:<2s}"+(fixedlen-len(info[2]))*margin \
        + "{:<1s}"+(fixedlen-len(info[3]))*margin \
        + "{:<3s}"+(15-len(info[4]))*margin \
        + "{:<1s}"+(fixedlen-len(info[5]))*margin \
        + "{:<1s}"+(fixedlen-len(info[6]))*margin \
        + "{:<1s}"+(fixedlen-len(info[7]))*margin \
        + "{:<3s}"+(fixedlen-len(info[8]))*margin \
        + "{:<5s}").format(info[0],info[1],info[2],info[3], info[4], info[5], info[6], info[7], info[8], info[9])
        #print(item)
        listbox.insert(END, item)

    item8Window.mainloop() 

def view_item9_command():
    #Viet ra file "item9.txt"
    output_file = backend.view_item9(e6.get())
    # doc noi dung file
    list_data = backend.read_file_data(output_file)
    
    # khai báo Tinker Window listbox mới
    item9Window = Tk()
    item9Window.title("Yêu cầu số 9 - Chỉ gồm các học sinh của trường đó")
    item9Window.geometry('1200x400')

    listbox = Listbox(item9Window)
    listbox.pack(fill=BOTH, expand=True)
    listbox.config(font=("Courier", 10))
    fixedlen = 12
    margin = " "
    # loop và display từng record trong file txt
    for i in list_data:
        info = [x.strip() for x in i.split(',')]
        item = ("{:<3s}"+(fixedlen-len(info[0]))*margin \
        + "{:<2s}"+(15-len(info[1]))*margin \
        + "{:<2s}"+(fixedlen-len(info[2]))*margin \
        + "{:<1s}"+(fixedlen-len(info[3]))*margin \
        + "{:<3s}"+(15-len(info[4]))*margin \
        + "{:<1s}"+(fixedlen-len(info[5]))*margin \
        + "{:<1s}"+(fixedlen-len(info[6]))*margin \
        + "{:<1s}"+(fixedlen-len(info[7]))*margin \
        + "{:<1s}"+(fixedlen-len(info[8]))*margin \
        + "{:<3s}"+(fixedlen-len(info[9]))*margin \
        + "{:<5s}").format(info[0],info[1],info[2],info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10])
        #print(item)
        listbox.insert(END, item)

    item9Window.mainloop() 

def view_item10_command():

    global listbox10_1
    global listbox10_2
    global listbox10_3
    global item10Window
    
    #Viet ra file "item10.txt"
    output_file = backend.view_item10()
    # doc noi dung file
    list_data = backend.read_file_data(output_file)

    header = "GIAY BAO DIEM"
    
    # khai báo Tinker Window listbox mới
    item10Window = Tk()
    item10Window.title("Yêu cầu số 10 - GIAY BAO DIEM")
    item10Window.geometry('1200x400')

    

    # listbox thứ 1
    listbox10_1 = Listbox(item10Window, height = 15, width = 40)
    #listbox10_1.pack(fill=BOTH, expand=True)
    listbox10_1.config(font=("Courier", 10, "bold"), bd = 4)
    # loop và display từng record trong file txt
    listbox10_1.insert(END, header)
    elments = list_data[0].split(',')
    for element in elments:
        listbox10_1.insert(END, element)

    # listbox thứ 2
    listbox10_2 = Listbox(item10Window, height = 15, width = 40)
    #listbox10_2.pack(fill=BOTH, expand=True)
    listbox10_2.config(font=("Courier", 10, 'bold'), bd = 4)
    # loop và display từng record trong file txt
    listbox10_2.insert(END, header)
    elments = list_data[1].split(',')
    for element in elments:
        listbox10_2.insert(END, element)

    # listbox thứ 3
    listbox10_3 = Listbox(item10Window, height = 15, width = 40)
    #listbox10_3.pack(fill=BOTH, expand=True)
    listbox10_3.config(font=("Courier", 10, 'bold'), bd = 4)
    # loop và display từng record trong file txt
    listbox10_3.insert(END, header)
    elments = list_data[2].split(',')
    for element in elments:
        listbox10_3.insert(END, element)
    
    #Button Search
    bSearch = Button(item10Window, bg = 'green', fg = 'white', height = 2, width=10, text='Search', command= update_item10_data_command)

    listbox10_1.grid(row=0, column=0,rowspan=10, columnspan=2, pady= 20, padx = 20)
    listbox10_2.grid(row=0, column=2,rowspan=10, columnspan=2, pady= 20, padx = 20)
    listbox10_3.grid(row=0, column=4,rowspan=10, columnspan=2, pady= 20, padx = 20)
    bSearch.grid(row = 7, column = 2,rowspan=10, columnspan=2, pady= 350, padx=100)
    
    item10Window.mainloop() 

def update_item10_data_command():

    global listbox10_1
    global listbox10_2
    global listbox10_3
    global item10Window

    #Viet ra file "item10.txt"
    output_file = backend.view_item10()
    # doc noi dung file
    list_data = backend.read_file_data(output_file)
    
    header = "GIAY BAO DIEM"

    # listbox thứ 1
    listbox10_1.delete(0,END)
    listbox10_1.insert(END, header)
    elments = list_data[0].split(',')
    for element in elments:
        listbox10_1.insert(END, element)

    # listbox thứ 2
    listbox10_2.delete(0,END)
    listbox10_2.insert(END, header)
    elments = list_data[1].split(',')
    for element in elments:
        listbox10_2.insert(END, element)

    # listbox thứ 3
    listbox10_3.delete(0,END)
    listbox10_3.insert(END, header)
    elments = list_data[2].split(',')
    for element in elments:
        listbox10_3.insert(END, element)

def clear_command():
    ''' view_command function to clear content of Listbox.
    
    '''
    lb1.delete(0,END)
    clear_entries()

wind = Tk()
wind.title("Phần mềm quản lý học sinh")
wind.geometry('950x500')

l0 = Label(wind, text = "Students", width = "10", fg = "blue")
l0.config(font=("Courier", 15))

l00 = Label(wind, text = "Management", width = "10", fg = "blue")
l00.config(font=("Courier", 15))

# Danh Sach
mahs = StringVar()
ho = StringVar()
ten = StringVar()
phai = StringVar()
ngaysinh = StringVar()
matruong = StringVar()

l1 = Label(wind, text = "MaHS", width = "10")
l2 = Label(wind, text = "Ho", width = "10")
l3 = Label(wind, text = "Ten", width = "10")
l4 = Label(wind, text = "Phai", width = "10")
l5 = Label(wind, text = "NgaySinh", width = "10")
l6 = Label(wind, text = "MaTruong", width = "10")

e1 = Entry(wind, textvariable =mahs)
e2 = Entry(wind, textvariable =ho, width= 40)
e3 = Entry(wind, textvariable =ten)
e4 = Entry(wind, textvariable =phai, width= 40)
e5 = Entry(wind, textvariable =ngaysinh)
e6 = Entry(wind, textvariable =matruong, width= 40)

# Diem
mahs1 = StringVar()
mon = StringVar()
diem = StringVar()
l7 = Label(wind, text = "MaHS", width = "10")
l8 = Label(wind, text = "Mon", width = "10")
l9 = Label(wind, text = "Diem", width = "10")
e7 = Entry(wind, textvariable =mahs1)
e8 = Entry(wind, textvariable =mon,width=40)
e9 = Entry(wind, textvariable =diem)

# Truong
matruong1 = StringVar()
tentruong = StringVar()
l10 = Label(wind, text = "MaTruong", width = "10")
l11 = Label(wind, text = "TenTruong", width = "10")
e10 = Entry(wind, textvariable =matruong1)
e11 = Entry(wind, textvariable =tentruong,width=40)

# Các buttons
b1ds = Button(wind, text = "Xem DanhSach", width = "15", command = viewds_command)
b1diem = Button(wind, text = "Xem Diem", width = "15", command = viewdiem_command)
b1truong = Button(wind, text = "Xem Truong", width = "15", command = viewtruong_command)
b2delete = Button(wind, text = "Xóa", width = "15", command = delete_command)
b3addbefore = Button(wind, text = "Chèn Trước", width = "15", command = add_before_command)
b4addafter = Button(wind, text = "Chèn Sau", width = "15", command = add_after_command)
b5 = Button(wind, text = "Xem Mục 5", width = "15", command = view_item5_command)
b6 = Button(wind, text = "Xem Mục 6", width = "15", command = view_item6_command)
b7 = Button(wind, text = "Xem Mục 7", width = "15", command = view_item7_command)
b8 = Button(wind, text = "Xem Mục 8", width = "15", command = view_item8_command)
b9 = Button(wind, text = "Xem Mục 9", width = "15", command = view_item9_command)
b10 = Button(wind, text = "Xem Mục 10", width = "15", command = view_item10_command)
b11 = Button(wind, text = "Xóa Data", width = "15", command = delete_data_command)
bExit = Button(wind, text = "Exit", width = "15", command = wind.destroy)

# Listbox
lb1 = Listbox(wind, height = 15, width = 70,selectmode = 'single',exportselection= False)
lb1.bind('<<ListboxSelect>>',get_selected_row)

sc1 = Scrollbar(wind)

l0.grid(row=0,column=1)
l00.grid(row=0,column=2)

b1ds.grid(row=4,column=3)
b1diem.grid(row=5,column=3)
b1truong.grid(row=6,column=3)
b2delete.grid(row=7,column=3)
b3addbefore.grid(row=8,column=3)
b4addafter.grid(row=9,column=3)
b5.grid(row=10,column=3)
b6.grid(row=11,column=3)
b7.grid(row=12,column=3)
b8.grid(row=13,column=3)
b9.grid(row=14,column=3)
b10.grid(row=15,column=3)
#b11.grid(row=19,column=3)
bExit.grid(row=20,column=3)

lb1.grid(row=4, column=0,rowspan=10, columnspan=2, pady= 20)

sc1.grid(row=4,column=2,rowspan=8)

lb1.configure(yscrollcommand=sc1.set)
lb1.config(font=("Courier", 10))

sc1.configure(command=lb1.yview)
e6.rowconfigure(4, pad=10)

wind.mainloop()

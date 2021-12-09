''' backendtxt will work with data from "./datafiles" folder
Not from database
'''
import os
import csv
import random

def view_ds():
    ''' view 
    '''
    rows = []
    with open('./DataFilesTxt/DanhDach.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            rows.append(i)
    # print(rows)
    return rows

def view_diem():
    ''' view 
    '''
    rows = []
    with open('./DataFilesTxt/Diem.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            rows.append(i)
    return rows

def view_truong():
    ''' view 
    '''
    rows = []
    with open('./DataFilesTxt/Truong.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            rows.append(i)
    return rows

def delete(id, table, option_val=""):
    ''' delete function to delete a specific record.
    '''
    danh_sach = view_ds()
    danh_sach_copy = danh_sach.copy()

    diem = view_diem()
    diem_copy = diem.copy()

    truong = view_truong()
    truong_copy = truong.copy()

    if table == 1:
        filePath = "./DataFilesTxt/DanhDach.csv"
        for i in danh_sach:
            if i[0] == id:
                danh_sach_copy.remove(i)
        write_file_csv(filePath,danh_sach_copy)
    elif table == 2:
        filePath = "./DataFilesTxt/Diem.csv"
        for i in diem:
            if i[0] == id and i[1] == option_val:
                diem_copy.remove(i)
        write_file_csv(filePath,diem_copy)
    elif table == 3:
        filePath = "./DataFilesTxt/Truong.csv"
        for i in truong:
            if i[0] == id:
                truong_copy.remove(i)
        write_file_csv(filePath,truong_copy)

def insert_ds(index,mahs,ho,ten,phai,ngaysinh,matruong,vitri="truoc"):
    ''' insertion function to insert a new record to the database.
    
        Arguments
        ---------
    '''
    
    filePath = "./DataFilesTxt/DanhDach.csv"
    startEffectedRow = index
    if vitri == "sau":
        startEffectedRow += 1
    listDs = view_ds()
    elm = [mahs,ho,ten,phai,ngaysinh,matruong]
    diem_copy = listDs[0:startEffectedRow] + [elm] + listDs[startEffectedRow:]
    write_file_csv(filePath,diem_copy)

def insert_diem(index,mahs,mon,diem,vitri="truoc"):
    ''' insertion function to insert a new record to the database.
    
        Arguments
        ---------
    '''
    filePath = "./DataFilesTxt/Diem.csv"
    startEffectedRow = index
    if vitri == "sau":
        startEffectedRow += 1
    listDiem = view_diem()
    elm = [mahs,mon,diem]
    diem_copy = listDiem[0:startEffectedRow] + [elm] + listDiem[startEffectedRow:]
    write_file_csv(filePath,diem_copy)

def insert_truong(index,matruong,tentruong,vitri="truoc"):
    ''' insertion function to insert a new record to the database.
    
        Arguments
        ---------
    '''
    filePath = "./DataFilesTxt/Truong.csv"
    startEffectedRow = index
    if vitri == "sau":
        startEffectedRow += 1
    listTruong = view_truong()
    elm = [matruong,tentruong]
    truong_copy = listTruong[0:startEffectedRow] + [elm] + listTruong[startEffectedRow:]
    write_file_csv(filePath,truong_copy)

def view_item5():
    ''' truy xuất theo yêu cầu số 5. 
        Kết quả file: item5.txt
    '''
    danh_sach = view_ds()
    diem = view_diem()
    list_result = []
    for ds in danh_sach:
        data = {}
        data["SBD"] = ds[0]
        data["Ho"] = ds[1]
        data["Ten"] = ds[2]
        data["Phai"] = ds[3]
        data["NgaySinh"] = ds[4]
        data["Toan"] = 0
        data["Van"] = 0
        data["TongDiem"] = 0
        data["DTN"] = 0
        data["XepLoai"] = None
        data["MaTruong"] = ds[5]
        for d in diem:
            if data["SBD"] == d[0]:
                if d[1].strip()=="Toan":
                    data["Toan"] = float(d[2])
                if d[1].strip()=="Van":
                    data["Van"] = float(d[2])
                if data["Van"] != 0 and data["Toan"] != 0:
                    data["TongDiem"] = data["Toan"] + data["Van"]
                    data["DTN"] = min(data["Toan"],data["Van"])
                    data["XepLoai"] = get_xeploai(data["Toan"], data["Van"])
                    break


        list_result.append(data)
    mylist = sorted(list_result, key=lambda k: (k['MaTruong'].lower(), k['Ten'].lower(), k['Ho'].lower()))
    header = "SBD,  Ho, Ten,  Phai, NgaySinh, Toan,  Van, TongDiem, DTN, XepLoai, MaTruong"
    file_name = "item5.txt"
    write_to_file(file_name, mylist, header)
    return file_name

def view_item6():
    ''' truy xuất theo yêu cầu số 6. 
        Kết quả file: item6.txt
    '''
    danh_sach = view_ds()
    diem = view_diem()
    list_result = []
    for ds in danh_sach:
        data = {}
        data["SDB"] = ds[0]
        data["Ho"] = ds[1]
        data["Ten"] = ds[2]
        data["Phai"] = ds[3]
        data["NgaySinh"] = ds[4]
        data["Toan"] = 0
        data["Van"] = 0
        # data["TongDiem"] = 0
        # data["DTN"] = 0
        # data["XepLoai"] = None
        data["MaTruong"] = ds[5]
        for d in diem:
            if data["SDB"] == d[0]:
                if d[1].strip()=="Toan":
                    data["Toan"] = float(d[2])
                if d[1].strip()=="Van":
                    data["Van"] = float(d[2])
                if data["Toan"] != 0 and data["Van"] != 0:
                    break
        if data["Toan"] > data["Van"]:       
            list_result.append(data)
    mylist = sorted(list_result, key=lambda k: (k['MaTruong'].lower(), k['Ten'].lower(), k['Ho'].lower()))
    header = "SBD,  Ho, Ten,  Phai, NgaySinh, Toan,  Van, MaTruong"
    file_name = "item6.txt"
    write_to_file(file_name, mylist, header)
    return file_name

def view_item7():
    ''' truy xuất theo yêu cầu số 7. 
        Kết quả file: item7.txt
    '''
    danh_sach = view_ds()
    diem = view_diem()
    list_result = []
    for ds in danh_sach:
        data = {}
        data["SDB"] = ds[0]
        data["Ho"] = ds[1]
        data["Ten"] = ds[2]
        data["Phai"] = ds[3]
        data["NgaySinh"] = ds[4]
        data["Toan"] = 0
        data["Van"] = 0
        data["TongDiem"] = 0
        data["XepLoai"] = None
        data["MaTruong"] = ds[5]
        for d in diem:
            if data["SDB"] == d[0]:
                if d[1].strip()=="Toan":
                    data["Toan"] = float(d[2])
                if d[1].strip()=="Van":
                    data["Van"] = float(d[2])
                data["TongDiem"] = data["Toan"] + data["Van"]
                data["XepLoai"] = get_xeploai(data["Toan"], data["Van"])
                if data["Toan"] != 0 and data["Van"] != 0:
                    break
        if data["XepLoai"] == "Kem":
            list_result.append(data)
    mylist = sorted(list_result, key=lambda k: (k['MaTruong'].lower(), k['Ten'].lower(), k['Ho'].lower()))
    header = "SBD,  Ho, Ten,  Phai, NgaySinh, Toan,  Van, TongDiem, XepLoai, MaTruong"
    file_name = "item7.txt"
    write_to_file(file_name, mylist, header)
    return file_name

def view_item8():
    ''' truy xuất theo yêu cầu số 8. 
        Kết quả file: item8.txt
    '''
    danh_sach = view_ds()
    diem = view_diem()
    list_result = []
    #Tao set data type để chứa các mã trường không trùng lặp trong db
    schoolSet = set()
    for ds in danh_sach:
        data = {}
        data["SDB"] = ds[0]
        data["Ho"] = ds[1]
        data["Ten"] = ds[2]
        data["Phai"] = ds[3]
        data["NgaySinh"] = ds[4]
        data["Toan"] = 0
        data["Van"] = 0
        data["TongDiem"] = 0
        data["XepLoai"] = None
        data["MaTruong"] = ds[5]
        schoolSet.add(ds[5])
        for d in diem:
            if data["SDB"] == d[0]:
                if d[1].strip()=="Toan":
                    data["Toan"] = float(d[2])
                if d[1].strip()=="Van":
                    data["Van"] = float(d[2])
                data["TongDiem"] = data["Toan"] + data["Van"]
                data["XepLoai"] = get_xeploai(data["Toan"], data["Van"])
                if data["Toan"] != 0 and data["Van"] != 0:
                    break
        list_result.append(data)

    list_mark = []
    for i in schoolSet:
        list_new = []
        for data in list_result:
            if data["MaTruong"] == i:
                list_new.append(data)
                list_result.remove(data)
        max = int(list_new[0]["TongDiem"])
        i = 0
        for addr in range(len(list_new)):
            if int(list_new[addr]["TongDiem"]) > max:
                max = int(list_new[addr]["TongDiem"])
                i = addr
        list_mark.append(list_new[i])    
    mylist = sorted(list_mark, key=lambda k: (k['MaTruong'].lower(), k['Ten'].lower(), k['Ho'].lower()))
    header = "SBD,  Ho, Ten,  Phai, NgaySinh, Toan,  Van, TongDiem, XepLoai, MaTruong"
    file_name = "item8.txt"
    write_to_file(file_name, mylist, header)
    return file_name

def view_item9(nameSchool):
    ''' view function to show the content of the database
        returns the content of the database with filter.
    '''
    danh_sach = view_ds()
    diem = view_diem()
    # print( danh_sach[].count("TV  "))
    # danh_sach = execute_sql("select * from DanhSach where trim(MaTruong) = '%s'" % (nameSchool,))
    # diem = execute_sql("select * from Diem")

    list_result = []
    for ds in danh_sach:
        if ds[5].strip() == nameSchool.strip():
            data = {}
            data["SBD"] = ds[0]
            data["Ho"] = ds[1]
            data["Ten"] = ds[2]
            data["Phai"] = ds[3]
            data["NgaySinh"] = ds[4]
            data["Toan"] = 0
            data["Van"] = 0
            data["TongDiem"] = 0
            data["DTN"] = 0
            data["XepLoai"] = None
            data["MaTruong"] = ds[5]
            for d in diem:
                if data["SBD"] == d[0]:
                    if d[1].strip()=="Toan":
                        data["Toan"] = float(d[2])
                    if d[1].strip()=="Van":
                        data["Van"] = float(d[2])
                    if data["Toan"] != 0 and data["Van"] != 0:
                        data["TongDiem"] = data["Toan"] + data["Van"]
                        data["DTN"] = min(data["Toan"],data["Van"])
                        data["XepLoai"] = get_xeploai(data["Toan"], data["Van"])
                        break
        # if data["MaTruong"].strip() == nameSchool.strip():
            list_result.append(data)
    mylist = sorted(list_result, key=lambda k: (k['MaTruong'].lower(), k['Ten'].lower(), k['Ho'].lower()))
    #print(mylist)
    header = "SBD,  Ho, Ten,  Phai, NgaySinh, Toan,  Van, TongDiem, DTN, XepLoai, MaTruong"
    file_name = "item9.txt"
    write_to_file(file_name, mylist, header)
    return file_name

def view_item10():
    ''' truy xuất theo yêu cầu số 10.
        lấy random 3 học sinh từ DanhSach 
        Kết quả file: item5.txt
    '''

    danh_sach = view_ds()
    diem = view_diem()

    num_to_select = 3 # set the number to select here.
    list_of_random_items = random.sample(danh_sach, num_to_select)
    #print(list_of_random_items)
    list_result = []
    for ds in list_of_random_items:
        data = {}
        # print(ds[3])
        data["SDB"] = ds[0]
        # data["Ho"] = ds[1]
        # data["Ten"] = ds[2]
        data["HoTen"] = ds[1].strip() + ' ' + ds[2].strip()
        #data["Phai"] = ds[3]
        #data["NgaySinh"] = ds[4]
        data["Toan"] = 0
        data["Van"] = 0
        data["TongDiem"] = 0
        #data["DTN"] = 0
        data["XepLoai"] = None
        #data["MaTruong"] = ds[5]
        for d in diem:
            # print(d)
            if data["SDB"] == d[0]:
                if d[1].strip()=="Toan":
                    data["Toan"] = float(d[2])
                if d[1].strip()=="Van":
                    data["Van"] = float(d[2])
                data["TongDiem"] = data["Toan"] + data["Van"]
                #data["DTN"] = min(data["Toan"],data["Van"])
                data["XepLoai"] = get_xeploai(data["Toan"], data["Van"])
        
        # Convert data cho dễ đọc
        data["SDB"] = "So Bao Danh: " + data["SDB"]
        data["HoTen"] = "Anh: " + data["HoTen"] if ds[3] is '0' else "Chi: " + data["HoTen"]
        data["Toan"] = "Diem Toan: " + str(data["Toan"])
        data["Van"] = "Diem Van: " + str(data["Van"])
        data["TongDiem"] = "TongDiem: " + str(data["TongDiem"])
        data["XepLoai"] = "Xep Loai: " + str(data["XepLoai"])
        
        list_result.append(data)
    #mylist = sorted(list_result, key=lambda k: (k['MaTruong'].lower(), k['Ten'].lower(), k['Ho'].lower()))
    mylist = list_result
    file_name = "item10.txt"
    write_to_file_no_h(file_name, mylist)
    return file_name

#xuất ra file txt khong cần header
def write_to_file_no_h(filename, a_list):
    textfile = open(filename, "w")
    for element in a_list:
        line = ""
        for key,value in element.items():
            line += str(value) + ","
        textfile.write(line + "\n")
    textfile.close()

#xuất ra file txt có header
def write_to_file(filename, a_list, header):
    textfile = open(filename, "w")
    textfile.write(header + "\n")
    for element in a_list:
        line = ""
        for key,value in element.items():
            line += str(value) + ","
        textfile.write(line + "\n")
    textfile.close()

# tính xep loại
def get_xeploai(toan, van):
    xeploai = ""
    if (toan + van) >=16 and toan >=7 and van >=7:
        xeploai = "Gioi"
    elif (toan + van) >=14 and toan >=6 and van >=6:
        xeploai = "Kha"
    elif (toan + van) >=10 and toan >=4 and van >=4:
        xeploai = "Trung Binh"
    else:
        xeploai = "Kem"
    return xeploai

# đọc nội dung file txt
def read_file_data(file_name):
    #Read file and add all line to a list variable
    with open(file_name, 'r')as f:
        a = f.readlines()
    lst = []
    for i in a:
        # new = i
        # print(i)
        lst.append(i.replace(',0,',',Nam,').replace(',1,',',Nu,').replace("\n",""))
    return lst

def delete_file(filePath):
    if os.path.exists(filePath):
        os.remove("demofile.txt")
    else:
        # print("The file does not exists")
        return
    
def write_file_csv(filePath,aList):
    with open(filePath,"w",newline = '') as f:
        writer = csv.writer(f)
        for i in aList:
            writer.writerow(i)
        f.close()
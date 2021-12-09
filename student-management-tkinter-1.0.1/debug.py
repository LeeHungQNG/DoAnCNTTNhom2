# print("{:<15s}  {:>5s}  {:<25s}  {:<5s}".format("Name","id","Nationality","Qual"))
# heads = ["Name","id","Nationality","Qual"]
fixedlen = 12
# print(("{:<4s}"+(fixedlen-len(heads[0]))*" " +"{:>5s}"+(fixedlen-len(heads[1]))*" " +"{:<25s}"+(fixedlen-len(heads[2]))*" " +"{:<5s}").format(heads[0],heads[1],heads[2],heads[3]))
# print(("{:<25s}"+(fixedlen-len(heads[2]))*".").format(heads[2]))

# print(("{:<4s}" + 5*".").format("a"))
# #rint("{:4s}".format(9))

def ia():
        margin =" "
        print(("{:<3s}"+(fixedlen-len(heads[0]))*margin \
        + "{:<2s}"+(15-len(heads[1]))*margin \
        + "{:<2s}"+(fixedlen-len(heads[2]))*margin \
        + "{:<1s}"+(fixedlen-len(heads[3]))*margin \
        + "{:<3s}"+(15-len(heads[4]))*margin \
        + "{:<1s}"+(fixedlen-len(heads[5]))*margin \
        + "{:<1s}"+(fixedlen-len(heads[6]))*margin \
        + "{:<1s}"+(fixedlen-len(heads[7]))*margin \
        + "{:<1s}"+(fixedlen-len(heads[8]))*margin \
        + "{:<3s}"+(fixedlen-len(heads[9]))*margin \
        + "{:<5s}").format(heads[0],heads[1],heads[2],heads[3], heads[4], heads[5], heads[6], heads[7], heads[8], heads[9], heads[10]) )

heads = ["SBD",  "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "TongDiem", "DTN", "XepLoai", "MaTruong"]
ia()
heads = ['00013', 'PK', 'Hongc', '0', '04/04/1983', '0', '0', '0', '0', 'None', '', '']
ia()
heads = ['00013', 'PK', 'Hongc1', '0', '04/04/1983', '0', '0', '0', '0', 'None', '', '']
ia()
heads = ['0210', 'Huynh Thi', 'Cua', '1', '02/09/1983', '10.0', '10.0', '20.0', '10.0', 'Gioi', 'BTX', '']
ia()
heads = ['0694', 'Nguyen Hoang', 'Dam', '0', '26/11/1982', '7.5', '8.5', '16.0', '7.5', 'Gioi', 'BTX', '']
ia()
heads = ['0204', 'Huynh Thanh', 'Danh', '0', '07/12/1982', '7.5', '4.5', '12.0', '4.5', 'Trung Binh', 'BTX', '']
ia()
heads = ['0217', 'Pham Thi', 'Dao', '1', '08/12/1983', '7.5', '8.5', '16.0', '7.5', 'Gioi', 'BTX', '']
ia()
heads = ['0211', 'Nguyen Minh', 'Hanh', '0', '15/11/1983', '6.0', '9.0', '15.0', '6.0', 'Kha', 'BTX', '']
ia()
heads = ['0706', 'Nguyen Thi', 'Hoa', '1', '28/11/1983', '6.5', '6.5', '13.0', '6.5', 'Trung Binh', 'BTX', '']
ia()
heads = ['0754', 'Pham Van', 'Hoang', '0', '27/10/1984', '9.5', '6.0', '15.5', '6.0', 'Kha', 'BTX', '']
ia()
heads = ['0688', 'Quach Thanh', 'Hong', '0', '24/06/1983', '9.0', '9.0', '18.0', '9.0', 'Gioi', 'BTX', '']
ia()
heads = ['0683', 'Le Thanh', 'Khoa', '0', '28/07/1983', '6.5', '8.0', '14.5', '6.5', 'Kha', 'BTX', '']
ia()
heads = ['0743', 'Huynh Phan', 'Khoi', '0', '22/05/1983', '5.5', '5.0', '10.5', '5.0', 'Trung Binh', 'BTX', '']
ia()
heads = ['0209', 'Tran Thi', 'Loan', '1', '25/11/1983', '4.5', '4.0', '8.5', '4.0', 'Kem', 'BTX', '']
ia()
heads = ['0718', 'Dinh Hai', 'Nam', '0', '25/12/1982', '6.0', '9.5', '15.5', '6.0', 'Kha', 'BTX', '']
ia()
heads = ['0736', 'Do Phuong', 'Nam', '0', '01/01/1984', '8.5', '5.0', '13.5', '5.0', 'Trung Binh', 'BTX', '']
ia()
heads = ['0215', 'Tran Thi', 'Nhi', '1', '18/11/1984', '5.5', '7.0', '12.5', '5.5', 'Trung Binh', 'BTX', '']
ia()
heads = ['0755', 'Nguyen Thi', 'Nhung', '1', '31/10/1983', '6.0', '8.5', '14.5', '6.0', 'Kha', 'BTX', '']
ia()
heads = ['0725', 'Huynh Van', 'On', '0', '16/04/1984', '6.5', '7.5', '14.0', '6.5', 'Kha', 'BTX', '']
ia()
heads = ['0682', 'Dang Minh', 'Quan', '0', '17/02/1984', '10.0', '10.0', '20.0', '10.0', 'Gioi', 'BTX', '']
ia()
heads = ['0696', 'Nguyen Van', 'Son', '0', '12/09/1983', '8.0', '6.0', '14.0', '6.0', 'Kha', 'BTX', '']
ia()
heads = ['0689', 'Nguyen Tan', 'Tai', '0', '22/08/1983', '8.5', '9.0', '17.5', '8.5', 'Gioi', 'BTX', '']
ia()
heads = ['0198', 'Truong Minh', 'Thang', '0', '26/02/1984', '4.5', '5.5', '10.0', '4.5', 'Trung Binh', 'BTX', '']
ia()
heads = ['0713', 'Bui Van', 'Thanh', '0', '12/08/1984', '8.5', '9.5', '18.0', '8.5', 'Gioi', 'BTX', '']
ia()
heads = ['0712', 'Nguyen Van', 'Thanh', '0', '13/11/1983', '8.0', '9.0', '17.0', '8.0', 'Gioi', 'BTX', '']
ia()
heads = ['0203', 'Le Kim', 'Thoa', '1', '01/04/1984', '6.5', '9.0', '15.5', '6.5', 'Kha', 'BTX', '']
ia()
heads = ['0719', 'Pham Thi', 'Thom', '1', '02/07/1984', '6.5', '5.0', '11.5', '5.0', 'Trung Binh', 'BTX', '']
ia()
heads = ['0695', 'Do Thi', 'Thuy', '1', '17/08/1984', '9.0', '5.0', '14.0', '5.0', 'Trung Binh', 'BTX', '']
ia()
heads = ['0441', 'Tran Kieu', 'Au', '0', '22/12/1982', '7.5', '6.0', '13.5', '6.0', 'Trung Binh', 'LHP', '']
ia()
heads = ['0043', 'Pham Hoai', 'Bong', '0', '11/10/1982', '9.0', '8.0', '17.0', '8.0', 'Gioi', 'LHP', '']
ia()
heads = ['0026', 'Doan Duc', 'Chi', '0', '25/10/1983', '4.0', '6.0', '10.0', '4.0', 'Trung Binh', 'LHP', '']
ia()
heads = ['0382', 'Tran Thuy', 'Dao', '1', '17/11/1983', '6.5', '8.5', '15.0', '6.5', 'Kha', 'LHP', '']
ia()
heads = ['0411', 'Nguyen Van', 'Dung', '0', '17/12/1983', '5.5', '5.0', '10.5', '5.0', 'Trung Binh', 'LHP', '']
ia()
heads = ['0412', 'Vo Thanh', 'Giang', '0', '10/07/1984', '8.5', '7.5', '16.0', '7.5', 'Gioi', 'LHP', '']
ia()
heads = ['0001', 'Nguyen Viet', 'Hong', '0', '04/04/1983', '0', '0', '0', '0', 'None', 'LHP', '']
ia()
heads = ['0014', 'Trang Phi', 'Hung', '0', '02/11/1984', '8.5', '6.0', '14.5', '6.0', 'Kha', 'LHP', '']
ia()
heads = ['0037', 'Tran', 'Khiem', '0', '04/12/1983', '7.0', '6.5', '13.5', '6.5', 'Trung Binh', 'LHP', '']
ia()


# # query = ("select SBD, Ho, Ten, Phai, NgaySinh, Diem as Toan, MaTruong from ("
# #             "SELECT ds.MaHS as SBD, ds.Ho, ds.Ten, ds.Phai, ds.NgaySinh, di.Mon, di.Diem, ds.MaTruong"
# #             "from DanhSach ds, Diem di"
# #             "where 1=1"
# #             "and ds.MaHS = di.MaHS"
# #             "and trim(di.Mon) = '%s')" % ("Toan",)
# #             )
# # print(query)

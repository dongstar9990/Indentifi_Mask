 
class QuanLySinhVien:
    listSinhVien = []
 
   
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
 
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
 
    def nhapSinhVien(self):
       
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        age = int(input("Nhap tuoi sinh vien: "))
        diemToan = float(input("Nhap diem toan: "))
        diemLy = float(input("Nhap diem Ly: "))
        diemHoa = float(input("Nhap diem Hoa: "))
        sv = SinhVien(svId, name, sex, age, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
 
    def updateSinhVien(self, ID):
       
        sv:SinhVien = self.findByID(ID)
       
        if (sv != None):
          
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            age = int(input("Nhap tuoi sinh vien: "))
            diemToan = float(input("Nhap diem toan: "))
            diemLy = float(input("Nhap diem Ly: "))
            diemHoa = float(input("Nhap diem Hoa: "))
       
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))
 
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
 
   
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
 
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
 
  
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
 
   
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
 
  
    def deleteById(self, ID):
        isDeleted = False
       
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
 
    
    def tinhDTB(self, sv:SinhVien):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
       
        sv._diemTB = math.ceil(diemTB * 100) / 100
 
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"
 
    
    def showSinhVien(self, listSV):
       
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                              sv._diemHoa,sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien

    from main.QuanLySinhVien import QuanLySinhVien
 
qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN C#")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **")
    print("**  6. Sap xep sinh vien theo ten.                   **")
    print("**  7. Sap xep sinh vien theo ID.                    **")
    print("**  8. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")
     
    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co id = ", ID, " da bi xoa.")
            else:
                print("\nSinh vien co id = ", ID ," khong ton tai.")
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ID.")
            qlsv.sortByID()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 8):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")


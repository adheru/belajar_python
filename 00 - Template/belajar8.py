import csv
import os 
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kembali():
    print("\n")
    input("Press any to continue...")
    clear_screen()

def menu_awal():
    while(True):
        print("        Unas Library           ")
        print("------------------------------------------------------")
        print(" [1] Show Book List")
        print(" [2] Book borrowed")
        print(" [3] Return book")  
        print(" [4] Input Book")
        print(" [5] Exit") 
        try:
            a=int(input("Select menu 1-5: "))
            print()
            if(a==1):
                displaybook()
                kembali()
            elif(a==2):
                listSplit()
                borow_book()
                kembali()
            elif(a==3):
                listSplit()
                kembalikan_buku()
                kembali()
            elif(a==4):
                listSplit()
                tambah_buku()
                kembali()
            elif(a==5):
                print("Thankyou~")
                break
            else:
                print("Select menu 1-5")
                kembali()
                continue
        except ValueError:
            print("Enter according to instructions !")
            kembali()
            continue

def listSplit():
    global book_title
    global book_author
    global book_stock
    global book_price
    book_title=[]
    book_author=[]
    book_stock=[]
    book_price=[]
    with open("belajar8_data.txt","r+") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    book_title.append(a)
                elif(ind==1):
                    book_author.append(a)
                elif(ind==2):
                    book_stock.append(a)
                elif(ind==3):
                    book_price.append(a.strip("Rp"))
                ind+=1

def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())

def displaybook():
    with open("belajar8_data.txt","r+") as f:
        lines=f.read()
        print(lines)
        print ()

def tambah_buku():
    with open("belajar8_data.txt", "a+") as f:
        title = input("Book Title = ")
        book_author = input("book_author = ")
        stok = input("stok = ")
        book_price = input("book_price = Rp ")   
        pembatas = ","
        f.write('\n' + title + pembatas + book_author + pembatas + stok + pembatas + 'Rp' + book_price)

def borow_book():
    success=False
    while(True):
        firstName=input("Masukkan nama depan peminjam: ")
        if firstName.isalpha():
            break
        print("Masukkan huruf A-Z")
    while(True):
        lastName=input("Masukkan nama belakang peminjam: ")
        if lastName.isalpha():
            break
        print("Masukkan huruf A-Z")
        print("")
    displaybook()
            
    t="Pinjaman-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("               Perpustakaan HMTI  \n")
        f.write("                   Dipinjam oleh: "+ firstName+" "+lastName+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N. \t\t title buku \t      book_author \n" )

    while success==False:
        print("Pilih menu di bawah ini :")
        for i in range(len(book_title)):
            print("Masukkan", i, "untuk meminjam buku", book_title[i])
    
        try:   
            a=int(input())
            try:
                if(int(book_stock[a])>0):
                    print("Buku Tersedia")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ book_title[a]+"\t\t  "+book_author[a]+"\n")

                    book_stock[a]=int(book_stock[a])-1
                    with open("belajar8_data.txt","r+") as f:
                        for i in range(8):
                            f.write(book_title[i]+","+book_author[i]+","+str(book_stock[i])+","+"Rp"+book_price[i]+"\n")
                            continue

                    #jika buku yang dipinjam lebih dari 1
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Apakah ingin pinjam buku lagi ? Masukkan y jika ya dan n jika tidak."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Pilih menu di bawah ini :")
                            for i in range(len(book_title)):
                                print("Masukkan", i, "untuk meminjam buku", book_title[i])
                            a=int(input())
                            if(int(book_stock[a])>0):
                                print("Buku tersedia")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ book_title[a]+"\t\t  "+book_author[a]+"\n")

                                book_stock[a]=int(book_stock[a])-1
                                with open("belajar8_data.txt","r+") as f:
                                    for i in range(8):
                                        f.write(book_title[i]+","+book_author[i]+","+str(book_stock[i])+","+"Rp"+book_price[i]+"\n")
                                        success=False
                                        continue
                            else:
                                loop=False
                                continue
                        elif (choice.upper()=="N"):
                            print ("Terimakasih telah meminjam buku. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Masukkan sesuai petunjuk !")
                        
                else:
                    print("Buku tidak tersedia")
                    borow_book()
                    success=False
                    continue
            except IndexError:
                print("")
                print("Pilih buku sesuai nomor.")
        except ValueError:
            print("")
            print("Pilih sesuai petunjuk !.")

def kembalikan_buku():
    name=input("Masukkan nama peminjam: ")
    a="Pinjaman-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("Rp") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("Nama peminjam salah")
        kembalikan_buku()

    b="Pengembalian-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Perpustakaan HMTI \n")
        f.write("                   Dikembalikan oleh: "+ name+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N.\t\ttitle Buku\t\tTotal\n")


    total=0.0
    for i in range(8):
        if book_title[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+book_title[i]+"\t\tRp"+book_price[i]+"\n")
                book_stock[i]=int(book_stock[i])+1
            total+=float(book_price[i])
            
    print("\t\t\t\t\t\t\t"+"Rp"+str(total))
    print("Apakah buku melewati batas peminjaman?")
    print("Masukkan Y jika ya dan N jika tidak")
    stat=input()
    if(stat.upper()=="Y"):
        print("Berapa hari keterlambatan?")
        hari=int(input())
        denda=3000*hari
        with open(b,"a+")as f:
            f.write("\t\t\t\t\tDenda: Rp"+ str(denda)+"\n")
        total=total+denda
    
    print("Total pembayaran: "+ "Rp"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: Rp"+ str(total))
    
        
    with open("belajar8_data.txt","r+") as f:
            for i in range(8):
                f.write(book_title[i]+","+book_author[i]+","+str(book_stock[i])+","+"Rp"+book_price[i]+"\n")



menu_awal()
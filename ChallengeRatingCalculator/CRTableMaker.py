import sqlite3

db = sqlite3.connect("CRTable.sqlite")
db.execute("create table if not exists CRTable(CR real, profBonus integer, AC integer, HitPointMin integer, HitPointMax integer, ATKbonu integer, AvgDmgMin integer, AvgDmgMax integer, SaveDC integer)")
db.execute("delete from CRTable")
db.execute("insert into CRTable values(0, 2, 13, 1, 6, 3, 0, 1, 13)")
db.execute("insert into CRTable values(0.125, 2, 13, 7, 35, 3, 2, 3, 13)")
db.execute("insert into CRTable values(0.25, 2, 13, 36, 49, 3, 4, 5, 13)")
db.execute("insert into CRTable values(0.5, 2, 13, 50, 70, 3, 6, 8, 13)")
db.execute("insert into CRTable values(1, 2, 13, 71, 85, 3, 9, 14, 13)")
db.execute("insert into CRTable values(2, 2, 13, 86, 100, 3, 15, 20, 13)")
db.execute("insert into CRTable values(3, 2, 13, 101, 115, 4, 21, 26, 13)")
db.execute("insert into CRTable values(4, 2, 14, 116, 130, 5, 27, 32, 14)")
db.execute("insert into CRTable values(5, 3, 15, 131, 145, 6, 33, 38, 15)")
db.execute("insert into CRTable values(6, 3, 15, 146, 160, 6, 39, 44, 15)")
db.execute("insert into CRTable values(7, 3, 15, 161, 175, 6, 45, 50, 15)")
db.execute("insert into CRTable values(8, 3, 16, 176, 190, 7, 51, 56, 16)")
db.execute("insert into CRTable values(9, 4, 16, 191, 205, 7, 57, 62, 16)")
db.execute("insert into CRTable values(10, 4, 17, 206, 220, 7, 63, 68, 16)")
db.execute("insert into CRTable values(11, 4, 17, 221, 235, 8, 69, 74, 17)")
db.execute("insert into CRTable values(12, 4, 17, 236, 250, 8, 75, 80, 17)")
db.execute("insert into CRTable values(13, 5, 18, 251, 265, 8, 81, 86, 18)")
db.execute("insert into CRTable values(14, 5, 18, 266, 280, 8, 87, 92, 18)")
db.execute("insert into CRTable values(15, 5, 18, 281, 295, 8, 93, 98, 18)")
db.execute("insert into CRTable values(16, 5, 18, 296, 310, 9, 99, 104, 18)")
db.execute("insert into CRTable values(17, 6, 19, 311, 325, 10, 105, 110, 19)")
db.execute("insert into CRTable values(18, 6, 19, 326, 340, 10, 111, 116, 19)")
db.execute("insert into CRTable values(19, 6, 19, 341, 355, 10, 117, 122, 19)")
db.execute("insert into CRTable values(20, 6, 19, 356, 400, 10, 123, 140, 19)")
db.execute("insert into CRTable values(21, 7, 19, 401, 445, 11, 141, 158, 20)")
db.execute("insert into CRTable values(22, 7, 19, 446, 490, 11, 159, 176, 20)")
db.execute("insert into CRTable values(23, 7, 19, 491, 535, 11, 177, 194, 20)")
db.execute("insert into CRTable values(24, 7, 19, 536, 580, 12, 195, 212, 21)")
db.execute("insert into CRTable values(25, 8, 19, 581, 625, 12, 213, 230, 21)")
db.execute("insert into CRTable values(26, 8, 19, 626, 670, 12, 231, 248, 21)")
db.execute("insert into CRTable values(27, 8, 19, 671, 715, 13, 249, 266, 22)")
db.execute("insert into CRTable values(28, 8, 19, 716, 760, 13, 267, 284, 22)")
db.execute("insert into CRTable values(29, 9, 19, 761, 805, 13, 285, 302, 22)")
db.execute("insert into CRTable values(30, 9, 19, 806, 850, 14, 303, 320, 23)")


cursor = db.cursor()
cursor.execute("select * from CRTable")
#for x in cursor:
#    print(x)
cursor.close()
db.commit()
db.close()
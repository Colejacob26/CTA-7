
dict1 = {"CSC101":3004, "CSC102":4501, "CSC103":6755, "NET110": 1244, "COM241":1411}
dict2 = {"CSC101":"Haynes", "CSC102":"Alvarado", "CSC103":"Rich", "NET110": "Burke", "COM241":"Lee"}
dict3 = {"CSC101":"8:00 a.m.", "CSC102":"9:00 a.m.", "CSC103":"10:00 a.m.", "NET110": "11:00 a.m.", "COM241":"1:00 p.m."}


print("Please enter course number:")
c_number = str(input())


print("Room Number:", dict1[c_number], "\n" "Instructor:", dict2[c_number],"\n" "Meeting time:", dict3[c_number])

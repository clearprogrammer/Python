#Logical operators
two_wheeler_license = False
four_wheeler_license = False
heavy_wheeler_license = False

if two_wheeler_license and not four_wheeler_license and not heavy_wheeler_license:
    print ("Only eligible to ride two wheeler license")

elif two_wheeler_license and four_wheeler_license and heavy_wheeler_license:
    print ("Eligible to ride all 2, 4 wheelers & heavy wheeler")

elif not two_wheeler_license:
    print ("no 2 wheeler license")


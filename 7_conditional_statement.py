#conditional statements
#if , elif, else

is_spicy = False
is_sweet = True

if is_spicy:
    print("cancel the order. Or request to modify")
    print("Continue eating only if you are comfortable with spicy")
elif is_sweet:
    print ("warning for diabetic patients")
    print ("Continue only if you would work out after eating")
else:
    print ("Don't cancel. Keep eating")
    print ("Can't find better food than this")
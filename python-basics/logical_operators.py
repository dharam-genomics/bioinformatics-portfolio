depth = 90
coverage = 100
vaf = 0.80
if(depth >= 80 and coverage >= 90 and vaf >= .7):
    print("Varaiant can be reported")
else:
    print("discard variant")
if(depth >= 92 and coverage >= 90 and vaf >= .7):
    print("Report the Variant!")
elif(depth >= 92 or coverage >= 110 or vaf >= .9):
    print("elif block! Variant can be reported")
else:
    print("Not report it")


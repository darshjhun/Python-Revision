fh=input("give me your name:")
smart_boys = ['darsh', 'Darsh','chandan','Chandan']
smart_girl = ['ruby','Ruby','priya', 'Priya', 'tithi','Tithi']
if fh in smart_boys:
    print("%s is handsome" % fh )
    print("%s is smart" % fh )
elif fh in smart_girl:
    print("%s is pretty" % fh )
    print("%s is smart" % fh )
else:
    print("%s is a fool" % fh)

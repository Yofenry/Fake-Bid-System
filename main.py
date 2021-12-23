import webbrowser
import random
LIST=["PS5","Nintendo Switch(LCD)","Xbox Series X","High End Gaming PC"]
a=random.randint(0,3)
ef = LIST[a]
print("Your Gaming Device Is: " + ef)
if ef == "PS5":
    nonuserbid = random.randint(750,1000)
    userbid = int(input("What Is Your Bid: "))
    if userbid > nonuserbid:
        nonuserbidstr = str(nonuserbid)
        input("Congrats You Won, Click Enter To Claim Your Image The Other Bid Was " + nonuserbidstr)
        webbrowser.open('https://608111-1969675-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2020/06/PS5_DIGITALEDITION_RENDER_WITHNOTICE_03.jpg')
    else:
        nonuserbidstr = str(nonuserbid)
        input("Sorry You Lost, The Other Bid Was " + nonuserbidstr)
elif ef == "Nintendo Switch(LCD)":
    nonuserbid = random.randint(300,450)
    userbid = int(input("What Is Your Bid: "))
    if userbid > nonuserbid:
        nonuserbidstr = str(nonuserbid)
        input("Congrats You Won, Click Enter To Claim Your Image The Other Bid Was " + nonuserbidstr)
        webbrowser.open('https://assets.nintendo.com/image/upload/b_white,c_pad,f_auto,h_382,q_auto,w_573/ncom/en_US/hardware/switch/nintendo-switch-new-package/gallery/image03?v=2021122218')
    else:
        nonuserbidstr = str(nonuserbid)
        input("Sorry You Lost, The Other Bid Was " + nonuserbidstr)
elif ef == "Xbox Series X":
    nonuserbid = random.randint(750, 1000)
    userbid = int(input("What Is Your Bid: "))
    if userbid > nonuserbid:
        nonuserbidstr = str(nonuserbid)
        input("Congrats You Won, Click Enter To Claim Your Image The Other Bid Was " + nonuserbidstr)
        webbrowser.open('https://compass-ssl.xbox.com/assets/b9/0a/b90ad58f-9950-44a7-87fa-1ee8f0b6a90e.jpg?n=XSX_Page-Hero-0_768x792.jpg')
    else:
        nonuserbidstr = str(nonuserbid)
        input("Sorry You Lost, The Other Bid Was " + nonuserbidstr)
elif ef == "High End Gaming PC":
    nonuserbid = random.randint(1000, 5000)
    userbid = int(input("What Is Your Bid: "))
    if userbid > nonuserbid:
        nonuserbidstr = str(nonuserbid)
        input("Congrats You Won, Click Enter To Claim Your Image The Other Bid Was " + nonuserbidstr)
        webbrowser.open('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4YhgE934J5Dr-Oxet5zalUBSteDMKfUfMPItamtk8-x_LiFLbmSyjp_O_z9bz-XmUmfo&usqp=CAU')
    else:
        nonuserbidstr = str(nonuserbid)
        input("Sorry You Lost, The Other Bid Was " + nonuserbidstr)
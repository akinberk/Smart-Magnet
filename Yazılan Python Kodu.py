import tkinter as tk
from selenium import webdriver
import time
from PIL import ImageTk,Image
import urllib.request
import ssl
from tkinter import messagebox
from itertools import cycle
import base64
from pyvirtualdisplay import Display


ssl._create_default_https_context = ssl._create_unverified_context

main = tk.Tk()
main.geometry("480x290")
main.title("SmartMagnet")
main.configure(background='white')
bilgigiris = tk.Tk()
bilgigiris.geometry("480x290")
bilgigiris.title("Bilgilerinizi Doldurun")
bilgigiris.withdraw()
twittergui=tk.Tk()
twittergui.geometry('480x290')
twittergui.title('Twitter')
twittergui.configure(background='#1da1f2')
twittergui.withdraw()
twitterguiref=tk.Tk()
twitterguiref.geometry('480x290')
twitterguiref.title('Twitter')
twitterguiref.configure(background='#1da1f2')
twitterguiref.withdraw()
instagramgui=tk.Tk()
instagramgui.geometry('480x290')
instagramgui.title('İnstagram')
instagramgui.configure(background='black')
instagramgui.withdraw()
instagramyukgui=tk.Tk()
instagramyukgui.geometry('480x290')
instagramyukgui.title('İnstagram')
instagramyukgui.configure(background='#DD2A7B')
instagramyukgui.withdraw()
instagramguiref=tk.Tk()
instagramguiref.geometry('480x290')
instagramguiref.title('İnstagram')
instagramguiref.configure(background='#DD2A7B')
instagramguiref.withdraw()
ekrangui=tk.Tk()
ekrangui.geometry('480x290')
ekrangui.title('Manzara')
ekrangui.configure(background='Black')  
ekrangui.update()
ekrangui.withdraw()
manzaragui=tk.Tk()
manzaragui.geometry('480x290')
manzaragui.title('Manzara')
manzaragui.configure(background='Black')  
manzaragui.update()
manzaragui.withdraw()
ailegui=tk.Tk()
ailegui.geometry('480x290')
ailegui.title('Aile')
ailegui.configure(background='Black')  
ailegui.update()
ailegui.withdraw()
aramagui=tk.Tk()
aramagui.geometry('480x290')
aramagui.title('Arama')
aramagui.configure(background='Black')
aramagui.withdraw()
fgöstergui=tk.Tk()
fgöstergui.geometry('480x290')
fgöstergui.title('Arama')
fgöstergui.configure(background='Black')  
fgöstergui.withdraw()
fgösteryukgui=tk.Tk()
fgösteryukgui.geometry('480x290')
fgösteryukgui.title('Arama')
fgösteryukgui.configure(background='Black')  
fgösteryukgui.withdraw()
display = Display(visible=0, size=(1000,1000))
display.start()
browser=webdriver.Firefox()
browser.get("https://www.google.com.tr/search?safe=strict&q=hava+durumu&spell=1&sa=X&ved=0ahUKEwjs1fys-KDiAhUZ6KYKHdWNCy0QBQgqKAA&biw=1146&bih=875")
time.sleep(3)
adresssel = browser.find_element_by_css_selector(".ts > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > h3:nth-child(1) > b:nth-child(1)")
adress = adresssel.text
sıcaklık = browser.find_element_by_css_selector(".ts > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
sıcaklıktk = sıcaklık.text
havadurumuimg = browser.find_elements_by_css_selector('.ts > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(2) > div:nth-child(1) > img:nth-child(2)')


for span in havadurumuimg:
    src = havadurumuimg[0].get_attribute('src')
    urllib.request.urlretrieve(src,('hava.png'))

def tick():  
    time2 = time.strftime('%H:%M:%S')  
    saat.config(text=time2)
    saat.after(200, tick)

def infologin():
    main.withdraw()
    bilgigiris.deiconify()

    igidtxt = tk.Label(bilgigiris, text="Instagram Id:  ", font=("Helvitca", 25))
    igpasstxt = tk.Label(bilgigiris, text="Instagram Pass:", font=("Helvitca", 25))
    twidtxt = tk.Label(bilgigiris, text="Twitter Id:  ", font=("Helvitca", 25))
    twpasstxt = tk.Label(bilgigiris, text="Twitter Pass:", font=("Helvitca", 25))

    igidtxt.grid(row=0, column=0,sticky='w')
    igpasstxt.grid(row=1, column=0,sticky='w')
    twidtxt.grid(row=2, column=0,sticky='w')
    twpasstxt.grid(row=3, column=0,sticky='w')

    igidentry = tk.Entry(bilgigiris)
    igpassentry = tk.Entry(bilgigiris)
    twidentry = tk.Entry(bilgigiris)
    twpassentry = tk.Entry(bilgigiris)

    igidentry.grid(row=0, column=1)
    igpassentry.grid(row=1, column=1)
    twidentry.grid(row=2, column=1)
    twpassentry.grid(row=3, column=1)

    def kaydet():
        global twid
        global twpass
        global igid
        global igpass
        igid = igidentry.get()
        igpass = igpassentry.get()
        twid = twidentry.get()
        twpass = twpassentry.get()
        bilgigiris.destroy()
        main.deiconify()
    def geri():
        bilgigiris.withdraw()
        main.deiconify()
    
    log = tk.Button(bilgigiris, text ="LOGIN",font=('times',25), fg = "black", command = kaydet)
    log.grid(row=4, column=1)
    geriinfo = tk.Button(bilgigiris, text ="Geri",font=('times',25), fg = "black", command = geri )
    geriinfo.grid(row=5, column=1)
    
    
def twitter():
    if twid=='' or twpass=='':
        messagebox.showerror("HATA","Lütfen Kullanıcı adı ve Şifre Giriniz:")

    elif twid !='' and twpass !='':
        main.withdraw()
        twittergui.deiconify()
        twitterload=tk.Label(twittergui,text='YÜKLENİYOR....',font=('Helvitca',50),fg='#1da1f2',bg='white')
        twitterload.grid(row=0,column=0,pady=215)    
        twittergui.update()
        global twitterkontrol
        browser.get("https://twitter.com/login")

        time.sleep(5)
        twitterid = browser.find_element_by_css_selector(".js-username-field")
        time.sleep(1)
        twitterpassword = browser.find_element_by_css_selector(".js-password-field")

        twitterid.send_keys(twid)
        twitterpassword.send_keys(twpass)
        time.sleep(2)

        girisyap=browser.find_element_by_css_selector("button.submit")
        girisyap.click()
        time.sleep(8)

        tweet=browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")        
        tweetsahip=browser.find_elements_by_css_selector(".fullname.show-popup-with-id.u-textTruncate")
        tweet1 = tweet[0].text
        tweet2 = tweet[1].text
        tweet3 = tweet[2].text
        tweet4 = tweet[3].text

        tweetsahip1 = tweetsahip[0].text
        tweetsahip2 = tweetsahip[1].text
        tweetsahip3 = tweetsahip[2].text
        tweetsahip4 = tweetsahip[3].text

        pp=browser.find_elements_by_css_selector(".avatar.js-action-profile-avatar")
        k=0
        j=0
        for span in pp:
            src = pp[k].get_attribute('src')
            k=k+1
            j=j+1
            urllib.request.urlretrieve(src,("pp_"+str(k)+".gif"))


        im = Image.open("pp_7.gif")
        newwidth=52
        newheight=52
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("pp_7.gif")

        im = Image.open("pp_6.gif")
        newwidth=52
        newheight=52
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("pp_6.gif")


        im = Image.open("pp_5.gif")
        newwidth=52
        newheight=52
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("pp_5.gif")


        im = Image.open("pp_4.gif")
        newwidth=52
        newheight=52
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("pp_4.gif")

        pp_1=ImageTk.PhotoImage(file="pp_4.gif",master=twittergui)
        pp_2=ImageTk.PhotoImage(file="pp_5.gif",master=twittergui)
        pp_3=ImageTk.PhotoImage(file="pp_6.gif",master=twittergui)
        pp_4=ImageTk.PhotoImage(file="pp_7.gif",master=twittergui)

        twittergui.update()
        twitterload.destroy()
        tweet1 = tk.Label(twittergui,image = pp_1,text="1. "+tweetsahip1+"\n"+tweet1,font=("Helvitca", 13),compound='left',fg='#1da1f2',bg='white')
        tweet1.grid(sticky='W',row=0,column=0)
        tweet1.image = pp_1
        tweet2 = tk.Label(twittergui,image = pp_2,text="2. "+tweetsahip2+"\n"+tweet2,font=("Helvitca", 13),compound='left',fg='#1da1f2',bg='white')
        tweet2.grid(sticky='W',row=1,column=0)
        tweet2.image=pp_2
        tweet3 = tk.Label(twittergui,image = pp_3,text="3. "+tweetsahip3+"\n"+tweet3,font=("Helvitca", 13),compound='left',fg='#1da1f2',bg='white')
        tweet3.grid(sticky='W',row=2,column=0)
        tweet3.image=pp_3
        tweet4 = tk.Label(twittergui,image = pp_4,text="4. "+tweetsahip4+"\n"+tweet4,font=("Helvitca", 13),compound='left',fg='#1da1f2',bg='white')
        tweet4.grid(sticky='W',row=3,column=0)
        tweet3.image=pp_4
        twittergui.update()
        

         

#        tweetbutton=tk.Button(twittergui,text="Tweetle",command=tweet_at)
#        tweetatma.grid(sticky='W',row=4,column=0)
#        tweetbutton.grid(sticky='W',row=5,column=0)



        def refresh():
            twittergui.withdraw()    
            twitterguiref.deiconify()
            twitterloadref=tk.Label(twitterguiref,text='YÜKLENİYOR....',font=('Helvitca',50),fg='White')
            twitterloadref.grid(sticky="W",row=0,column=0,pady=215)    
            twitterguiref.update()

            tweet=browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")
                          
            tweetsahip=browser.find_elements_by_css_selector(".fullname.show-popup-with-id.u-textTruncate")
            
            tweet1 = tweet[0].text
            tweet2 = tweet[1].text
            tweet3 = tweet[2].text
            tweet4 = tweet[3].text

            tweetsahip1 = tweetsahip[0].text
            tweetsahip2 = tweetsahip[1].text
            tweetsahip3 = tweetsahip[2].text
            tweetsahip4 = tweetsahip[3].text

            pp=browser.find_elements_by_css_selector(".avatar.js-action-profile-avatar")
            k=0
            j=0
            for span in pp:
                src = pp[k].get_attribute('src')
                k=k+1
                j=j+1
                urllib.request.urlretrieve(src,("pp_"+str(k)+".gif"))

            im = Image.open("pp_1.gif")
            newwidth=33
            newheight=33
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("pp_1.gif")

            im = Image.open("pp_2.gif")
            newwidth=33
            newheight=33
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("pp_2.gif")


            im = Image.open("pp_3.gif")
            newwidth=33
            newheight=33
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("pp_3.gif")


            im = Image.open("pp_4.gif")
            newwidth=33
            newheight=33
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("pp_4.gif")
            pp_1=ImageTk.PhotoImage(file="pp_1.gif")
            pp_2=ImageTk.PhotoImage(file="pp_2.gif")
            pp_3=ImageTk.PhotoImage(file="pp_3.gif")
            pp_4=ImageTk.PhotoImage(file="pp_4.gif")
            
            twitterguiref.update()
            tweet1 = tk.Label(twitterguiref,image = pp_1,text="1. "+tweetsahip1+"\n"+tweet1,compound='left',fg='#1da1f2',bg='white',anchor=tk.W)
            tweet1.grid(sticky='W',row=0,column=0)
            tweet1.image = pp_1
            tweet2 = tk.Label(twitterguiref,image = pp_2,text="2. "+tweetsahip2+"\n"+tweet2,compound='left',fg='#1da1f2',bg='white')
            tweet2.grid(sticky='W',row=1,column=0)
            tweet2.image=pp_2
            tweet3 = tk.Label(twitterguiref,image = pp_3,text="3. "+tweetsahip3+"\n"+tweet3,compound='left',fg='#1da1f2',bg='white')
            tweet3.grid(sticky='W',row=2,column=0)
            tweet3.image=pp_3
            tweet4 = tk.Label(twitterguiref,image = pp_4,text="4. "+tweetsahip4+"\n"+tweet4,compound='left',fg='#1da1f2',bg='white')
            tweet4.grid(sticky='W',row=3,column=0)
            tweet3.image=pp_4
            twittergui.update()
            twitterefresh=tk.Button(twitterguiref,text="Tweetleri Yenile ve Gör",command=refresh)
            twitterefresh.grid(row=4,column=0)


            twitterguiref.update()
            twittergui.mainloop()

        twitterefresh=tk.Button(twittergui,text="Tweetleri Yenile ve Gör",command=refresh)
        twitterefresh.grid(sticky='W',row=4,column=0)

        def geritw():
            twittergui.withdraw()
            main.deiconify()

        twittergeri=tk.Button(twittergui,text="Geri",command=geritw)
        twittergeri.grid(sticky='W',row=5,column=0)

        twittergui.update()
        twittergui.mainloop()            

        
def instagram():
    if igid=='' or igpass=='':
        messagebox.showerror("HATA","Lütfen Kullanıcı adı ve Şifre Giriniz:")

    elif igid !='' and igpass !='':
        main.withdraw()
        instagramyukgui.deiconify()
        
        instagramyukguiload=tk.Label(instagramyukgui,text='YÜKLENİYOR....',font=('Helvitca',50),fg='White',bg='#DD2A7B')
        instagramyukguiload.grid(row=0,column=0)    
        instagramyukgui.update()
        
        #browser=webdriver.Firefox()
        browser.get("https://www.instagram.com/")
        time.sleep(10)

        giris = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        giris.click()
        time.sleep(10)

        ıdısntagram = browser.find_element_by_name("username")
        passwordısntagram = browser.find_element_by_name("password")

        ıdısntagram.send_keys(igid)
        passwordısntagram.send_keys(igpass)

        time.sleep(5)

        login=browser.find_element_by_css_selector('._0mzm-.sqdOP.L3NKy')
        login.click()

        time.sleep(10)

        instaid=[]
        instaid=browser.find_elements_by_css_selector('.FPmhX.notranslate.nJAzx')
        img = []
        img=browser.find_elements_by_css_selector('.FFVAD')
        time.sleep(2)

        i = 0
        j = 0
        for span in img:
            
                src = img[i].get_attribute('src')

                i=i+1

                j=j+1

                urllib.request.urlretrieve(src, ('_insta_' + str(j)+'.gif'))

        #instaid1 = instaid[0].text
        #instaid2 = instaid[1].text
        #instaid3 = instaid[2].text
        #instaid4 = instaid[3].text
        #src = img.get_attribute('src')
        #urllib.request.urlretrieve(src,"photo.png")


        #w = tk.Scale(insgui, from_=0, to=2000)
        #w.grid(row=0,column=1)


        SCROLL_PAUSE_TIME = 0.5
        browser.execute_script("window.scrollTo(0, 7000)") 
        time.sleep(2)
  

        img1=[]
        img1=browser.find_elements_by_css_selector('.FFVAD')


        i = 0
        j = 3
        for span in img1:
            
                src = img1[i].get_attribute('src')

                i=i+1

                j=j+1

                urllib.request.urlretrieve(src, ('_insta_' + str(j)+'.gif'))
        

        im = Image.open('_insta_1.gif')
        width, height = im.size
        ypercent= 220/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("_insta_1.gif")

        im = Image.open('_insta_2.gif')
        width, height = im.size
        ypercent= 220/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("_insta_2.gif")

        im = Image.open('_insta_3.gif')
        width, height = im.size
        ypercent= 220/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("_insta_3.gif")

        im = Image.open('_insta_4.gif')
        width, height = im.size
        ypercent= 220/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("_insta_4.gif")


        im = Image.open('_insta_5.gif')
        width, height = im.size
        ypercent= 220/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("_insta_5.gif")
                      
        images = ["_insta_1.gif","_insta_2.gif","_insta_3.gif","_insta_4.gif","_insta_5.gif"]
        photos =cycle(ImageTk.PhotoImage(file=image,master=instagramgui)for image in images)
       
        def slideshow():
           img = next(photos)
           displayCanvas.config(image=img)
           instagramgui.after(5000, slideshow)
        
        instagramgui.configure(background='Black')    
        #arayüz.overrideredirect(True)
        #width = arayüz.winfo_screenwidth()
        #height = arayüz.winfo_screenwidth()
        #arayüz.geometry('%dx%d' % (640, 480))
        displayCanvas = tk.Label(instagramgui,height=220,width=480,bg='black')
        displayCanvas.grid(row=0,column=0)
        instagramgui.after(10, lambda: slideshow())
        instagramyukgui.withdraw()
        instagramgui.deiconify()

        def refreshins():
            instagramgui.withdraw()
            instagramguiref.deiconify()
            instagramguiload=tk.Label(instagramguiref,text='YÜKLENİYOR....',font=('Helvitca',50),fg='White',bg='#DD2A7B')
            instagramguiload.grid(row=0,column=0)    
            instagramguiref.update()
            
            browser.get("https://www.instagram.com/")

            instaid=[]
            instaid=browser.find_elements_by_css_selector('.FPmhX.notranslate.nJAzx')
            img = []
                    
            img=browser.find_elements_by_css_selector('.FFVAD')
                    
            time.sleep(2)

            i = 0
            j = 0
            for span in img:
                
                    src = img[i].get_attribute('src')

                    i=i+1

                    j=j+1

                    urllib.request.urlretrieve(src, ('_insta_' + str(j)+'.gif'))

            #instaid1 = instaid[0].text
            #instaid2 = instaid[1].text
            #instaid3 = instaid[2].text
            #instaid4 = instaid[3].text
            #src = img.get_attribute('src')
            #urllib.request.urlretrieve(src,"photo.png")


            #w = tk.Scale(insgui, from_=0, to=2000)
            #w.grid(row=0,column=1)


            SCROLL_PAUSE_TIME = 0.5
            browser.execute_script("window.scrollTo(0, 7000)") 
            time.sleep(2)
      

            img1=[]
            img1=browser.find_elements_by_css_selector('.FFVAD')


            i = 0
            j = 3
            for span in img1:
                
                    src = img1[i].get_attribute('src')

                    i=i+1

                    j=j+1

                    urllib.request.urlretrieve(src, ('_insta_' + str(j)+'.gif'))
            

            im = Image.open('_insta_1.gif')
            width, height = im.size
            ypercent= 220/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("_insta_1.gif")

            im = Image.open('_insta_2.gif')
            width, height = im.size
            ypercent= 220/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("_insta_2.gif")

            im = Image.open('_insta_3.gif')
            width, height = im.size
            ypercent= 220/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("_insta_3.gif")

            im = Image.open('_insta_4.gif')
            width, height = im.size
            ypercent= 220/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("_insta_4.gif")


            im = Image.open('_insta_5.gif')
            width, height = im.size
            ypercent= 220/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("_insta_5.gif")
                          
            images = ["_insta_1.gif","_insta_2.gif","_insta_3.gif","_insta_4.gif","_insta_5.gif"]
            photos =cycle(ImageTk.PhotoImage(file=image,master=instagramguiref)for image in images)

            def slideshow():
               img = next(photos)
               displayCanvas.config(image=img)
               instagramguiref.after(5000, slideshow)
                   
            instagramguiref.configure(background='Black')    
            #arayüz.overrideredirect(True)
            #width = arayüz.winfo_screenwidth()
            #height = arayüz.winfo_screenwidth()
            #arayüz.geometry('%dx%d' % (640, 480))
            displayCanvas = tk.Label(instagramguiref,height=220,width=480,bg='black')
            displayCanvas.grid(row=0,column=0)
            instagramguiref.after(10, lambda: slideshow())

            intstarefresh=tk.Button(instagramguiref,text="Postları Yenile",command = refreshins)
            intstarefresh.grid(row=1,column=0)
            def geriinref():
                instagramguiref.withdraw()
                main.deiconify()
            instagramrefgeri=tk.Button(instagramrefgui,text="Geri",command=geriinref)
            instagramrefgeri.grid(row=2,column=0)            
        intstarefresh=tk.Button(instagramgui,text="Postları Yenile",command = refreshins)
        intstarefresh.grid(row=1,column=0)

        def geriin():
            instagramgui.withdraw()
            main.deiconify()
            

        instagramgeri=tk.Button(instagramgui,text="Geri",command=geriin)
        instagramgeri.grid(row=2,column=0)
    
def ekrankoruyucu():
    main.withdraw()
    ekrangui.deiconify()

    def manzara():
        ekrangui.withdraw()
        manzaragui.deiconify()

        im = Image.open('manzara1.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("manzara1.gif")
        
        im = Image.open('manzara2.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("manzara2.gif")

        im = Image.open('manzara3.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("manzara3.gif")

        im = Image.open('manzara4.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("manzara4.gif")

        im = Image.open('manzara5.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("manzara5.gif")

        images = ["manzara1.gif","manzara2.gif","manzara3.gif","manzara4.gif","manzara5.gif"]
        photos =cycle(ImageTk.PhotoImage(file=image,master=manzaragui)for image in images)

        def slideshow():
           img = next(photos)
           displayCanvas.config(image=img)
           manzaragui.after(5000, slideshow)
               
        manzaragui.configure(background='Black')    
        #arayüz.overrideredirect(True)
        #width = arayüz.winfo_screenwidth()
        #height = arayüz.winfo_screenwidth()
        #arayüz.geometry('%dx%d' % (640, 480))
        displayCanvas = tk.Label(manzaragui,height=263,width=480,bg='black')
        displayCanvas.grid(row=0,column=0)
        manzaragui.after(10, lambda: slideshow())

        def geriman():
           manzaragui.withdraw()
           ekrangui.deiconify()
            

        manzarageri=tk.Button(manzaragui,text="Geri",command=geriman)
        manzarageri.grid(row=2,column=0)

    def aile():
        ekrangui.withdraw()
        ailegui.deiconify()       



        im = Image.open('aile1.gif')
        width, height = im.size
        ypercent= 320/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("aile1.gif")

        im = Image.open('aile2.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("aile2.gif")

        im = Image.open('aile3.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("aile3.gif")

        im = Image.open('aile4.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("aile4.gif")

        im = Image.open('aile4.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("aile4.gif")

        im = Image.open('aile5.gif')
        width, height = im.size
        ypercent= 263/height
        xpercent= 480/width
        if ypercent >= xpercent:
            newheight=xpercent*height
            newwidth=xpercent*width
        else:
            newheight=ypercent*height
            newwidth=ypercent*width
        im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
        im.save("aile5.gif")

        images = ["aile1.gif","aile2.gif","aile3.gif","aile4.gif","aile5.gif"]
        photos =cycle(ImageTk.PhotoImage(file=image,master=ailegui)for image in images)

        def slideshow():
           img = next(photos)
           displayCanvas.config(image=img)
           ailegui.after(5000, slideshow)


        ailegui.configure(background='Black')    
        #arayüz.overrideredirect(True)
        #width = arayüz.winfo_screenwidth()
        #height = arayüz.winfo_screenwidth()
        #arayüz.geometry('%dx%d' % (640, 480))
        displayCanvas = tk.Label(ailegui,height=263,width=480,bg='black')
        displayCanvas.grid(row=0,column=0)
        ailegui.after(10, lambda: slideshow())


        def geriaile():
           ailegui.withdraw()
           ekrangui.deiconify()


        ailegeri=tk.Button(ailegui,text="Geri",command=geriaile)
        ailegeri.grid(row=2,column=0)



    def aramaileindir():
        ekrangui.withdraw()
        aramagui.deiconify()  

        aramaentry=tk.Entry(aramagui)
        aramaentry.grid(row=0,column=0)

        def aramafotogösterme():
            aramagui.withdraw()
            global aramaget
            aramaget=aramaentry.get()
            
            fgöstergui.deiconify()
            fgösterguiload=tk.Label(fgöstergui,text='YÜKLENİYOR....',font=('Helvitca',50),fg='White',bg='black')
            fgösterguiload.grid(row=0,column=0) 
            fgöstergui.update() 

            browser.get('https://www.google.com/imghp?hl=en')

            #aramaclick=browser.find_element_by_css_selector(".gLFyf.gsfi")
            #aramaclick.click()
            time.sleep(2)
            aramaentrygiris=browser.find_element_by_css_selector("#sfcnt")
            aramaentrygiris.click()
            time.sleep(3)
            aramainput=browser.find_element_by_css_selector('#mib')
            aramainput.send_keys(aramaget)
            time.sleep(4)
            aramabutton=browser.find_element_by_id("tsbb")
            aramabutton.click()
            time.sleep(1)
            
            time.sleep(4)
            
            aramimg=[]
            aramaimg=browser.find_elements_by_css_selector('.GivUyc')            

            time.sleep(3)
            
            i = 0
            j = 2
            for span in aramaimg:

                    src2 = aramaimg[i].get_attribute('src')
                
                    i=i+1

                    j=j+1

                    urllib.request.urlretrieve(src2, ('indirilenfoto' + str(j)+'.gif'))

            im = Image.open('indirilenfoto3.gif')
            width, height = im.size
            ypercent= 280/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("indirilenfoto3.gif")

            im = Image.open('indirilenfoto4.gif')
            width, height = im.size
            ypercent= 280/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("indirilenfoto4.gif")

            im = Image.open('indirilenfoto5.gif')
            width, height = im.size
            ypercent= 280/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("indirilenfoto5.gif")

            im = Image.open('indirilenfoto6.gif')
            width, height = im.size
            ypercent= 280/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("indirilenfoto6.gif")

            im = Image.open('indirilenfoto7.gif')
            width, height = im.size
            ypercent= 263/height
            xpercent= 480/width
            if ypercent >= xpercent:
                newheight=xpercent*height
                newwidth=xpercent*width
            else:
                newheight=ypercent*height
                newwidth=ypercent*width
            im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
            im.save("indirilenfoto7.gif")
            
            images = ["indirilenfoto3.gif","indirilenfoto4.gif","indirilenfoto5.gif","indirilenfoto6.gif","indirilenfoto7.gif",]
            photos =cycle(ImageTk.PhotoImage(file=image,master=fgöstergui)for image in images)

            def slideshow():
                img = next(photos)
                displayCanvas.config(image=img)
                fgöstergui.after(5000, slideshow)
               
            fgöstergui.configure(background='Black')    
            #arayüz.overrideredirect(True)
            #width = arayüz.winfo_screenwidth()
            #height = arayüz.winfo_screenwidth()
            #arayüz.geometry('%dx%d' % (640, 480))
            displayCanvas = tk.Label(fgöstergui,height=263,width=480,bg='black')
            displayCanvas.grid(row=0,column=0)
            fgöstergui.after(10, lambda: slideshow())

            def gerifgöster():
                fgöstergui.withdraw()
                aramagui.deiconify()


            fgöstergeri=tk.Button(fgöstergui,text="Geri",command=gerifgöster)
            fgöstergeri.grid(row=1,column=0)
            
       
        aramabuttongui=tk.Button(aramagui,text='Arayüzde Arama yap',command=aramafotogösterme)
        aramabuttongui.grid(row=1,column=0)



        def geriarama():
           aramagui.withdraw()
           ekrangui.deiconify()


        aramageri=tk.Button(aramagui,text="Geri",command=geriarama)
        aramageri.grid(row=2,column=0)






    manzarabutton=tk.Button(ekrangui,text='Manzara Fotoğrafları',command=manzara)
    manzarabutton.grid(row=0,column=0)

    ailebutton=tk.Button(ekrangui,text='Aile Fotoğraları',command=aile)
    ailebutton.grid(row=0,column=1)

    aramaekranbutton=tk.Button(ekrangui,text='Arama Yapmak için:',command=aramaileindir)
    aramaekranbutton.grid(row=0,column=2)

    def geriekran():
       ekrangui.withdraw()
       main.deiconify()


    aramageri=tk.Button(ekrangui,text="Geri",command=geriekran)
    aramageri.grid(row=1,column=1)



twitterlogo=ImageTk.PhotoImage(file="twitter.png")
twitterbutton = tk.Button(main,command = twitter,image=twitterlogo,compound="top")
twitterbutton.grid(row=0,column=0,padx=25)

instalogo=ImageTk.PhotoImage(file="instagram.png")
instagrambutton=tk.Button(main,command = instagram,image=instalogo,compound="top")
instagrambutton.grid(row=0,column=1,padx=25)

infologinbutton=tk.Button(main,text="Giris Yap",font=("Helvitca",21),command = infologin,compound="top")
infologinbutton.grid(row=1,column=0)

ekrankoruyucubutton=tk.Button(main,text="Fotoğraflar",font=("Helvitca",21),command = ekrankoruyucu,compound="top")
ekrankoruyucubutton.grid(row=1,column=1)




saat = tk.Label(main,font=("Helvitca",21), bd=1, relief=tk.SUNKEN, anchor=tk.W) 
saat.grid(row=2,column=0)

im = Image.open('hava.png')
newwidth=26
newheight=26
im = im.resize((int(newwidth), int(newheight)), Image.ANTIALIAS)
im.save("hava.png")
sıcaklıkimage = ImageTk.PhotoImage(file="hava.png")
havalabel = tk.Label(main,image = sıcaklıkimage,text=sıcaklıktk+'C',font=("Helvitca", 21),compound='left')
havalabel.grid(row=2,column=1)

tick()

main.mainloop()




    

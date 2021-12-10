from tkinter import *
from tkinter.messagebox import*


host_files = {
    'Windows': r"C:\Windows\System32\drivers\etc\hosts",
    'Linux':'/etc/host',
    'MAC' : '/etc/hosts'
}
localhost = '127.0.0.1'

def block(win):
    def block_websites(websites):
        host_file = host_files['MAC']
        sites_to_block = list(websites.split(' , '))

        
        blocked_websites_txt = open('blocked_websites.txt', 'a')
        with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
            blocked_websites_txt.seek(0, 2)
            for site in sites_to_block:
                blocked_websites_txt.write(site)
      
        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.read()

            for site in sites_to_block:
                if site not in content_in_file:
                    hostfile.write(localhost + '\t' + site + '\n')
                    showinfo('Websites blocked!', message='We have blocked the websites you wanted blocked!')
                else:
                    showinfo('Website Already blocked!', 'A website you entered is already blocked')


    blck_wn = Toplevel(win, background='White')
    blck_wn.title("Block a website")
    blck_wn.geometry('300x200')
    blck_wn.resizable(False, False)

    Label(blck_wn, text='Block websites', background='White', font=("Georgia", 16)).place(x=80, y=0)
    Label(blck_wn, text='Enter the URLs (www.(sitename).com):', background='White', font=('Times', 13)).place(
        x=0, y=50)

    sites = Text(blck_wn, width=35, height=3)
    sites.place(x=0, y=100)

    submit_btn = Button(blck_wn, text='Submit', bg='Grey', command=lambda: block_websites(sites.get('1.0',END)))
    submit_btn.place(x=100, y=160)


def unblock(win):
    def unblock_websites(websites_to_unblock):
        host_file = host_files['MAC']

        with open(host_file, 'r+') as hostfile:
            content_in_file = hostfile.readlines()
            hostfile.seek(0)

            for line in content_in_file:
                if not any(site in line for site in websites_to_unblock):
                    hostfile.write(line)

                hostfile.truncate()

        with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
            file_content = blocked_websites_txt.readlines()
            blocked_websites_txt.seek(0)

            for line in file_content:
                if not any(site in line for site in websites_to_unblock):
                    blocked_websites_txt.write(line)

                blocked_websites_txt.truncate()


        Label(unblck_wn, text='Website Blocked!', font=("Times", 13), bg='Aquamarine').place()


    
    with open('blocked_websites.txt', 'r+') as blocked_websites:
        blck_sites = blocked_websites.read().splitlines()[2:]

    unblck_wn = Toplevel(win, background='white')
    unblck_wn.title("Block a website")
    unblck_wn.geometry('285x200')
    unblck_wn.resizable(False, False)

    Label(unblck_wn, text='Unblock websites', background='white', font=("Georgia", 16)).place(x=80, y=0)
    Label(unblck_wn, text='Select the URLs that you want to unblock:', background='white', font=('Times',
                                                                                                      13)).place(x=0, y=70)

    
    blck_sites_strvar = StringVar(unblck_wn)
    blck_sites_strvar.set(blck_sites[0])
    dropdown = OptionMenu(unblck_wn, blck_sites_strvar, *blck_sites)
    dropdown.config(width=20)
    dropdown.place(x=60, y=100)

    submit_btn = Button(unblck_wn, text='Submit', bg='MidnightBlue',
                        command=lambda: unblock_websites(blck_sites_strvar.get()))
    submit_btn.place(x=100, y=160)



root = Tk()
root.title("Personal Project")
root.geometry('400x300')
root.wm_resizable(False, False)


Label(root, text='Oluwasubomi Website Blocker', font=("Times", 16, "bold italic")).place(x=45, y=20)
Label(root, text='What do you want to do?', font=("Times", 14,"italic")).place(x=90, y=50)

Button(root, text='Block a Website', font=('Times', 16), bg='Grey', command=lambda: block(root)).place(x=110, y=100)

Button(root, text='Unblock a Website', font=('Times', 16), bg='Grey', command=lambda: unblock(root)).place(x=100, y=140)

root.update()
root.mainloop()

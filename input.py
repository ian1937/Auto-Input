from bs4 import BeautifulSoup
import requests, csv, pyautogui, re, sys
from  tkinter import *



shop_name = 'IvanPlastik'




def start_tokopedia():
    try:
        file = entry_file.get()
        speed = entry_speed.get()
        pyautogui.PAUSE = int(speed)
        pelanggan = entry_pelanggan.get()
        code = entry_invoice.get()



        with open(file) as html_file:
            soup = BeautifulSoup(html_file, 'lxml')
            page = soup.find('div', class_='content-area')


            for invoice in page.find_all_next('div'):
                header = str(invoice.find_all('span'))
                matches = re.findall(rf'{code}(.+?)</span>', header)
                number = str(matches).replace("[", "").replace("]", "").replace("'", "").replace("/", "")


                if number == '':
                    continue
                else:
                    pyautogui.click(pyautogui.locateCenterOnScreen('img/pelanggan.png'))
                    pyautogui.typewrite(pelanggan)
                    pyautogui.press('enter')
                    pyautogui.click(pyautogui.locateCenterOnScreen('img/invoice.png'))
                    pyautogui.press('enter')
                    pyautogui.typewrite(number)
                    pyautogui.press('enter', presses=7)


                for product in invoice.find_all('a'):
                    name = re.sub(' +', ' ', str(product.text).replace(shop_name, '').replace('\n', ''))
                    if name[0] == ' ':
                        continue
                    pyautogui.typewrite(name)

                    pyautogui.press('enter')
                    pyautogui.press('enter')


                    info = product.find_parent('tr')
                    removespace = re.sub(' +', ' ', str(info).replace('\n', ''))


                    quantity = re.findall(r'<td style="padding: 15px; text-align: center;" valign="top">(.+?)</td>', removespace)
                    removebracket = str(quantity).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
                    pyautogui.typewrite(str(removebracket))

                    pyautogui.press('enter')


                    price = re.findall(r'<td style="padding: 15px; white-space: nowrap; text-align: center;" valign="top">(.+?)</td>', removespace)
                    removeRp = str(price).replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace("Rp", "").replace(".", "")
                    if removeRp == '':
                        continue
                    pyautogui.typewrite(str(removeRp))

                    pyautogui.press('enter', presses=5)


                pyautogui.click(pyautogui.locateCenterOnScreen('img/simpan.png'))

            entry_message.delete(0,END)
            entry_message.insert(0, 'Done!')

    except IndexError:
        entry_message.delete(0,END)
        entry_message.insert(0, 'Something is wrong with your data.')
    except FileNotFoundError:
        entry_message.delete(0,END)
        entry_message.insert(0, 'File not found. Please check file name again.')
    except:
        entry_message.delete(0,END)
        entry_message.insert(0, 'Sorry, something went wrong.')




root = Tk()


button_start = Button(root, text='Start', command=start_tokopedia)

label_speed = Label(root, text='Speed (0.1 - 1)')
label_file = Label(root, text='File name :')
# label_shop = Label(root, text='Shop name')
label_invoice = Label(root, text='Invoice code :')
label_message = Label(root, text='Message :')
label_pelanggan = Label(root, text='No. Pelanggan :')


variable_speed = StringVar(root, value='1')
variable_file = StringVar(root, value='Invoice.html')
variable_customer = StringVar(root, value='1000')
variable_code = StringVar(root, value='/XX/IX/')


entry_speed = Entry(root, textvariable=variable_speed)
entry_file = Entry(root, textvariable=variable_file)
entry_message = Entry(root)
# entry_shop = Entry(root)
entry_invoice = Entry(root)
entry_pelanggan = Entry(root, textvariable=variable_customer)


button_start.grid(row=0, columnspan=2, pady=15)

label_speed.grid(row=1, sticky=W, padx=10)
label_file.grid(row=2, sticky=W, padx=10)
# label_shop.grid(row=3, sticky=W)
label_pelanggan.grid(row=3, sticky=W, padx=10)
label_invoice.grid(row=4, sticky=W, padx=10)
label_message.grid(row=5, sticky=W, padx=10)


entry_speed.grid(row=1, column=1, padx=10)
entry_file.grid(row=2, column=1, padx=10)
entry_pelanggan.grid(row=3, column=1, padx=10)
# entry_shop.grid(row=3, column=1)
entry_invoice.grid(row=4, column=1, padx=10)
#entry_message.configure(state='readonly')
entry_message.grid(row=6, columnspan=2,  sticky = W+E, ipady=30, padx=10, pady=10)


root.mainloop()


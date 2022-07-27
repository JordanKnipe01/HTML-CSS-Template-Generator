from tkinter import *
#from ttkthemes import themed_tk as tk #For set Themes
from tkinter import ttk
import tkinter as tk
import lxml
import shutil
import clipboard
import pyperclip
import klembord

feature_count = 0
specification_count = 0
item_count = 0
description_paragraph_count = 0
important_info_count = 0

feature_countl = []
specification_countl = []
item_countl = []
description_paragraph_countl = []
important_info_countl = []

features = []
specifications = []
items = []
description_paragraphs = []
important_paragraphs = []
class Win:


    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Window")
        self.window()
        fullscreen_width = self.root.winfo_screenwidth()
        fullscreen_height = self.root.winfo_screenheight()
        self.root.geometry("{}x{}".format(fullscreen_width - 10, fullscreen_height))
        self.root.minsize(int(fullscreen_width / 1.8), 400)
        self.root.maxsize(int(fullscreen_width), int(fullscreen_height))

    def window(self):
        "Cointains all the widgets:"
        self.mainframe  = tk.Frame(self.root,borderwidth=2,relief="groove")
        self.mainframe.grid(column=0,row=0, sticky="n")
        self.mainframe.grid_columnconfigure(0, weight=1)
        #self.mainframe.grid_rowconfigure(0, weight=1)
        self.root.minsize(int(self.root.winfo_screenwidth() / 1.15), self.root.winfo_screenheight())
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        """
        canvas = Canvas(self.mainframe)
        canvas.grid(column=0, row=0, sticky="nswe")
        scroll_bar = tk.Scrollbar(self.root, orient=VERTICAL, command=canvas.yview)
        scroll_bar.grid(column=1, row=0, sticky="nsw", rowspan=50)

        canvas.config(yscrollcommand=scroll_bar,scrollregion = canvas.bbox("all"))
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion = canvas.bbox("all")))

        second_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=second_frame, anchor="nw")
        """
        def frame0():
            "Contains the listbox on the left"
            self.frm0 = tk.Frame(self.mainframe,borderwidth=2, relief="groove")
            self.frm0.grid(column=0, row=0,
                           sticky="nswe")  # adapt to window

            self.frm0.grid_columnconfigure(0, weight=1)
            self.frm0.grid_columnconfigure(1, weight=1)


            #self.frm0.grid_rowconfigure(1, weight=1)

            self.description_label1 = tk.Label(self.frm0, text="Description", width=46)
            self.description_label1.grid(column=0, row=0, sticky='nswe')
            self.description_label1.config(font=("Roboto", 12,'bold','underline'))
            self.description_label1.columnconfigure(0,weight=1)
            #self.description_entry = Entry(self.frm0)
            #self.description_entry.grid(column=0, row=2, sticky=W, pady=2)

            main_button = Button(self.frm0, text='+', command=add_paragraph, width=5,font=("Courier",12,'bold'))
            main_button.grid(column=0, row=1,sticky='w',padx=140)
            main_button.columnconfigure(0,weight=1)

            minus_button = Button(self.frm0, text='-', command=remove_description, width=5, font=("Courier", 12, 'bold'))
            minus_button.grid(column=0, row=1,sticky='e', padx=140)

            minus_button.columnconfigure(0, weight=1)



        def frame5():
            "Contains the listbox on the left"
            self.frm5 = tk.Frame(self.mainframe,borderwidth=2, relief="groove")
            self.frm5.grid(column=4, row=0,
                           sticky="nswe")  # adapt to window


            self.description_label0 = tk.Label(self.frm5, text="Important Information",width=46)
            self.description_label0.grid(column=0, row=0, padx=0,sticky='nswe')
            self.description_label0.config(font=("Roboto", 12,'bold','underline'))
            #self.description_entry = Entry(self.frm0)
            #self.description_entry.grid(column=0, row=2, sticky=W, pady=2)

            main_button = Button(self.frm5, text='+', command=add_Important_Info, width=5,font=("Courier",12,'bold'))
            main_button.grid(column=0, row=1,sticky='w', padx=140)
            minus_button = Button(self.frm5, text='-', command=remove_important_Info, width=5, font=("Courier", 12, 'bold'))
            minus_button.grid(column=0, row=1, sticky='e', padx=140)

            #main_button.grid_columnconfigure(0, weight=1)
            #minus_button.grid_columnconfigure(0, weight=1)
            #main_button.grid_rowconfigure(1, weight=1)
            #minus_button.grid_rowconfigure(1, weight=1)
            #self.description_label0.grid_rowconfigure(0, weight=1)
            #self.description_label0.grid_columnconfigure(0, weight=1)
            self.frm5.grid_columnconfigure(0, weight=1)
            self.frm5.grid_columnconfigure(4, weight=1)
            #self.frm5.grid_rowconfigure(0, weight=1)
            #self.frm5.grid_rowconfigure(1, weight=1)
            """
            self.root.grid_columnconfigure(4, weight=1)
            self.root.grid_columnconfigure(0, weight=1)
            self.root.grid_columnconfigure(1, weight=1)
            self.root.grid_columnconfigure(2, weight=1)
            self.root.grid_columnconfigure(3, weight=1)
            self.root.grid_columnconfigure(5, weight=1)
            self.frm5.grid_columnconfigure(1, weight=1)
            """
        def frame1():
            "Contains the listbox on the left"
            self.frm1 = tk.Frame(self.mainframe,borderwidth=2, relief="groove")
            self.frm1.grid(column=1, row=0,
                           sticky="nswe")  # adapt to window

            self.label1 = tk.Label(self.frm1,text="Features & Benefits", width=22)
            self.label1.grid(column=1,row=0,sticky='nswe')
            self.label1.config(font=("Roboto", 12,'bold','underline'))
            main_button = Button(self.frm1, text='+', command=add_feature, width=5,font=("Courier",12,'bold'))
            main_button.grid(column=1, row=1,sticky='w', padx=30)
            minus_button = Button(self.frm1, text='-', command=remove_features, width=5, font=("Courier", 12, 'bold'))
            minus_button.grid(column=1, row=1, sticky='e', padx=30)

            self.emptylabel2 = Label(self.frm1,width=1)
            self.emptylabel2.grid(column=0, row=0 ,sticky='nswe')

            self.frm1.grid_columnconfigure(0, weight=1)
            self.frm1.grid_columnconfigure(1, weight=1)
            """
            
            self.frm1.grid_rowconfigure(0, weight=1)
"""
        def frame2():
            "Contains the listbox on the left"
            self.frm2 = tk.Frame(self.mainframe,borderwidth=2, relief="groove")
            self.frm2.grid(column=2, row=0,
                               sticky="nswe")  # adapt to window

            self.label1 = tk.Label(self.frm2, text="Specifications",width=22)
            self.label1.grid(column=1, row=0)
            self.label1.config(font=("Roboto", 12,'bold','underline'))
            main_button = Button(self.frm2, text='+', command=add_specification, width=5,font=("Courier",12,'bold'))
            main_button.grid(column=1, row=1, sticky='w', padx=30)

            min_button = Button(self.frm2, text='-', command=remove_specifications, width=5, font=("Courier", 12, 'bold'))
            min_button.grid(column=1, row=1, sticky='e', padx=30)


            self.emptylabel2 = Label(self.frm2, width=1)
            self.emptylabel2.grid(column=0, row=0,sticky='nswe')
            self.frm2.grid_columnconfigure(2, weight=1)
            self.frm2.grid_columnconfigure(0, weight=1)
            self.frm2.grid_columnconfigure(1, weight=1)

        def frame4():
            "Contains the listbox on the left"
            self.frm4 = tk.Frame(self.mainframe,borderwidth=2, relief="groove")
            self.frm4.grid(column=3, row=0,
                               sticky="nswe")  # adapt to window

            self.label1 = tk.Label(self.frm4, text="What is Included?", width=22)
            self.label1.grid(column=1, row=0,sticky='nswe')
            self.label1.config(font=("Roboto", 12,'bold','underline'))
            main_button = Button(self.frm4, text='+', command=add_Item, width=5,font=("Courier",12,'bold'))
            main_button.grid(column=1, row=1,sticky='w', padx=30)

            min_button = Button(self.frm4, text='-', command=remove_items, width=5, font=("Courier", 12, 'bold'))
            min_button.grid(column=1, row=1, sticky='e', padx=30)

            self.emptylabel2 = Label(self.frm4,width=1)
            self.emptylabel2.grid(column=0, row=0,sticky='nswe')
            self.frm4.grid_columnconfigure(3, weight=1)


        def frame3():
            "Contains the listbox on the left"
            self.frm3 = tk.Frame(self.mainframe,borderwidth=2, relief="groove")
            self.frm3.grid(column=5, row=0,
                               sticky="nswe")  # adapt to window

            self.submit_label = tk.Label(self.frm3, text="Submit")
            self.submit_label.grid(column=1, row=0,sticky='nswe')
            self.submit_label.config(font=("Roboto", 12,'bold','underline'))
            main_button = Button(self.frm3, text='Webshop Template', command=GenerateHTML)
            main_button.grid(column=1, row=1,sticky='nswe')
            ebay_button = Button(self.frm3, text='Ebay Template', command=GenerateEbayHTML)
            ebay_button.grid(column=1, row=2, sticky='nswe')
            self.frm3.grid_columnconfigure(5, weight=1)

        def GenerateEbayHTML():
            from bs4 import BeautifulSoup

            features_final = []
            specifications_final = []
            items_final = []
            description_paragraphs_final = []
            important_infos_final = []

            for feat in features:
                textfeat = feat.get()
                print(textfeat)
                features_final.append(textfeat)

            for spec in specifications:
                textspec = spec.get()
                print(textspec)
                specifications_final.append(textspec)

            for item in items:
                textitem = item.get()
                print(textitem)
                items_final.append(textitem)

            for paragraph in description_paragraphs:
                textparagraph = paragraph.get("1.0", END)
                print(textparagraph)
                description_paragraphs_final.append(textparagraph)

            for importantinfo in important_paragraphs:
                textimportantparagraph = importantinfo.get("1.0", END)
                print(textimportantparagraph)
                important_infos_final.append(textimportantparagraph)

            # Open test.html for reading
            shutil.copy2('EbayTemplate.html', 'newEbay.html')

            with open('EbayTemplate.html', 'r') as html_file:
                soup = BeautifulSoup(html_file.read(), features='html.parser')

                # :::::::Important Information::::::
                t = len(important_infos_final)
                while t > 0:
                    importantinfotag = soup.new_tag("p", **{'class': 'importantinfoparagraph'})
                    importantinfotag.string = "test"
                    foundpimportanttag = soup.find("div", id='ImportantInfo')
                    foundpimportanttag.append(importantinfotag)
                    t -= 1

                for idximportantparagraph, tag in enumerate(soup.find_all("p", {"class": 'importantinfoparagraph'})):
                    tag.string.replace_with(important_infos_final[idximportantparagraph])

                # :::::::Description::::::
                z = len(description_paragraphs_final)
                while z > 0:
                    paragraphtag = soup.new_tag("p", **{'class': 'paragraph'})
                    paragraphtag.string = "test"
                    foundparagraphtag = soup.find("div", id='DescriptionBox')
                    foundparagraphtag.append(paragraphtag)
                    z -= 1

                for idxparagraph, tag in enumerate(soup.find_all("p", {"class": 'paragraph'})):
                    tag.string.replace_with(description_paragraphs_final[idxparagraph])

                # :::::::FEATURES AND BENEFITS::::::

                # Go through each 'A' tag and replace text with '-'
                if (len(features_final) > len(soup.find_all("li", {"class": 'feature'}))):
                    x = len(features_final) - len(soup.find_all("li", {"class": 'feature'}))

                    while x > 0:
                        feattag = soup.new_tag("li", **{'class': 'feature'})
                        feattag.string = "test"
                        foundfeattag = soup.find("div", id='FeaturesList').find_next('ul')
                        foundfeattag.append(feattag)
                        x -= 1

                for idxfeat, tag in enumerate(soup.find_all("li", {"class": 'feature'})):
                    tag.string.replace_with(features_final[idxfeat])

                # Store prettified version of modified html
                # new_text = soup.prettify()

                # :::::::SPECIFICATIONS::::::

                # Go through each 'A' tag and replace text with '-'
                if (len(specifications_final) > len(soup.find_all("li", {"class": 'specification'}))):
                    y = len(specifications_final) - len(soup.find_all("li", {"class": 'specification'}))

                    while y > 0:
                        spectag = soup.new_tag("li", **{'class': 'specification'})
                        spectag.string = "test"
                        foundspectag = soup.find("div", id='SpecificationsList').find_next('ul')
                        foundspectag.append(spectag)
                        y -= 1
                        # print(y)

                print("specs in list" + str(len(specifications_final)))
                print("specs in listssss" + str(len(specifications)))
                print("specs on html" + str(len(soup.find_all("li", {"class": 'specification'}))))

                for idxspec, tag in enumerate(soup.find_all("li", {"class": 'specification'})):
                    tag.string.replace_with(specifications_final[idxspec])

                    # :::::::INCLUDED::::::

                    # Go through each 'A' tag and replace text with '-'
                if (len(items_final) > len(soup.find_all("li", {"class": 'item'}))):
                    x = len(items_final) - len(soup.find_all("li", {"class": 'item'}))

                    while x > 0:
                        itemtag = soup.new_tag("li", **{'class': 'item'})
                        itemtag.string = "test"
                        founditemtag = soup.find("div", id='ItemsList').find_next('ul')
                        founditemtag.append(itemtag)
                        x -= 1

                for idxitem, tag in enumerate(soup.find_all("li", {"class": 'item'})):
                    tag.string.replace_with(items_final[idxitem])
                # Store prettified version of modified html
                if important_info_count == 0:
                    element = soup.find("td", id="Important")
                    if element:
                        element.decompose()
                if item_count == 0:
                    element = soup.find("td", id="Included")
                    if element:
                        element.decompose()
                if feature_count == 0:
                    element = soup.find("td", id="FnB")
                    if element:
                        element.decompose()
                if specification_count == 0:
                    element = soup.find("td", id="Specs")
                    if element:
                        element.decompose()
                #new_text = soup.prettify()
                this_text = str(soup)
            # Write new contents to test.html
            with open('newEbay.html', mode='w', encoding='UTF-8') as new_html_file:
                new_html_file.write(this_text)
            #pyperclip.copy('')
            #clipboard.copy(new_text)
            #pyperclip.copy(new_text)
            #klembord.set_with_rich_text(new_text,new_text)
            klembord.set_text(this_text)

        def GenerateHTML():
            from bs4 import BeautifulSoup

            features_final = []
            specifications_final = []
            items_final = []
            description_paragraphs_final = []
            important_infos_final = []

            for feat in features:
                textfeat = feat.get()
                print(textfeat)
                features_final.append(textfeat)

            for spec in specifications:
                textspec = spec.get()
                print(textspec)
                specifications_final.append(textspec)

            for item in items:
                textitem = item.get()
                print(textitem)
                items_final.append(textitem)

            for paragraph in description_paragraphs:
                textparagraph = paragraph.get("1.0", END)
                print(textparagraph)
                description_paragraphs_final.append(textparagraph)

            for importantinfo in important_paragraphs:
                textimportantparagraph = importantinfo.get("1.0", END)
                print(textimportantparagraph)
                important_infos_final.append(textimportantparagraph)


            # Open test.html for reading
            shutil.copy2('WebpageTemplate.html','newTemplate.html')

            with open('WebpageTemplate.html', 'r') as html_file:
                soup = BeautifulSoup(html_file.read(), features='html.parser')

                # :::::::Important Information::::::
                t = len(important_infos_final)
                while t > 0:
                    importantinfotag = soup.new_tag("p", **{'class': 'importantinfoparagraph'})
                    importantinfotag.string = "test"
                    foundpimportanttag = soup.find("div", id='ImportantInfo')
                    foundpimportanttag.append(importantinfotag)
                    t -= 1

                for idximportantparagraph, tag in enumerate(soup.find_all("p", {"class": 'importantinfoparagraph'})):
                    tag.string.replace_with(important_infos_final[idximportantparagraph])

                # :::::::Description::::::
                z = len(description_paragraphs_final)
                while z > 0:
                    paragraphtag = soup.new_tag("p", **{'class': 'paragraph'})
                    paragraphtag.string = "test"
                    foundparagraphtag = soup.find("div", id='DescriptionBox')
                    foundparagraphtag.append(paragraphtag)
                    z -= 1

                for idxparagraph, tag in enumerate(soup.find_all("p", {"class": 'paragraph'})):
                    tag.string.replace_with(description_paragraphs_final[idxparagraph])


                # :::::::FEATURES AND BENEFITS::::::

                # Go through each 'A' tag and replace text with '-'
                if(len(features_final) > len(soup.find_all("li", {"class": 'feature'}))):
                    x = len(features_final) - len(soup.find_all("li", {"class": 'feature'}))


                    while x > 0:
                        feattag = soup.new_tag("li", **{'class':'feature'})
                        feattag.string = "test"
                        foundfeattag = soup.find("div", id='FeaturesList').find_next('ul')
                        foundfeattag.append(feattag)
                        x -= 1



                for idxfeat, tag in enumerate(soup.find_all("li", {"class": 'feature'})):
                    tag.string.replace_with(features_final[idxfeat])

                # Store prettified version of modified html
                #new_text = soup.prettify()




                # :::::::SPECIFICATIONS::::::

                # Go through each 'A' tag and replace text with '-'
                if (len(specifications_final) > len(soup.find_all("li", {"class": 'specification'}))):
                    y = len(specifications_final) - len(soup.find_all("li", {"class": 'specification'}))

                    while y > 0:
                        spectag = soup.new_tag("li", **{'class': 'specification'})
                        spectag.string = "test"
                        foundspectag = soup.find("div", id='SpecificationsList').find_next('ul')
                        foundspectag.append(spectag)
                        y -= 1
                        #print(y)

                print("specs in list" + str(len(specifications_final)))
                print("specs in listssss" + str(len(specifications)))
                print("specs on html" + str(len(soup.find_all("li", {"class": 'specification'}))))

                for idxspec, tag in enumerate(soup.find_all("li", {"class": 'specification'})):
                    tag.string.replace_with(specifications_final[idxspec])

                    # :::::::INCLUDED::::::

                    # Go through each 'A' tag and replace text with '-'
                if (len(items_final) > len(soup.find_all("li", {"class": 'item'}))):
                    x = len(items_final) - len(soup.find_all("li", {"class": 'item'}))

                    while x > 0:
                        itemtag = soup.new_tag("li", **{'class': 'item'})
                        itemtag.string = "test"
                        founditemtag = soup.find("div", id='ItemsList').find_next('ul')
                        founditemtag.append(itemtag)
                        x -= 1

                for idxitem, tag in enumerate(soup.find_all("li", {"class": 'item'})):
                    tag.string.replace_with(items_final[idxitem])
                # Store prettified version of modified html
                if important_info_count == 0:
                    element = soup.find("tr", id="Important")
                    if element:
                        element.decompose()
                if item_count == 0:
                    element = soup.find("tr", id="Included")
                    if element:
                        element.decompose()
                if feature_count == 0:
                    element = soup.find("tr", id="FnB")
                    if element:
                        element.decompose()
                if specification_count == 0:
                    element = soup.find("tr", id="Specs")
                    if element:
                        element.decompose()
                new_text = soup.prettify()


            # Write new contents to test.html
            with open('newTemplate.html', mode='w') as new_html_file:
                new_html_file.write(new_text)



            #clipboard.copy(new_text)
            #pyperclip.copy(new_text)
            klembord.set_text(new_text)


        def remove_important_Info():
            global important_info_count
            global important_paragraphs
            if(important_info_count <= 0):
                return
            important_info_count -= 1
            listlen = len(important_paragraphs)
            important_paragraphs[listlen - 1].destroy()
            important_paragraphs.remove(important_paragraphs[listlen - 1])
            important_info_countl[listlen - 1].destroy()
            important_info_countl.remove(important_info_countl[listlen - 1])

        def remove_description():
            global description_paragraph_count
            global description_paragraphs
            if(description_paragraph_count <= 0):
                return
            description_paragraph_count -= 1
            listlen = len(description_paragraphs)
            description_paragraphs[listlen - 1].destroy()
            description_paragraphs.remove(description_paragraphs[listlen - 1])
            description_paragraph_countl[listlen - 1].destroy()
            description_paragraph_countl.remove(description_paragraph_countl[listlen - 1])

        def remove_features():
            global features
            global feature_count
            if(feature_count <= 0):
                return
            feature_count -= 1
            listlen = len(features)
            features[listlen - 1].destroy()
            features.remove(features[listlen - 1])
            feature_countl[listlen - 1].destroy()
            feature_countl.remove(feature_countl[listlen - 1])

        def remove_specifications():
            global specification_count
            global specifications
            if(specification_count <= 0):
                return
            specification_count -= 1
            listlen = len(specifications)
            specifications[listlen - 1].destroy()
            specifications.remove(specifications[listlen - 1])
            specification_countl[listlen - 1].destroy()
            specification_countl.remove(specification_countl[listlen - 1])

        def remove_items():
            global item_count
            global items
            if(item_count <= 0):
                return
            item_count -= 1
            listlen = len(items)
            items[listlen - 1].destroy()
            items.remove(items[listlen - 1])
            item_countl[listlen - 1].destroy()
            item_countl.remove(item_countl[listlen - 1])


        def add_Important_Info():
            global important_info_count
            global important_paragraphs
            if(important_info_count >= 10):
                return
            important_info_count += 1
            self.important_label = Label(self.frm5, text=important_info_count)
            self.important_label.grid(column=0,row=important_info_count+2)
            self.important_entry = Text(self.frm5,width=52,height = 5)
            self.important_entry.grid(column=0,row=important_info_count+2,pady=4)

            print("Features: " + str(important_info_count))
            important_paragraphs.append(self.important_entry)

            important_info_countl.append(self.important_label)
            print(len(important_paragraphs))
            for importantparagraph in important_paragraphs:
                print(importantparagraph)

        def add_paragraph():
            global description_paragraph_count
            global description_paragraphs
            if (description_paragraph_count >= 10):
                return
            description_paragraph_count += 1
            self.description_label = Label(self.frm0, text=description_paragraph_count)
            self.description_label.grid(column=0,row=description_paragraph_count+2)
            self.description_entry = Text(self.frm0, width=52, height=5)

            self.description_entry.grid(column=0,row=description_paragraph_count+2, pady=4)
            print("Features: " + str(description_paragraph_count))
            description_paragraphs.append(self.description_entry)
            description_paragraph_countl.append(self.description_label)
            print(len(description_paragraphs))
            for paragraph in description_paragraphs:
                print(paragraph)

        def add_feature():
            global feature_count
            global features
            if (feature_count >= 34):
                return
            feature_count += 1
            self.feature_label = Label(self.frm1, text=feature_count)
            self.feature_label.grid(column=0,row=feature_count+2)
            self.feature_entry = Entry(self.frm1,width=33)
            self.feature_entry.grid(column=1,row=feature_count+2,pady=4)
            print("Features: " + str(feature_count))
            features.append(self.feature_entry)
            feature_countl.append(self.feature_label)
            print(len(features))
            for feat in features:
                print(feat)


        def add_specification():
            global specification_count
            global specifications
            if (specification_count >= 34):
                return
            specification_count += 1
            self.spec_label1 = Label(self.frm2, text=specification_count)
            self.spec_label1.grid(column=0,row=specification_count+2)
            self.spec_entry1 = Entry(self.frm2,width=33)
            self.spec_entry1.grid(column=1,row=specification_count+2,pady=4)
            print("Specifications: " + str(specification_count))
            specifications.append(self.spec_entry1)
            specification_countl.append(self.spec_label1)
            print(len(specifications))
            for spec in specifications:
                print(spec)

        def add_Item():
            global item_count
            global items
            if (item_count >= 34):
                return
            item_count += 1
            self.item_label = Label(self.frm4, text=item_count)
            self.item_label.grid(column=0,row=item_count+2)
            self.item_entry = Entry(self.frm4,width=33)
            self.item_entry.grid(column=1,row=item_count+2,pady=4)
            print("Features: " + str(item_count))
            items.append(self.item_entry)
            item_countl.append(self.item_label)
            print(len(items))
            for item in items:
                print(item)


        def widget_design():
            "The widgets on the window"
            frame1()
            frame2()
            frame0()
            frame3()
            frame4()
            frame5()
            #listbox()


        widget_design()


win = Win()
win.root.mainloop()
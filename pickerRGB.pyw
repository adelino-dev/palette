import tkinter as tk

class PickerRGB(object):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame1 = tk.Frame(self.frame)
        self.frame2 = tk.Frame(self.frame)
        self.frame3 = tk.Frame(self.frame)
        self.frame4 = tk.Frame(self.frame)
        self.frame5 = tk.Frame(self.frame)

        self.redValue = tk.IntVar()
        self.greenValue = tk.IntVar()
        self.blueValue = tk.IntVar()
        self.rgbValue = tk.StringVar()

        #Labels:
        self.label_red = tk.Label(self.frame1,text = "Red:")
        self.label_green = tk.Label(self.frame2, text = "Green:")
        self.label_blue = tk.Label(self.frame3, text = "Blue:")
        self.label_rgb_R = tk.Label(self.frame4, text = "R")
        self.label_rgb_G = tk.Label(self.frame4, text = "G")
        self.label_rgb_B = tk.Label(self.frame4, text = "B:")
    
        #Scales:
        self.scale_red = tk.Scale(self.frame1,
                                  from_ = 0, to = 100,
                                  orient = tk.HORIZONTAL,
                                  variable = self.redValue,
                                  command = self._changeColor,)
        
        self.scale_green = tk.Scale(self.frame2,
                                    from_ = 0, to = 100,
                                    orient = tk.HORIZONTAL,
                                    variable = self.greenValue,
                                    command = self._changeColor)
        
        self.scale_blue = tk.Scale(self.frame3,
                                   from_ = 0, to = 100,
                                   orient = tk.HORIZONTAL,
                                   variable = self.blueValue,
                                   command = self._changeColor)
        
        #Entries:
        self.entry_red = tk.Entry(self.frame1)
        self.entry_green = tk.Entry(self.frame2)
        self.entry_blue = tk.Entry(self.frame3)
        self.entry_rgb = tk.Entry(self.frame4,
                                  bd= 0,
                                  textvariable = self.rgbValue,
                                  width = 9)

        
        
        #Canvas:
        self.canvas = tk.Canvas(self.frame5)
        
        #### Binding the events ####
        
        self.entry_red.bind('<Return>', self._setEntryRed)
        self.entry_green.bind('<Return>', self._setEntryGreen)
        self.entry_blue.bind('<Return>', self._setEntryBlue)
        self.entry_rgb.bind('<Return>', self._setEntryRGB)

        ### Seting widgets formatation ###
        self._formatWidgets()
        
        ### Packing ###
        self.label_red.pack(side = tk.LEFT)
        self.label_green.pack(side = tk.LEFT)
        self.label_blue.pack(side = tk.LEFT)

        self.label_rgb_R.pack(side = tk.LEFT)
        self.label_rgb_G.pack(side = tk.LEFT)
        self.label_rgb_B.pack(side = tk.LEFT)
        
        self.scale_red.pack(side = tk.LEFT)
        self.scale_green.pack(side = tk.LEFT)
        self.scale_blue.pack(side = tk.LEFT)
        
        self.entry_red.pack(side = tk.LEFT)
        self.entry_green.pack(side = tk.LEFT)
        self.entry_blue.pack(side = tk.LEFT)
        self.entry_rgb.pack()

        self.canvas.pack()
        
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame.pack()



    def _changeColor(self, event):
        """Change the canva color according to the scales inputs (and also update the entries inputs)"""
        self.red = (hex(self.scale_red.get()).split('x'))[1]
        self.green = (hex(self.scale_green.get()).split)('x')[1]
        self.blue = (hex(self.scale_blue.get()).split('x'))[1]
        
        if len(self.red) == 1:
            self.red = '0'+self.red
        if len(self.green) == 1:
            self.green = '0'+self.green
        if len(self.blue) == 1:
            self.blue = '0'+self.blue
        
        self.rgb = "#"+self.red+self.green+self.blue
        self.canvas['bg'] = self.rgb
        self._updateEntries(event)

    def _updateEntries(self, event):
        """Update the entries inputs according to the scales inputs"""
        self.len_inputRGB = len(self.entry_rgb.get())
        self.entry_rgb.delete(0, last= self.len_inputRGB)
        self.entry_rgb.insert(0, self.rgb)

        self.len_inputRed = len(self.entry_red.get())
        self.entry_red.delete(0, last= self.len_inputRed)
        self.entry_red.insert(0, self.scale_red.get())

        self.len_inputGreen = len(self.entry_green.get())
        self.entry_green.delete(0, last= self.len_inputGreen)
        self.entry_green.insert(0, self.scale_green.get())
        
        self.len_inputBlue = len(self.entry_blue.get())
        self.entry_blue.delete(0, last= self.len_inputBlue)
        self.entry_blue.insert(0, self.scale_blue.get())

    def _setEntryRed(self, event):
        """Update the scale red input according to the entry red input"""
        self.inputRed = int(self.entry_red.get())
        self.scale_red.set(self.inputRed)
        
    def _setEntryGreen(self, event):
        """Update the scale green input according to the entry green input"""
        self.inputGreen = int(self.entry_green.get())
        self.scale_green.set(self.inputGreen)
        
    def _setEntryBlue(self, event):
        """Update the scale blue input according to the entry blue input"""
        self.inputBlue = int(self.entry_blue.get())
        self.scale_blue.set(self.inputBlue)
        
    def _setEntryRGB(self, event):
        """Update the scales inputs according to the entry RGB input"""
        self.inputRGB = self.entry_rgb.get()
        self.inputRed = self.inputRGB[1:3]
        self.inputGreen = self.inputRGB[3:5]
        self.inputBlue = self.inputRGB[5:7]
        
        self.scale_red.set(self.inputRed)
        self.scale_green.set(self.inputGreen)
        self.scale_blue.set(self.inputBlue)

    def _formatWidgets(self, widthCanvas = 400):
        self.frame['bg'] = self.frame1['bg'] = self.frame2['bg'] = self.frame3['bg'] = self.frame4['bg'] = "white"
        #self.frame1['anchor'] = self.frame2['anchor'] = self.frame3['anchor'] = self.frame4['anchor'] = "nw"
        self.frame5['bg'] = "gray"
        self.frame5['pady'] = 3; self.frame5['padx'] = 3
        self.frame4['pady'] = 10; self.frame4['padx'] = 3
        self.frame['pady'] = 20; self.frame['padx'] = 80

        self.canvas['width'] = self.canvas['height'] = widthCanvas
        self.canvas['bd'] = 3
        self.canvas['bg'] = "#000"
        
        self.label_red['fg'] = self.label_rgb_R['fg'] = 'red'
        self.label_green['fg'] = self.label_rgb_G['fg'] = 'green'
        self.label_blue['fg'] = self.label_rgb_B['fg'] = 'blue'
        self.label_red['bg'] = self.label_green['bg'] = self.label_blue['bg'] = self.frame['bg']
        self.label_rgb_R['bg'] = self.label_rgb_G['bg'] = self.label_rgb_B['bg'] = self.frame['bg']
        self.label_red['width'] = self.label_green['width'] = self.label_blue['width'] = 6
        self.label_rgb_R['width'] = self.label_rgb_G['width'] = self.label_rgb_B['width'] = 0
        self.label_red['anchor'] = self.label_green['anchor'] = self.label_blue['anchor'] = 'sw'
        self.label_red['font'] = self.label_green['font'] = self.label_blue['font'] = ("Times New Roman", 13)
        
        self.entry_red['bd'] = self.entry_green['bd'] = self.entry_blue['bd'] = 1
        self.entry_red['width'] = self.entry_green['width'] = self.entry_blue['width'] = 5

        self.scale_red['cursor'] = self.scale_green['cursor'] = self.scale_blue['cursor'] = "hand2"
        self.scale_red['bg'] = self.scale_green['bg'] = self.scale_blue['bg'] = self.frame['bg']
        self.scale_red['length'] = self.scale_green['length'] = self.scale_blue['length'] = int(self.canvas['width'])
        
        
        
if __name__ == "__main__":
    window = tk.Tk()
    window.title("RGB Color Picker")
    PickerRGB(window)
    window.mainloop()


        


        

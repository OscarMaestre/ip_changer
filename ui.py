import tkinter


class UI(tkinter.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Prueba")
         
def main():
  
    root = tkinter.Tk()
    app = UI()
    root.mainloop()  


if __name__ == '__main__':
    main()   
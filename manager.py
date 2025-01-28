from tkinter import Tk, Frame  
from container import Container

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Nombre de la Empresa") #Cambiaar el nombre
        self.resizable(False, False)
        self.configure(bg="#C6D9E3")
        
        window_width = 800
        window_height = 400
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.container = Frame(self, bg="#C6D9E3")
        self.container.pack(fill="both", expand=True)
        
        self.frames = {
            Container: None
        }
        
        # Con estas dos llamadas podemos ver lo que hay en el container
        self.load_frame()
        self.show_frame(Container)
        
    def load_frame(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame
            
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise() 

def main():
    app = Manager()
    app.mainloop()
    
if __name__ == "__main__":
    main()
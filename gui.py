import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os

class RamDiskBuilderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("linux Builder...")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Memória onde os ficheiros são ligados
        self.memory_buffer = b""
        self.loaded_files = []

        # Barra superior com botões
        top = tk.Frame(root, bg="black")
        top.pack(fill="x", pady=5)

        btn_style = {
            "bg": "white",
            "fg": "black",
            "activebackground": "#dddddd",
            "activeforeground": "black",
            "relief": "flat",
            "width": 10
        }

        tk.Button(top, text="OPEN", command=self.open_files, **btn_style).pack(side="left", padx=5)
        tk.Button(top, text="SAVE", command=self.save_file, **btn_style).pack(side="left", padx=5)
        tk.Button(top, text="CLEAR", command=self.clear_memory, **btn_style).pack(side="left", padx=5)

        # Área de texto (preview/debug)
        self.text = ScrolledText(
            root,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Consolas", 10)
        )
        self.text.pack(fill="both", expand=True, padx=5, pady=5)

        self.log("linux Builder startup.\n")

    def log(self, msg):
        self.text.insert("end", msg)
        self.text.see("end")

    def open_files(self):
        paths = filedialog.askopenfilenames(
            title="open files ",
            filetypes=[("elf files", "*"), ("All files", "*")]
        )
        if 0==0:
                os.system("mkdir /tmp/root 2> /dev/null")
                os.system('printf "y\n" | rm /tmp/root/* 2> /dev/null')
                os.system('printf "y\n" | rm /tmp/root/*.* 2> /dev/null')
               
                
        if not paths:
            return

        for path in paths:
            #try:
            if 0==0:
                os.system("cp $1 /tmp/root/ ".replace("$1",path))
                
                self.log(f"[OK] Carregado: {path} \n")
            #except Exception as e:
            #    self.log(f"[ERRO] {path}: {e}\n")
        
        

    def save_file(self):
        

        path = filedialog.asksaveasfilename(
            title="save disk",
            defaultextension=".iso",
            filetypes=[("iso", "*.iso"), ("All files", "*")]
        )

        if not path:
            return

        try:
            os.system('cp isolinux.bin /tmp/root 2> /dev/null')
            os.system('cp isolinux.cfg /tmp/root 2> /dev/null')
            os.system('cp vmlinuz /tmp/root 2> /dev/null')
            os.system('cp initrd.gz /tmp/root 2> /dev/null')
            
            os.system('chmod 777 /tmp/root/*')
            

            ss='genisoimage -o $1 -input-charset utf-8 -b "isolinux.bin" -no-emul-boot -boot-load-size 4  -boot-info-table "/tmp/root" '.replace("$1",path)
            print(ss)
            os.system(ss)

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def clear_memory(self):
        self.memory_buffer=""
        self.loaded_files.clear()
        self.text.delete("1.0", "end")
        self.log("memory clear.\n")
        if 0==0:
                os.system("mkdir /tmp/root 2> /dev/null")
                os.system('printf "y\n" | rm /tmp/root/* 2> /dev/null')
                os.system('printf "y\n" | rm /tmp/root/*.* 2> /dev/null')



if __name__ == "__main__":
    root = tk.Tk()
    app = RamDiskBuilderGUI(root)
    root.mainloop()

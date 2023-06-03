from tkinter import ttk

def apply_style():
    style = ttk.Style()

    # Appliquer un style pour les boutons
    style.configure('TButton', 
                    font=('calibri', 10, 'bold'),
                    foreground='black')

    # Appliquer un style pour les tableaux
    style.configure('Treeview', 
                    rowheight=25,
                    background='white',
                    fieldbackground='white')
                    
    # Appliquer un style pour les en-têtes de tableaux
    style.configure('Treeview.Heading', 
                    font=('calibri', 11, 'bold'),
                    foreground='black')

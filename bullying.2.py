import tkinter as tk 

victimas = []
testigos = []

ventana = tk.Tk()
ventana.title("Registro")
ventana.geometry("400x300")

def limpiar():
  for widget in ventana.winfo_children():
    widget.destroy()
    
def menu():
 limpiar()
 tk.Label(ventana, text="Selecciona una opcion").pack(pady=10)
 tk.Button(ventana, text="Victima", command=victima).pack(pady=5)
 tk.Button(ventana, text="Testigo", command=testigo).pack(pady=5)
 tk.Button(ventana, text="Archivo", command=archivos).pack(pady=5)
 tk.Button(ventana, text="Salir", command=ventana.destroy).pack(pady=5)
  
def victima():
  limpiar()
  tk.Label(ventana, text="Victima").pack()
  tk.Label(ventana, text="Nombre: (puede ser anonimo)").pack()
  entry_nombre = tk.Entry(ventana)
  entry_nombre.pack()
  
  tk.Label(ventana, text="Lugar de la escuela: ").pack()
  entry_lugar = tk.Entry(ventana)
  entry_lugar.pack()
  
  tk.Label(ventana, text="Tipo de bullying: ").pack()
  entry_tipo = tk.Entry(ventana)
  entry_tipo.pack()

  tk.Label(ventana, text="Si sabe el grupo de el/la agresor/a ingreselo: ").pack()
  entry_grupo = tk.Entry(ventana)
  entry_grupo.pack()
  
  def guardar():
    victimas.append([
      entry_nombre.get(),
      entry_lugar.get(),
      entry_tipo.get(),
      entry_grupo.get()
    ])
    menu()
    
  tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
  tk.Button(ventana, text="Menu", command=menu).pack()
  
def testigo():
  limpiar()
  tk.Label(ventana, text="Testigo").pack()
  tk.Label(ventana, text="Lugar de la escuela: ").pack()
  entry_lugar = tk.Entry(ventana)
  entry_lugar.pack()
  
  tk.Label(ventana, text="Tipo de bullying: ").pack()
  entry_tipo = tk.Entry(ventana)
  entry_tipo.pack()
  
  tk.Label(ventana, text="Intervino? si/no: ").pack()
  entry_intervino = tk.Entry(ventana)
  entry_intervino.pack()

  tk.Label(ventana, text="Si sabe el grupo de el/la agresor/a ingreselo: ").pack()
  entry_grupo = tk.Entry(ventana)
  entry_grupo.pack()
  
  def guardar():
    testigos.append([
      entry_lugar.get(),
      entry_tipo.get(),
      entry_intervino.get(),
      entry_grupo.get()
    ])
    menu()
    
  
  tk.Button(ventana, text="Guardar", command=guardar).pack(pady=5)
  tk.Button(ventana, text="Menu", command=menu).pack()
  
def archivos(): 
  limpiar()
  tk.Label(ventana, text="Archivo").pack()
  
  texto = tk.Text(ventana, height=12, width=45)
  texto.pack()
  
  texto.insert(tk.END, "===VICTIMAS===\n")
  for v in victimas:
    texto.insert(tk.END, f"Nombre: {v[0]}, Lugar: {v[1]}, Tipo: {v[2]}, Grupo: {v[3]}\n")
    
  texto.insert(tk.END, "===TESTIGOS===\n")
  for t in testigos:
    texto.insert(tk.END, f"Lugar: {t[0]}, Tipo: {t[1]}, Intervino: {t[2]}, Grupo: {t[3]}\n")
    
  tk.Button(ventana, text="Menu", command=menu).pack()
  
menu()
ventana.mainloop()

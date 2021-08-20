import tkinter as tk 


class Calculadora:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("375x467")
		self.root.resizable(0,0)
		self.root.title("CalculadoraPy")
		self.total = ""
		self.exp = ""
		self.frame = self.displayFrame()

		self.totaltxt,  self.exptxt = self.textoFrame()
		self.bts = {
			7: (1,1), 8: (1,2), 9: (1,3),
			4: (2,1), 5: (2,2), 6: (2,3),
			1: (3,1), 2: (3,2), 3: (3,3),
			0: (4,1), '.': (4,3)
		}
		self.ops = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+" }

		self.botoesFrame = self.displayBtnFrame()

		for x in range(1,5):
			self.botoesFrame.rowconfigure(x,weight=1)
			self.botoesFrame.columnconfigure(x,weight=1)


		self.makeBtns()
		self.btnsCalc()
		self.spcBtns()

		self.Teclas()




	def addToVal(self, val):
		self.exp += str(val)
		self.updateVal()

	def updateTotalVal(self):
		expressao = self.total
		for op, simbolo in self.ops.items():
			expressao = expressao.replace(op, f'{simbolo}')

		self.totaltxt.config(text=expressao)


	def updateVal(self):
		self.exptxt.config(text=self.exp[:11])

	def addCalc(self, calc):
		self.exp += calc
		self.total += self.exp
		self.exp = ""
		self.updateVal()
		self.updateTotalVal()


	def btnsCalc(self): 

		x = 0
		for op, simbolo in self.ops.items():
			opBtn= tk.Button(self.botoesFrame, text=simbolo, font=("Arial", 20),bg="#F8FAFF", fg="#151515",borderwidth=0, command=lambda x=op: self.addCalc(x))
			opBtn.grid(row=x, column=4, sticky=tk.NSEW)
			x += 1


	
	def spcBtns(self):
		self.apagar()
		self.resultado()
		self.raiz()
		self.raizQ()
		self.retroceder()
		self.makeZero()
		self.mudarSinal()

	def apagar(self):


		for op, simbolo in self.ops.items():
			clearBtn= tk.Button(self.botoesFrame, text="CE", font=("Arial", 14),bg="#F8FAFF", fg="#151515",borderwidth=0, command=self.apagarFcn)
			clearBtn.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)

	def apagarFcn(self):
		self.exp =""
		self.total = ""
		self.updateTotalVal()
		self.updateVal()
		
	def resultado(self):


		for op, simbolo in self.ops.items():
			clearBtn= tk.Button(self.botoesFrame, text="=", font=("Arial", 20),bg="#CCEDFF", fg="#151515",borderwidth=0,command=self.resultadoFcn)
			clearBtn.grid(row=4, column=4, rowspan=2, sticky=tk.NSEW)


	def sinal(self):
		if eval(self.exp) > 0:
			self.exp = "-"+self.exp
			self.updateVal()

		else:
			self.exp = self.exp[1:]
			self.updateVal()
			
	def mudarSinal(self):


		for op, simbolo in self.ops.items():
			clearBtn= tk.Button(self.botoesFrame, text="- / +", font=("Arial", 16),bg="#FFF", fg="#151515",borderwidth=0,command=self.sinal)
			clearBtn.grid(row=1, column=3, sticky=tk.NSEW)

	def retrocederFn(self):
		self.exp = self.exp[:-1]
		self.updateVal()
		self.updateTotalVal()

	def retroceder(self):


		for op, simbolo in self.ops.items():
			clearBtn= tk.Button(self.botoesFrame, text="C", font=("Arial", 14),bg="#FFF", fg="#151515",borderwidth=0,command=self.retrocederFn)
			clearBtn.grid(row=1, column=2, columnspan=1, sticky=tk.NSEW)


	def sqrRoot(self):
		self.exp = str(eval(f"{self.exp}**0.5"))
		self.updateVal()

	def raizQ(self):


		for op, simbolo in self.ops.items():
			clearBtn= tk.Button(self.botoesFrame, text="\u221ax", font=("Arial", 20),bg="#fff", fg="#151515",borderwidth=0,command=self.sqrRoot)
			clearBtn.grid(row=0, column=3, sticky=tk.NSEW)


	def raizQfc(self):
		self.exp = str(eval(f"{self.exp}**2"))
		self.updateVal()

	def raiz(self):


		for op, simbolo in self.ops.items():
			clearBtn= tk.Button(self.botoesFrame, text="x\u00b2", font=("Arial", 20),bg="#fff", fg="#151515",borderwidth=0,command=self.raizQfc)
			clearBtn.grid(row=0, column=2, sticky=tk.NSEW)

	def resultadoFcn(self):
		self.total += self.exp
		self.updateTotalVal()
		try:
			self.exp = str(eval(self.total))

			self.total = ""
		except Exception as erro:
			self.exp = "Erro"

		self.updateVal()


	def Teclas(self):
		self.root.bind("<Return>", lambda event: self.resultadoFcn())
		self.root.bind("<BackSpace>", lambda event: self.retrocederFn())
		self.root.bind("<Escape>", lambda event: self.apagarFcn())

		for tecla in self.bts:
			self.root.bind(str(tecla), lambda event, digito=tecla: self.addToVal(digito))

		for tecla in self.ops:
			self.root.bind(tecla, lambda event, digito=tecla: self.addCalc(digito))


			

	def textoFrame(self):
		total = tk.Label(self.frame ,text=self.total, anchor=tk.E, bg="#F5F5F5",fg="#151515",padx=24,font=("Arial", 16))
		total.pack(expand=True, fill="both")

		texto = tk.Label(self.frame ,text=self.exp, anchor=tk.E, bg="#F5F5F5",fg="#151515",padx=24,font=("Arial", 40, "bold"))
		texto.pack(expand=True, fill="both")

		return total, texto

	def displayFrame(self):
		dframe = tk.Frame(self.root, height=221,bg="#F5F5F5")
		dframe.pack(expand=True, fill="both")
		return dframe

	def displayBtnFrame(self):
		bframe = tk.Frame(self.root)
		bframe.pack(expand=True, fill="both")
		return bframe

	def makeBtns(self):
		for btn,gridindex in self.bts.items():
			btns = tk.Button(self.botoesFrame, text=str(btn),bg="#FFFFFF", fg="#222222", font=("Arial", 18),borderwidth=0, command= lambda x=btn: self.addToVal(x))
			btns.grid(row=gridindex[0]+1, column=gridindex[1],sticky=tk.NSEW)


	def makeZero(self):
			btns = tk.Button(self.botoesFrame, text=str('0'),bg="#FFFFFF", fg="#222222", font=("Arial", 18),borderwidth=0, command= lambda : self.addToVal('0'))
			btns.grid(row=5, column=1, columnspan=2,sticky=tk.NSEW)



	def run(self):
		self.root.mainloop()

if __name__ == "__main__":
	calc = Calculadora()
	calc.run()
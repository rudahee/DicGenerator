import itertools
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as FileDialog


class App():

	def __init__(self):
		
		# Creating Windows and Frames
		self.window = tk.Tk()
		self.window.title = "Dictionary Generator"

		main_frame = tk.Frame(self.window)
		main_frame.grid(row=0, column=0, padx=5, pady=5)

		basic_options_frame = tk.Frame(main_frame)
		basic_options_frame.grid(row=0, column=0, padx=5, pady=5)

		dic_options_frame = tk.Frame(main_frame)
		dic_options_frame.grid(row=1, column=0, padx=5, pady=5)

		# Path, name and extension widgets
		path_label = tk.Label(basic_options_frame, text="Path")
		path_label.grid(row=0, column=0)

		path_entry = tk.Entry(basic_options_frame)
		path_entry.grid(row=0, column=1)

		label_name_output = tk.Label(basic_options_frame, text="Filename")
		label_name_output.grid(row=1, column=0)

		entry_name_output = tk.Entry(basic_options_frame)
		entry_name_output.grid(row=1, column=1)

		button_name_output = tk.Button(basic_options_frame, text="Search path", command=self.selectPath)
		button_name_output.grid(row=0, column=2)

		label_extension = tk.Label(basic_options_frame, text="Extension")
		label_extension.grid(row=2, column=0)

		combobox_extension = ttk.Combobox(basic_options_frame, state="readonly")
		combobox_extension.grid(row=2, column=1)
		combobox_extension["values"] = ["*.txt","*.dic","*.lst","no extension"]

		# Type of dict: Predefined
		self.dict_option = tk.IntVar()
		dict_type_radiobutton = tk.Radiobutton(dic_options_frame, text="Predefined", value=1, variable=self.dict_option)
		dict_type_radiobutton.grid(row=0, column=0)

		label_dict_type = tk.Label(dic_options_frame, text="Select predefined dict")
		label_dict_type.grid(row=2, column=0)

		# Dict type 
		combobox_dict_type = ttk.Combobox(dic_options_frame, state="readonly")
		combobox_dict_type.grid(row=2, column=1)
		combobox_dict_type["values"] = ["Pin/Passcode", "Spain number phone", "Movistar password config", "Movistar password network"]

		# Type of dict: Custom
		dict_type_radiobutton = tk.Radiobutton(dic_options_frame, text="Custom", value=2, variable=self.dict_option)
		dict_type_radiobutton.grid(row=3, column=0)
		
		# Lenght of custom dict
		label_length = tk.Label(dic_options_frame, text="Password lenght")
		label_length.grid(row=4, column=0)
		
		entry_lenght = tk.Entry(dic_options_frame)
		entry_lenght.grid(row=4, column=1)

		# Chars of custom dict
		label_allow_chars = tk.Label(dic_options_frame, text="Insert allow characters")
		label_allow_chars.grid(row=5, column=0)

		entry_allow_chars = tk.Entry(dic_options_frame)
		entry_allow_chars.grid(row=6, column=0, columnspan=3)

		# Start button
		button_start = tk.Button(dic_options_frame, text="Start!", command=self.runThread)
		button_start.grid(row=7, column=3)


		self.window.mainloop()

	def selectPath(self):
		# Find the path, if not selected, the output folder is the same where the script is located
		self.ruta = FileDialog.askdirectory(
			initialdir='.',
			title="Open folder")

	def runThread(self):
		
		#Creating a thread, that threat it's generator.
		generating_dic = threading.Thread(target=self.genDic)
		generating_dic.daemon = True
		generating_dic.start()

	def genDic(self, len_password=9, characters="123456", name_out='Dic.txt'):
		
		# Generating a dictionary
		
		txt = open(name_out, 'w')

		for i in itertools.product(list(characters), repeat=len_password):
			txt.write("\n")
			for j in i:			
				txt.write(''.join(str(j)))
			
                #    if opcion == 4:
                #	    txt.write('95573' + ''.join(str(j) for j in i) + '00\n')
		txt.close()


		#Create a window where you are notified that the file was finished generating
		self.finished = tk.Tk()
		self.finished.title = "Finished!"

		main_frame_finished = tk.Frame(self.finished)
		main_frame_finished.grid(row=0, column=0)
		
		label_finished = tk.Label(main_frame_finished, text="Dictionary is finished")
		label_finished.grid(row=0, column=0, padx=5, pady=3)

		button_finished = tk.Button(main_frame_finished, text="Ok!", command=self.finished.destroy)
		button_finished.grid(row=1, column=0, padx=10, pady=3)

		self.finished.mainloop()



if __name__ == "__main__":
	App()

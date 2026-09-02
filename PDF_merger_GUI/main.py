import os
import tkinter as tk
from tkinter import filedialog, messagebox

from pypdf import PdfWriter


class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.selected_pdfs = []

        title = tk.Label(root, text="Select PDF files to merge", font=("Arial", 12, "bold"))
        title.pack(pady=(20, 10))

        self.file_list = tk.Listbox(root, width=60, height=12)
        self.file_list.pack(padx=20, pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add PDFs", width=15, command=self.add_files)
        add_button.grid(row=0, column=0, padx=10)

        clear_button = tk.Button(button_frame, text="Clear", width=15, command=self.clear_files)
        clear_button.grid(row=0, column=1, padx=10)

        merge_button = tk.Button(root, text="Merge PDFs", width=20, height=2, bg="#4CAF50", fg="white", command=self.merge_pdfs)
        merge_button.pack(pady=15)

    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf")],
        )

        if not files:
            return

        for file_path in files:
            if file_path not in self.selected_pdfs:
                self.selected_pdfs.append(file_path)
                self.file_list.insert(tk.END, os.path.basename(file_path))

    def clear_files(self):
        self.selected_pdfs.clear()
        self.file_list.delete(0, tk.END) #tk.end to clear previous list of files

    def merge_pdfs(self):
        if not self.selected_pdfs:
            messagebox.showwarning("No files selected", "Please select at least one PDF file.")
            return

        output_path = filedialog.asksaveasfilename(
            title="Save merged PDF as",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged.pdf",
        )

        if not output_path:
            return

        merger = PdfWriter()

        try:
            for pdf_path in self.selected_pdfs:
                merger.append(pdf_path)

            with open(output_path, "wb") as output_file:
                merger.write(output_file)

            messagebox.showinfo("Success", f"PDFs merged successfully to:\n{output_path}")
        except Exception as exc:
            messagebox.showerror("Merge failed", f"An error occurred while merging the PDFs:\n{exc}")
        finally:
            merger.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = PdfMergerApp(root)
    root.mainloop() #run the GUI loop to keep the application running and responsive to 

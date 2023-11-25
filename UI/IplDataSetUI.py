import tkinter as tk
from tkinter import ttk, filedialog
from Services.IPLDataSetServices import IPLDataSetsServices


class IplDataSetUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("IPL Data Analysis")
        self.geometry("1200x800")

        self.file_path = None
        self.service = IPLDataSetsServices()

        self.analyze_frame = ttk.Frame(self)
        self.analyze_frame.place(relx=0.02, rely=0.02, relwidth=0.45, relheight=1)

        self.options_frame = ttk.Frame(self)
        self.options_frame.place(relx=0.02, rely=0.55, relwidth=0.45, relheight=0.35)

        self.results_frame = ttk.Frame(self)
        self.results_frame.place(relx=0.52, rely=0.02, relwidth=0.45, relheight=1)

        logo = tk.PhotoImage(file="assets/logo.png")
        logo_label = ttk.Label(self.analyze_frame, image=logo)
        logo_label.image = logo
        logo_label.pack(side=tk.TOP)

        select_file_label = ttk.Label(self.analyze_frame, text="Select IPL DataSet File",
                                      font=("poppins", 10, "bold"))
        select_file_label.pack(pady=2)

        select_button = ttk.Button(self.analyze_frame, text="Select File", command=self.select_file)
        select_button.pack(pady=3)

        self.selected_file_label = ttk.Label(self.analyze_frame, text="No file selected", font=("poppins", 10))
        self.selected_file_label.pack(pady=2)

        submit_button = ttk.Button(self.analyze_frame, text="Submit", command=self.submit)
        submit_button.pack(pady=3)

        exit_button = ttk.Button(self.analyze_frame, text="Exit", command=self.quit)
        exit_button.pack(pady=3)

        self.analysis_label = ttk.Label(self.results_frame, text="Analysis Results", font=("Helvetica", 20, "bold"))
        self.analysis_label.pack(pady=10)

        self.result_text = tk.Text(self.results_frame, wrap=tk.WORD, height=20, width=70)
        self.result_text.pack()

        self.hide_options()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xls")])
        if self.file_path:
            file_name = self.file_path.split("/")[-1]
            self.selected_file_label.config(text=f"Selected File: {file_name}")
            self.selected_file_label.pack(pady=2)

    def submit(self):
        if self.file_path is None:
            print("Select File")
        else:
            if self.service.read_csv(self.file_path):
                highest_wicket_taker = self.service.highest_wicket_taker()
                highest_run_scorer = self.service.highest_run_scorer()
                basic_stats = self.service.basic_statistics()

                result_text = (
                    f"\nHighest Wicket Taking Team In THE IPL: {highest_wicket_taker}\n"
                    f"\nHighest Run Scorer Team In THE IPL: {highest_run_scorer}\n"
                    f"\nDescribed Data: {basic_stats}"
                )
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, result_text)

                self.show_options()

    def hide_options(self):
        self.options_frame.pack_forget()

    def show_options(self):
        self.options_buttons_frame = ttk.Frame(self.results_frame)
        self.options_buttons_frame.pack(pady=10)

        matches_played_button = ttk.Button(self.options_buttons_frame, text="Matches Played",
                                           command=self.service.matches_played_analysis)
        matches_played_button.pack(side=tk.LEFT, padx=5)

        titles_won_button = ttk.Button(self.options_buttons_frame, text="Titles Won",
                                       command=self.service.titles_won_analysis)
        titles_won_button.pack(side=tk.LEFT, padx=5)

        net_run_rate_button = ttk.Button(self.options_buttons_frame, text="Net Run Rate",
                                         command=self.service.net_run_rate_analysis)
        net_run_rate_button.pack(side=tk.LEFT, padx=5)

        linear_regression_button = ttk.Button(self.options_buttons_frame, text="Linear Regression",
                                              command=self.service.linear_regression_analysis)
        linear_regression_button.pack(side=tk.LEFT, padx=5)

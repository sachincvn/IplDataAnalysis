import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
from scipy import stats
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt


class IPLDataSetsServices:
    def __init__(self):
        self.data = None

    def read_csv(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            return True
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return False

    def highest_wicket_taker(self):
        return self.data.iloc[self.data['HighestWicketTaker'].idxmax()]

    def highest_run_scorer(self):
        return self.data.iloc[self.data['HighestRunScrorer'].idxmax()]

    def basic_statistics(self):
        return self.data.describe()

    def matches_played_analysis(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='TeamName', y='Gamesplayed', data=self.data)
        plt.title('Number of Matches Played by Each Team')
        plt.xlabel('Team Name')
        plt.ylabel('Number of Matches Played')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def titles_won_analysis(self):
        sorted_data = self.data.sort_values(by='NoOfTitleWons', ascending=False)
        plt.figure(figsize=(10, 6))
        sns.barplot(x='NoOfTitleWons', y='TeamName', data=sorted_data, orient='h')
        plt.title('Number of Titles Won by Each Team')
        plt.xlabel('Number of Titles Won')
        plt.ylabel('Team Name')
        plt.tight_layout()
        plt.show()

    def net_run_rate_analysis(self):
        plt.figure(figsize=(8, 8))
        plt.pie(self.data['NetRunRate'], labels=self.data['TeamName'], autopct='%1.1f%%', startangle=140)
        plt.title('Net Run Rate Distribution Across Teams')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def linear_regression_analysis(self):
        x = self.data['Gamesplayed']
        y = self.data['NetRunRate']
        slope, intercept, r, p, std_err = stats.linregress(x, y)

        def myfunc(x):
            return slope * x + intercept

        mymodel = list(map(myfunc, x))

        plt.scatter(x, y)
        plt.plot(x, mymodel, color='red')
        plt.xlabel('Games Played')
        plt.ylabel('Net Run Rate')
        plt.title('Linear Regression Analysis')
        plt.show()
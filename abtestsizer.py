import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.power import tt_ind_solve_power
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def convert_to_datetime(dataframe, date_column):
    """
    Convert the specified column to a datetime type if not already.

    Args:
        dataframe (pd.DataFrame): The DataFrame.
        date_column (str): The name of the date column.

    Returns:
        pd.DataFrame: The DataFrame with the date column converted to datetime.
    """
    if not pd.api.types.is_datetime64_any_dtype(dataframe[date_column]):
        dataframe[date_column] = pd.to_datetime(dataframe[date_column])
    return dataframe

def calculate_sample_size(dataframe, date_column, user_id_column, baseline_conversion_rate):
    """
    Calculate the sample size for predefined values of alpha, power, and MDE.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing the data. Use imported data. 
        date_column (str): The name of the date column.
        metric_column (str): The name of the metric column.
        baseline_conversion_rate (float): The baseline conversion rate.

    Returns:
        int: The sample size per group.
    """
    alpha_values = [0.05, 0.10]
    power_values = [0.70, 0.80, 0.90]
    mde_values = [0.03, 0.05, 0.10]
    
    dataframe = convert_to_datetime(dataframe, date_column)
    
    users_per_day = dataframe.groupby(date_column)[user_id_column].count()
    users_mean = users_per_day.mean()
    
    for alpha in alpha_values:
        for power in power_values:
            for mde in mde_values:
                p1 = baseline_conversion_rate / 100
                p2 = p1 * (1 + p1 + mde)
                cohen_D = sm.stats.proportion_effectsize(p1, p2)
                n = tt_ind_solve_power(effect_size=cohen_D, power=power, alpha=alpha)
                n = int(round(n, -3))
                total_sample_size = 2 * n
                
                print(f"Alpha: {alpha}, Power: {power}, MDE: {mde}")
                print(f"Sample size per group: {n}")
                print(f"Total sample size for the entire test per group: {total_sample_size}\n")

                ttest_power = TTestIndPower()
                ttest_power.plot_power(dep_var='nobs', nobs=np.arange(1000, 30000, 1000), effect_size=[cohen_D], title='Power Analysis')
                plt.axhline(power, linestyle='--', label='Desired Power', alpha=0.5)
                plt.axvline(n, linestyle='--', color='orange', label='Sample Size', alpha=0.5)
                plt.ylabel('Statistical Power')
                plt.grid(alpha=0.08)
                plt.legend()
                plt.show()
                
                alloc = np.arange(0.10, 1.1, 0.10)
                size = round(visits_mean, -3) * alloc
                days = np.ceil(2 * n / size)
                f, ax = plt.subplots(figsize=(6, 4))
                ax.plot(alloc, days, '-o')
                ax.xaxis.set_major_locator(MultipleLocator(0.1))
                ax.set_title('Days Required Given User Allocation per Day')
                ax.set_ylabel('Experiment Duration in Days')
                ax.set_xlabel('% Users Allocated to the Experiment per Day')
                plt.show()
 
#This project is licensed under the MIT License - see the license.txt file for details.
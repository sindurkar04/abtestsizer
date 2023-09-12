# AB Test Sizer

## Overview

AB Test Sizer is a Python script that calculates the required sample size for A/B tests based on predefined values of significance level (alpha), statistical power (beta), and minimum detectable effect (MDE). It utilizes the `statsmodels` library to perform power analysis for A/B testing.

## Prerequisites

Before using this script, ensure that you have the following Python libraries installed:

- `pandas` for data manipulation
- `numpy` for numerical operations
- `matplotlib` for data visualization
- `statsmodels` for statistical analysis
- `logging` for logging information (optional)

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib statsmodels

Usage
To use the AB Test Sizer script, follow these steps:

Import the necessary libraries at the beginning of your Python script:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import statsmodels.api as sm
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.power import tt_ind_solve_power
import logging

Configure the logging settings (optional):
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
Define your dataset and variables:

dataframe: The DataFrame containing your data. Replace this with your actual dataset.
date_column: The name of the date column in your dataset.
user_id_column: The name of the user ID column in your dataset.
baseline_conversion_rate: The baseline conversion rate for your A/B test.
Use the calculate_sample_size function to calculate the sample size for different combinations of alpha, power, and MDE:


calculate_sample_size(dataframe, date_column, user_id_column, baseline_conversion_rate)
The function will print the calculated sample sizes and display graphs for statistical power analysis and experiment duration.

Customize the predefined values of alpha_values, power_values, and mde_values as needed for your specific analysis.

Example
Here's a simple example of how to use the AB Test Sizer script:

dataframe = pd.DataFrame()  # Replace with your actual data
date_column = "date_column"
user_id_column = "user_id_column"
baseline_conversion_rate = 10.0  # Replace with your baseline conversion rate

calculate_sample_size(dataframe, date_column, user_id_column, baseline_conversion_rate)


Feel free to customize and use this script for your A/B testing sample size calculations.

You can save this markdown content as a `README.md` file in your project repository. Be sure to replace the placeholder values and instructions with your actual dataset and usage details.

This project is licensed under the MIT License - see the license.txt file for details.
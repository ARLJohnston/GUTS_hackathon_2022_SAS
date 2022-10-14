import pandas as pd
import numpy as np

location_data = pd.read_csv("location_data.csv", on_bad_lines='warn')
people_data = pd.read_csv("people_data.csv", on_bad_lines='warn')
security_data = pd.read_csv("security_logs.csv", on_bad_lines='warn')
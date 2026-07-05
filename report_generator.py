"""
Generate CSV test report.
"""

import pandas as pd

def save_results(results):

    df = pd.DataFrame(results)

    df.to_csv("results/test_log.csv", index=False)

    print("CSV report generated successfully.")

# ----------------------------------------------------------
# report_generator.py
# Generates a CSV file containing the test results.
# ----------------------------------------------------------
import pandas as pd
def save_results(test_results):
    """
    Save the test results into a CSV file.
    """
    dataframe = pd.DataFrame(test_results)
    output_file = "results/test_log.csv"
    dataframe.to_csv(output_file, index=False)
    print(f"Results saved successfully in {output_file}")

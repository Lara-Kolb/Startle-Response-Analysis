import pandas as pd
import numpy as np
import sys
import os

def analyze_max_g_values(csv_file_path):
    """
    Analyzes a CSV file to find the maximum 'g' value per experiment
    and calculates the mean of those maximums across repetitions.
    
    Parameters:
    csv_file_path (str): Path to the CSV file to analyze
    
    Returns:
    tuple: (max_values_dict, mean_of_maxes)
    """
    try:
        # Read the CSV file, skipping the first metadata row
        # The header is at row 1 (0-indexed)
        df = pd.read_csv(csv_file_path, skiprows=1)
        
        # Filter out metadata rows (those starting with -130, -120, etc.)
        # Keep only rows where the first column is -900 (actual data rows)
        df = df[df.iloc[:, 0] == -900]
        
        # Convert ValueG to numeric, filtering out any non-numeric values
        df['ValueG'] = pd.to_numeric(df['ValueG'], errors='coerce')
        df = df[df['ValueG'].notna()]
        
        # Create absolute value column for absolute maximum calculation
        df['AbsValueG'] = df['ValueG'].abs()
        
        # Group by Trial (experiment type) and TrialNo (repetition)
        # Find maximum g value (largest value)
        max_values = df.groupby(['Trial', 'TrialNo'])['ValueG'].max()
        
        # Find absolute maximum g value (largest absolute value)
        abs_max_values = df.groupby(['Trial', 'TrialNo'])['AbsValueG'].max()
        
        # Calculate the means
        mean_of_maxes = max_values.mean()
        mean_of_abs_maxes = abs_max_values.mean()
        
        print(f"\n{'='*60}")
        print(f"Analysis of: {csv_file_path}")
        print(f"{'='*60}\n")
        
        print("Maximum ValueG per Experiment Repetition:")
        print("-" * 60)
        for (trial, trial_no), max_val in max_values.items():
            print(f"Trial '{trial}', Repetition {trial_no}: {max_val:.2f} g")
        
        print(f"\n{'='*60}")
        print(f"Mean of Maximum Values: {mean_of_maxes:.4f} g")
        print(f"Total number of experiments: {len(max_values)}")
        print(f"{'='*60}\n")
        
        print("Absolute Maximum ValueG per Experiment Repetition:")
        print("-" * 60)
        for (trial, trial_no), abs_max_val in abs_max_values.items():
            print(f"Trial '{trial}', Repetition {trial_no}: {abs_max_val:.2f} g")
        
        print(f"\n{'='*60}")
        print(f"Mean of Absolute Maximum Values: {mean_of_abs_maxes:.4f} g")
        print(f"Total number of experiments: {len(abs_max_values)}")
        print(f"{'='*60}\n")
        
        return max_values.to_dict(), mean_of_maxes, abs_max_values.to_dict(), mean_of_abs_maxes
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return None, None, None, None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None, None, None, None

def main():
    """
    Main function to run the analysis.
    Can be called from command line with a file path or will prompt for input.
    """
    # Set the CSV file to analyze
    #csv_file = r"c:\Users\1kolb\Desktop\Startle-Response-Analysis\2026\Animal96_January21.CSV"
    csv_file = r"C:\Users\1kolb\Desktop\Startle-Response-Analysis\2022\Animal27_October24.CSV"
    
    # Run the analysis
    max_values_dict, mean_of_maxes, abs_max_values_dict, mean_of_abs_maxes = analyze_max_g_values(csv_file)
    
    if max_values_dict is not None:
        # Automatically save results to a file in the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_filename = os.path.basename(csv_file).replace('.CSV', '_analysis.txt').replace('.csv', '_analysis.txt')
        output_file = os.path.join(script_dir, output_filename)
        with open(output_file, 'w') as f:
            f.write(f"Analysis of: {csv_file}\n")
            f.write("=" * 60 + "\n\n")
            f.write("Maximum ValueG per Experiment Repetition:\n")
            f.write("-" * 60 + "\n")
            for (trial, trial_no), max_val in max_values_dict.items():
                f.write(f"Trial '{trial}', No {trial_no}: {max_val:.2f} g\n")
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Mean of Maximum Values: {mean_of_maxes:.4f} g\n")
            f.write(f"Total number of experiments: {len(max_values_dict)}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("Absolute Maximum ValueG per Experiment Repetition:\n")
            f.write("-" * 60 + "\n")
            for (trial, trial_no), abs_max_val in abs_max_values_dict.items():
                f.write(f"Trial '{trial}', No {trial_no}: {abs_max_val:.2f} g\n")
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Mean of Absolute Maximum Values: {mean_of_abs_maxes:.4f} g\n")
            f.write(f"Total number of experiments: {len(abs_max_values_dict)}\n")
            f.write("=" * 60 + "\n")
        print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()

import pandas as pd

# Function to combine valid and rogue data into a single CSV
def combine_data(valid_file='valid_data.csv', rogue_file='rogue_data.csv', output_file='raw_data.csv'):
    # Reading valid data
    df_valid = pd.read_csv(valid_file)

    # Reading rogue data
    df_rogue = pd.read_csv(rogue_file)

    # Combining both datasets
    df_combined = pd.concat([df_valid, df_rogue], ignore_index=True)

    # Save to CSV
    df_combined.to_csv(output_file, index=False)
    print(f"Combined data saved to {output_file}")





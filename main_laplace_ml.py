import argparse
import os
import logging
from data_processor_ml import process_file_laplace_ml
from noise_generation import generate_laplace_noise_samples
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process data files with Planar Laplace Mechanism.')
    parser.add_argument('--input_dir', required=True, help='Directory containing input CSV files.')
    parser.add_argument('--output_dir', required=True, help='Directory to save output CSV files.')
    parser.add_argument('--iteration', required=True, help='Directory to save output CSV files.')

    return parser.parse_args()

def main_laplace_ml():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    args = parse_arguments()

    base_directory_input = args.input_dir
    base_directory_output = args.output_dir
    num_iterations_ml = int(args.iteration)
    
    noise_directory = r"C:\Users\ss6365\Desktop\VisualCodeImplementation\noise_laplace"
    
    # Check if the input directory exists and is a directory
    if not os.path.isdir(base_directory_input):
        logging.error("Input directory does not exist or is not a directory.")
        raise ValueError("Input directory does not exist or is not a directory.")
    
    # Check if the input directory contains at least one CSV file
    if not any(file.endswith('.csv') for file in os.listdir(base_directory_input)):
        logging.error("Input directory does not contain any CSV files.")
        raise ValueError("Input directory does not contain any CSV files.")
    
    # Ensure output directory exists
    os.makedirs(base_directory_output, exist_ok=True)
    
    epsilon_values = [0.1, 1, 5]
    
    for epsilon in epsilon_values:

        noise_laplace = load_noise_samples(epsilon, noise_directory)
        
        for file_name in os.listdir(base_directory_input):
            if file_name.endswith('.csv'):
                file_path = os.path.join(base_directory_input, file_name)
                process_file_laplace_ml(file_path, epsilon, base_directory_output, noise_laplace,num_iterations_ml)

def load_noise_samples(epsilon, noise_dir):
    """Load noise samples for a given epsilon from a file."""
    file_path = os.path.join(noise_dir, f"laplace_noise_epsilon_{epsilon}.json")
    with open(file_path, 'r') as file:
        samples = json.load(file)
    return samples



if __name__ == '__main__':
    main_laplace_ml()

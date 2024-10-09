import os
from PIL import Image

def get_input():
    while True:
        file_path = input("Enter the path to the JPEG file: ")
        if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg')):
            return file_path
        else:
            print("Invalid file path or not a JPEG file. Please try again.")

def check_file_format(file_path):
    try:
        with Image.open(file_path) as img:
            if img.format.upper() not in ['JPEG', 'JPG']:
                raise ValueError("The input file is not in JPEG format.")
    except IOError:
        raise ValueError("Unable to open the file. It may be corrupted or not an image file.")

def convert_to_png(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'PNG')

def main():
    print("JPEG to PNG Converter")
    
    # Get input
    input_file = get_input()
    
    try:
        # Check file format
        check_file_format(input_file)
        
        # Generate output file name
        output_file = os.path.splitext(input_file)[0] + '.png'
        
        # Convert to PNG format and save
        print("Converting JPEG to PNG...")
        convert_to_png(input_file, output_file)
        
        # Output
        print(f"Conversion complete. PNG file saved as: {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

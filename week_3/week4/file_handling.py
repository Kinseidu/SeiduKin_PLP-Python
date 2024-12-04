def read_and_modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its contents, and writes the modified version to a new file.

    :param input_filename: str, the name of the input file to read from.
    :param output_filename: str, the name of the output file to write to.
    """
    try:
        # Open and read the input file
        with open(input_filename, 'r') as infile:
            contents = infile.readlines()
        
        # Modify the contents (example: convert to uppercase)
        modified_contents = [line.upper() for line in contents]

        # Write the modified contents to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_contents)
        
        print(f"File '{input_filename}' has been read and modified content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename and try again.")
    except IOError as e:
        print(f"Error: Unable to read or write files. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for input and output filenames
    input_filename = input("Enter the name of the file to read from: ")
    output_filename = input("Enter the name of the file to write to: ")

    # Call the read_and_modify_file function
    read_and_modify_file(input_filename, output_filename)


if __name__ == "__main__":
    main()

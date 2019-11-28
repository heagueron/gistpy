def countAll(text):
    # your code here


    # Program must use the return statement
    # return type should be a dictionary
    return 


###################################################
# DO NOT MODIFY CODE BELOW THIS LINE
def main():
    input_file_name = input("Input filename: ")
    file_Handle = open(input_file_name, 'r')
    output_file = open("out_"+input_file_name, 'w')
    lines = file_Handle.readlines()

    for line in lines:
        sample_dict = countAll(line)
        output_file.write(str(sample_dict) + '\n')
    output_file.close()
    file_Handle.close()

if __name__ == "__main__":
    main()

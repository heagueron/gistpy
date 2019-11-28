def check_inventory(inventory, low=5):
    # your code here


    # Program must use the return statement
    # return type must be a list in order to get grades
    
    return 


###################################################
# DO NOT MODIFY CODE BELOW THIS LINE
import ast


def main():
    input_file_name = input("Input filename: ")
    file_handle = open(input_file_name, 'r')
    output_file = open("out_" + input_file_name, 'w')
    lines = file_handle.readlines()

    for line in lines:
        line = line.split(',')
        # print(line)
        if int(line[-1]) == 0:
            #            dict_ = ast.literal_eval(str(','.join(line[:-1])))
            #            #print(dict_)
            #            #print()
            output_file.write(str(check_inventory(ast.literal_eval(','.join(line[:-1])))) + '\n')
        else:
            output_file.write(str(check_inventory(ast.literal_eval(','.join(line[:-1])), int(line[-1]))) + '\n')

    output_file.close()
    file_handle.close()

if __name__ == "__main__":
    main()

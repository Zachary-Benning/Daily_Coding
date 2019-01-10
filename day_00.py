# Given a string and a set of delimiters, reverse the words in the string while maintaining
#     the relative order of the delimiters.
#     For example, given "hello/world:here", return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases:
#     "hello/world:here/", "hello//world:here"

#################################### BACKGROUND ###############################################
# A delimiter is a sequence of one or more characters used to specify the boundary between separate,
# independent regions in plain text or other data streams.[1] An example of a delimiter is the
# comma character, which acts as a field delimiter in a sequence of comma-separated values.

# IN OTHER WORDS: delimiters can theoretically be any symbol predefined but generally are non-alpha
# non-numeric symbols.
################################################################################################

##################################### Idea #####################################################
# We are going to predefine a set of delimiters.
# Go through string letter by letter adding to a string then once we have reached a delimiter
# append the string to a list then append the delimiter and continue on
# Special case exists when two delimiters are adjacent, but should be trivial to handle.
################################################################################################

######################################### CODE SPACE ###########################################
# Predefined Delimiter set hard coded
#       - We could allow input to set these but for the purpose of this exercise and testing we
#           will begin with a hard coded delimiter set.
delimiter_set = ['/',':']
# Predefined Testing_string set hardcoded for the same purposes as the delimiter set
testing_string = 'hello/world:here:'

def string_parse_function(input_string, input_delimiter_set):
    # Our output list
    output = []
    # used to hold the current running string
    temp_buffer = ''
    delimiter_flag = 0
    # Iterating through each element in the input_string
    for x in range(len(input_string)):
        # Iterating through each element in the input_delimiter_set
        for y in range(len(input_delimiter_set)):
            # Checking if the current element is a delimiter
            if input_string[x] == input_delimiter_set[y]:
                delimiter_flag = 1
                # Pushing the previous string to the output list
                output.append(temp_buffer)
                # pushing the current delimiter to output list
                output.append(input_string[x])
                # resetting the temp_string
                temp_buffer = ''

            #non-delimiter
        if delimiter_flag != 1:
            temp_buffer += input_string[x]
        delimiter_flag = 0
    return output

# Flip function to flip
def reverse_words(parsed_string):
    output = [''] * len(parsed_string)
    for x in range(len(parsed_string)):
        if x % 2 == 0:
            output[(len(parsed_string) - 1) - x] = parsed_string[x]
        else:
            output[x] = parsed_string[x]
    return output
print(reverse_words(string_parse_function(testing_string, delimiter_set)))

################################################################################################

################################# SCRATCH BUFFER ###############################################
# test = [1,2,3,4,5]
# output = [0] * len(test)
# for x in range(len(test)):
#     if x % 2 == 0:
#         output[(len(test)-1) - x] = test[x]
#     else:
#         output[x] = test[x]
# print(output)
#.append adds to end
#.pop removes
#
# x = [1,2,3]
# y = x.pop(0)
# print(y)
# y = x.pop(0)
# print(y)
################################# SCRATCH BUFFER ###############################################


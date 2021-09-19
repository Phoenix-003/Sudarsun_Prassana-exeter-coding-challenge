class GlobalMembers(object):
    buff = str(['\0' for _ in range(DefineConstants.BUFFER_SIZE)])
    fPtr = None
    fTemp = None


    @staticmethod
    def main():



        str = ["" for _ in range(1000)]
        str1 = ["" for _ in range(1000)]





        oldWord = None
        newWord = None

        fp = fopen("french_dictionary.csv","r")

        fPtr = fopen("t8.shakespeare.txt", "r")
        fTemp = fopen("replace.txt", "w")

        if fPtr is None or fTemp is None:
            # Unable to open file hence exit 
            print("\nUnable to open file.\n", end = '')
            print("Please check whether file exists and you have read/write privilege.\n", end = '')
            sys.exit(0)



        if fp == None:
            print("error occured", end = '')
            return 0
        else:
            buffer = str(['\0' for _ in range(1024)])

            row = 0
            column = 0
            i = 0
            j = 0

            while fgets(buffer, 1024, fp):
                column = 0
                row += 1
                i = 0
                j = 0
                # To avoid printing of column
                # names in file can be changed
                # according to need
                if row == 1:
                    continue

                # Splitting the data
                value = strtok(buffer, ", ")
                r = None
                for r in range(0, 1000):

                    while value != '\0':
                        # Column 1+-*

                        if column == 0:

                            str[i] = value

                            oldWord = str[i]





                        # Column 2
                        if column == 1:

                            str1[j] = value

                            newWord = str1[j]








                        if oldWord!=None and newWord!=None:
                        temp_ref_oldWord = RefObject(oldWord);
                        temp_ref_newWord = RefObject(newWord);
                            replica(temp_ref_oldWord, temp_ref_newWord)
                            newWord = temp_ref_newWord.arg_value
                            oldWord = temp_ref_oldWord.arg_value
                            oldWord = None
                            newWord = None


                        i += 1
                        j += 1
                        value = strtok(None, ", ")
                        column += 1




                print("\n", end = '')








            fclose(fp)




    @staticmethod
    def replica(self, oldWord, newWord):


        while (fgets(buff, DefineConstants.BUFFER_SIZE, fPtr)) != None:
            # Replace all occurrence of word from current line
        temp_ref_buff = RefObject(buff);
            replaceAll(temp_ref_buff, oldWord.arg_value, newWord.arg_value)
            buff = temp_ref_buff.arg_value

            # After replacing write it to temp file.
            fputs(buff, fTemp)


        fclose(fPtr)
        fclose(fTemp)


        # Delete original source file 
        remove("t8.shakespeare.txt")

        # Rename temp file as original file 
        rename("replace.tmp", "t8.shakespeare.txt")

        print("\nSuccessfully replaced all occurrences of '{0}' with '{1}'.".format(oldWord.arg_value, newWord.arg_value), end = '')

        return 0












    @staticmethod
    def replaceAll(self, str, oldWord, newWord):
        pos = None
        temp = str(['\0' for _ in range(DefineConstants.BUFFER_SIZE)])
        index = 0
        owlen = None

        owlen = len(oldWord)

        if not strcmp(oldWord, newWord):
            return

        while (pos = strstr(str.arg_value, oldWord)) != None:
            # Backup current line
            temp = str.arg_value

            # Index of current found word
            index = pos - str.arg_value

            # Terminate str after word found index
            str.arg_value[index] = '\0'

           
            str.arg_value = str.arg_value + newWord

            str.arg_value = str.arg_value + temp[index:] + owlen

    # Close the file

class DefineConstants(object):
    BUFFER_SIZE = 1000


class RefObject(object):
    def __init__(self, ref_arg):
        arg_value = ref_arg

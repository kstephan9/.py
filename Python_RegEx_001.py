import re, sys, os

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

'''

sentence = 'Start a sentenc e and then bring it to an end.'

def main():

    pattern = re.compile(r'abc')

    matches = pattern.finditer(text_to_search)

    for amatch in matches:
        print(amatch)


if __name__ == "__main__":
#    if not len(sys.argv) == 3:
#        print("Usage: {} input_file output_file".format(sys.argv[0]))

#    main("ken_infile.txt", "ken_outfile.txt")
    main()
    print("Finished!")

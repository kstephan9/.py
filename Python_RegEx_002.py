import re, sys, os

NameAge = """
Janice is 23 and Theon is 33
Gabriel is 44 and Joey is 21
"""


def main(infilename, outfilename):


    ages = re.findall(r'\d{1,3}', NameAge)
    names = re.findall(r'[A-Z][a-z]*', NameAge)

    ageDict = {}
    x = 0

    for eachname in names:
        ageDict[eachname] = ages[x]
        x+= 1

    #print("ages: ", ages)
    #print("ageDict: ", ageDict)


    str = " we need to inform him of the latest information "
    if re.search("inform", str):
        print("There is inform")

    #
    # findall finds all occurances
    #
    allinform = re.findall("inform", str )

    print("allinform: ", allinform)

    for i in allinform:
        print(i)

    #
    # Define an iterator
    #

    for i in re.finditer("inform", str):
        locTuple = i.span()

        #print("locTuple: "+locTuple.str)
        print(locTuple)

    #
    # Match words to a particular pattern
    #
    str = "Sat, hat, mat, pat, at"

    allStr = re.findall("[shmp]at", str)
    for i in allStr:
        print(i)

    #
    # Match series of range of characters
    #
    str = "Sat, hat, mat, pat, at"

    print("\n")
    someStr = re.findall("[h-m]at", str)
    for i in someStr:
        print(i)

    #
    # Exclude match series of range of characters
    #
    str = "Sat, hat, mat, pat, at"

    print("\n")
    someStr = re.findall("[^h-m]at", str)
    for i in someStr:
        print(i)

    #
    # Replace a string
    #
    Food = "hat rat mat pat"

    print("\n")
    my_regex = re.compile("[r]at")

    Food = my_regex.sub("food", Food)

    print(Food)

    #
    # Match a single character
    #
    randstr = "12345"

    print("\n")

    print("Matches: ", len(re.findall("\d{5}", randstr)))

    #
    # Match a single character
    #
    randstr = '''
    Keep the blue flag
    flying high
    Chelsea
    '''

    print("\n")

    print("randstr: ", randstr)
    my_regex = re.compile("\n")
    randstr = my_regex.sub(" ", randstr)
    print("randstr: ", randstr)

    #
    # Match sequences of characters
    #
    num = "123 1234 12345 123456 1234567"

    print("120: ", len(re.findall("\d{5,7}", num)))

    phn = "412-555-1212"
    if re.search("\w{3}-\w{3}-\w{4}", phn):
        print(phn)

    #
    # Match name and spaces
    #
    if re.search("\w{2,20}\s\w{2,20}","Saurabh kuls"):
        print("130: yes")

    #
    #
    #

    email = '''
    sk@aol.com md@.com @sao.com   dc@.com  sk@aol.com
    CoreyMSchafer@gmail.com
    corey.schafer@university.edu
    corey-321-schafer@my-work.net
    '''

    email_pattern = re.compile(r'[a-zA-Z.\-]+@[a-zA-Z-]+\.(com|edu|net)')
    print("EmailMatches1: ", len(re.findall("[\w._%+-]{1,20}@.[\w.-]{2,20}.[A-Za-z]{2,3}", email)))
    print("EmailMatches2: ", len(re.findall(email_pattern, email)))

    mymatches = email_pattern.finditer(email)

    for mm in mymatches:
        print(mm)

    urls= '''
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    '''

    urlpattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

    sub_urls = urlpattern.sub(r'\2\3', urls)

    print("sub_urls: ", sub_urls)

    mymatches = urlpattern.finditer(urls)
    for match in mymatches:
        print("urlmatches-group(0): ", match.group(0)
            , "\nurlmatches-group(1): ",  match.group(1)
            , "\nurlmatches-group(2): ", match.group(2)
            , "\nurlmatches-group(3): ", match.group(3))




if __name__ == "__main__":
#    if not len(sys.argv) == 3:
#        print("Usage: {} input_file output_file".format(sys.argv[0]))

    main("ken_infile.txt", "ken_outfile.txt")
    print("Finished!")

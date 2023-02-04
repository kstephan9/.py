import re, sys, os

text = """BLANCH, I've got
STELLA: Blanch, live!
BLANCHE: Stella, oh, Stella, Stella! Stella for Star
BLANCHE: Now, then, let me look at you. NickAndNora
STANLEY: Why, that you had to live in these conditions, BLANCHE
BLANCHE: I'm tired.
STELLA: Blanche, live!
abc
live
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
"""

with open("ken_infile.txt", 'w') as out:
    out.write(text)



def main(infilename, outfilename):

    if not os.path.exists(infilename):
        print("ERROR: Input file does not exist!")
        sys.exit()

    with open(infilename,'r') as infile:
        lines = infile.readlines()

    pattern = re.compile(r"^(.+ +.+)$")
    pattern2 = re.compile(r"(NickAndNora)")
    pattern3 = re.compile(r'[A-Z][a-z]*')

    with open(outfilename, 'w') as outfile:
        for line in lines:
            mymatch = re.match(pattern, line)
            if mymatch:
                my_newline = re.sub(pattern, r'"\g<1>"', line)
                outfile.write("mymatch1: "+my_newline)
                print("mymatch1: "+my_newline)
            else:
                outfile.write("line 42: "+line)

            mymatch2 = re.search(pattern2, line)
            #print(pattern2)
            if mymatch2:
                my_newline = re.sub(pattern2, r'abcdef\g<1>ghijkl', line)
                outfile.write("mymatch2: "+my_newline)
                print("mymatch2: "+my_newline)
            else:
                outfile.write("line 51: "+line)

            mymatch3 = re.search(pattern3, line)
            if mymatch3:
                my_newline = re.sub(pattern3, r'pattern3\g<0>pattern3', line)
                outfile.write("mymatch3: "+my_newline)
                print("mymatch3: "+my_newline)
            else:
                outfile.write("line 59: "+line)



def main1():

    countStella = 0
    stellaSays = False

    lines = text.splitlines()
    for line in lines:
#        if re.match("BLANCHE", line): # returns only lines that begin with "BLANCHE"
        if re.search("(BLANCHE|abc)", line): # returns only lines that begin with "BLANCHE"
            print("line 72: "+line.strip())
        if line.find("live") != -1:
            if line.find("STELLA:") !=  -1:
                stellaSays = True
                countStella = countStella + 1

    print(countStella, stellaSays)

if __name__ == "__main__":
#    if not len(sys.argv) == 3:
#        print("Usage: {} input_file output_file".format(sys.argv[0]))

    main("ken_infile.txt", "ken_outfile.txt")
    print("Finished!")

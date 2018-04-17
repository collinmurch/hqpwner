# # # # # # # # # # # # # # # # # # # # # # # # #
# Written by Collin Murch. Assumes OS is MacOS. #
# # # # # # # # # # # # # # # # # # # # # # # # #

import subprocess, sys, urllib.request, urllib.parse, json

# Grab stored tokens from JSON file (for ease of Github use)
try:
    tokens=json.load(open('tokens.json'))
    key=tokens["key"]
    cx=tokens["cx"]
except:
    print("Error parsing tokens.json. Does it exist?")

# Warn user if they haven't updated their file with the correct tokens
if key is '' or cx is '':
    print("Please update tokens.json.")
    sys.exit()

# Applying Google custom search API tokens or default search
gURI='https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=' %(key, cx)
google='https://www.google.com/search?q='

# Default screen capture path
picPath='./capture.png'

# Open google to the question page using user's default browser
def googler(query, q, a):
    subprocess.Popen(['open',google+query])

# Outputs amount of instances of each answer in results
def scanner(query, q, a):
    
    # Each count item corresponds to an answer (a[0]: counter[0], etc.)
    count=[0]*3

    # Grab results from custom search engine
    try:
        r=urllib.request.urlopen(gURI+query).read()
    except:
        print("Could not access URL.")
        sys.exit()

    # Split massive string using the answer as a delimeter
    # Instances will be one less than the array length
    for i in range(0, len(a)):
        # Split by words
        words = a[i].split(' ')

        # Use last word of answer if multiple words, or use first if second word is shared
        try:
            deli=words[-1].lower()
            if deli in a[i-1].lower() or deli in a[i-2].lower() or deli in q.lower():
                deli=words[0].lower()
        except:
            print("Using full term as delimiter.")
            deli=a[i].lower()

        # Remove plurals -- worth it even when non-plural words end in "s"
        if deli.endswith ('s'):
            deli=deli[:-1].lower()

        print("Using delimiter: %s" %deli)

        count[i]=len(str(r).lower().split(deli))-1
        print(a[i]+': '+str(count[i]))
    
    # Check if not is in the question
    if ' not ' in q.lower():
        best=min(count)
    else:
        best=max(count)

    # Return all answers that are have either the lowest
    # or the highest count (determined above)
    answers=[]
    for i in range(0, len(count)):
            if count[i] is best:
                answers.append(a[i])

    print("Returning: ", answers)
    return answers

# Outputs the amount of google results for a given question + answer
def counter(q, a):

    # Each count item corresponds to an answer (a[0]: counter[0], etc.)
    count=[0]*3

    # For each answer, concatonate it to the question, and grab amount of results
    for i in range(0, len(a)):
        query=urllib.parse.quote_plus(q+' AND '+a[i])

        # Open URL
        try:
            r=urllib.request.urlopen(gURI+query).read()
        except:
            print("Could not access URL.")
            sys.exit()

        # Parse results from JSON data
        count[i]=int(json.loads(r)['queries']['request'][0]['totalResults'])

        print(a[i]+': '+str(count[i]))

    # Check if not is in the question
    if ' not ' in q.lower():
        best=min(count)
    else:
        best=max(count)

    # Return all answers that are have either the lowest
    # or the highest count (determined above) 
    answers=[]
    for i in range(0, len(count)):
            if count[i] is best:
                answers.append(a[i])

    print("Returning: ", answers)
    return answers

# Determine best answers from gathered data
def results(a1, a2):

    # If both return 0 or both return 3, it didn't work
    if len(a1)+len(a2) is not (0 or 6):

        # If first method returns bad answers, trust method 2
        if len(a1) is (3 or 0):
            for x in a2:
                # Cyan
                print("\n\nLikely: \33[36;1m%s\033[0m\n" %x)
        
        # Cross reference answers from method 1 to those from method 2
        # If cross-reference succeedes, print any correct answer(s)
        # Otherwise, print all in answers in a1
        ref=[x for x in a1 if x in a2]

        if len(ref) is 0:
            for x in a1: 
                # Magenta
                print("\n\nSomewhat Likely: \33[35;1m%s\033[0m\n" %x)
        else:
            for x in ref:
                # Green
                print("\n\nExtremely Likely: \33[32;1m%s\033[0m\n" %x)
    else:
        print("\n\n\33[91;1mNo conclusions could be drawn from gathered data.\033[0m\n")

def main():

    # Interactively capture screen
    print("Please select screenshot area.")
    try:
        subprocess.Popen(['screencapture', '-i', 'capture.png']).wait()
    except:
        print("Error capturing screen.")
        sys.exit()

    # Pipe picture to tesseract, ignore text returned to console
    subprocess.Popen(['/usr/local/bin/tesseract', picPath, 'output', '-l', 'eng'], 
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).wait()
    file=open('output.txt').read()

    # Check if file is empty (signaling a parsing error)
    if ''.join(file.split()) is '':
        print("Error parsing screen capture.")
        sys.exit()

    # Generate stripped list of all lines in OCR output
    fData=list(filter(None, [s.strip() for s in file.splitlines()]))

    question=""
    options=[""]*3

    # Add lines to question string until "?", then save location and exit
    pointer=0
    for x in fData:
        question+=x+' '
        if '?' in x:
            break
        pointer+=1
    question.strip()

    # Assuming earch option is on a seperate line (HQ standard),
    # use each next item (new line) as a new option
    options[0]=fData[pointer+1].strip()
    options[1]=fData[pointer+2].strip()
    options[2]=fData[pointer+3].strip()

    # Print out parsed question and options
    print("\n"+question)
    print(options[0])
    print(options[1])
    print(options[2]+"\n\n")

    # URI encode the question
    encoded=urllib.parse.quote_plus(question)

    # Get the answer using the various methods
    googler(encoded, question, options)
    answers1=scanner(encoded, question, options)
    print('\n')
    answers2=counter(question, options)

    # Analyze results     
    results(answers1, answers2)

main()
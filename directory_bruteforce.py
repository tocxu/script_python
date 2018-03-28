from fake_useragent import UserAgent
try:
    import sys #Used to take command line arguments and exit when needed
    import socket #used to test for a valid URL
    import requests # used to make HTTP requests and receive response code

    rhost = sys.argv[1]
    wordlist = sys.argv[2]

# Evaluate the URL
    print ('[*] Cheking RHOST...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        status = s.connect_ex((rhost, 80))
        s.close()
        if status == 0:
            print('[DONE]')
            pass
        else:
            print('[FAIL]')
            print('[!] Error: Cannot Reach RHOST %s\n' %rhost)
            sys.exit(1)
    except socket.error:
        print('[FAIL]')
        print('[!] Error: cannot reach rhost: %s\n' %rhost)

        # Read the Specified Word List
    print('[*] Passing the wordlist...')
    try:
        with open(wordlist) as file:
            to_check = file.read().strip().split('\n') # This will be a list of paths to check #.strip() to get rid of the extra newline at the end of the file
            print('[DONE]')
            print('[*] Total Paths to Check: %s' %(str(len(to_check))))
    except IOError:
        print('[FAIL]')
        print('[!] Error: Failed to read specified File \n')

    # Make the Path Checking Function
    def checkpath(path):
        try:
            print('RHOST: %s' %rhost)
            header=UserAgent().random
            headers = {'User-Agent':str(header)}
            response = requests.get(('http://' + rhost + '/'+ path),headers=headers).status_code
        except Exception:
            print('[!] Error: An Unexpected error Occured')
            sys.exit(1)
        if response == 200:
            print('[*] valid Path Found: /%s' %path)
            with open('result.txt','w') as f:
                f.write(path)
        else:
            print('[*] Fail Path Found: /%s' %path)

    # Iterate Over the List of Paths
    print('\n[*] Beginning Scan...\n')
    for i in range(len(to_check)):
        checkpath(to_check[i])
        print('\n[*] Scan Complete!')
except KeyboardInterrupt:
    print('\n [!] Error: User Interrupted Scan')
    sys.exit()

import re, csv, sys
#input file is an argument, using command line
file = open(sys.argv[1]).read()
#file = open('10.2.82.0.xml').read()
critical = []
severe = []
moderate = []
#create ouput file depend on input filename
output = str(sys.argv[1])[:-4] +'.csv'
with open(output,'w') as result:
#with open('10.2.82.0.csv','w') as result:
    #found = re.findall('<para>(.*)</para>', file)
    #find data by tag
    found = re.findall('<Section (.*)>',file)
    for x in found:
        #filter critical vulnerabilities
        if 'SectionNumber="3.1.' in x:
            critical.append(x)
            result.write(x.replace('SectionLevel','critical')+str(x.split('SectionID="'))+'\n')
        # filter severe vulnerabilities
        elif 'SectionNumber="3.2.' in x:
            severe.append(x)
            result.write(x.replace('SectionLevel','severe')+str(x.split('SectionID="')) + '\n')
        #filter moderate vulnerabilities
        elif 'SectionNumber="3.3.' in x:
           moderate.append(x)
           result.write(x.replace('SectionLevel','moderate')+str(x.split('SectionID="')) + '\n')
#print number of vulnerabilities in each level
print('number of critical: %s ',len(critical))
print('number of severe: %s ',len(severe))
print('number of moderate: %s ',len(moderate))

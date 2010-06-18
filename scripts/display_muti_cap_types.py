import csv

from silcc.lib.capnormalizer import capitalization_type, CapType

if __name__ == '__main__':
    reader = csv.reader(open('data/training/muti_submissions.csv', 'rU'))
    for line in reader:
        if len(line) != 3:
            continue
        print line
        text = line[1] 
        type_ = capitalization_type(text)
        for k, v in CapType.__dict__.iteritems():
            if isinstance(v, int) and type_ == v:
                print k

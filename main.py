

import argparse
import datetime
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-a')
group.add_argument('-b')
parser.add_argument('-o' , '--output' , action='store_true' , help='show output' , required=False)
parser.add_argument('-n' , '--now' , dest='now' , action='store_true' , help='show now' , required=False)
parser.add_argument('-f' , '--file' , dest='file'  )


# parser.add_argument('name' )
# parser.add_argument('family')

args = parser.parse_args()
if args.file:
    print(args.file)

if args.now:
    now = datetime.datetime.now()
    print(f"Now: {now}")

print(args)
#! /usr/bin/env python


#mvng, a much needed reform and renovation of the ancient Unix mv command (dating back to 1971)

import optparse, sys
import signal





def signal_handler(signal, frame):

	print("Interrupted/terminated")

	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


parser = optparse.OptionParser()

parser.add_option('-f', '--force', 	action="store_false", dest="force_flag", help="Don't ask any stupid question, just do it! Default is off", default=False)
#parser.add_option("-p", "--port", type="int", action="store", dest="port", help="Which port to connect for the port ping. Default is 22", default="22")
parser.usage="%prog [options] Source Destination\nMoves a file from source to destination \nWritten by Markus Bawidamann D20200709 after having an unhappy run in with the legacy mv command."


options, args = parser.parse_args()


if args == []:
	print("You must at least specify a source and destination")
	parser.print_help()
	sys.exit(1)



force_flag = options.force_flag
source=args[0]
destination=args[1]

print(source,destination)

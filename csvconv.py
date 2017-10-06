import mailbox
import csv

writer = csv.writer(open("mbox-output.csv", "wb"))

for message in mailbox.mbox('Follow up.mbox'):
	if message['from'] != "Bridget Letts <bridget@groupraise.org>":
		writer.writerow([message['Date'],message['X-Gmail-Labels'], message['subject'], message['from']])

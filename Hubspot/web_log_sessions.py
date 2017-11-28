#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
def checkio(log_text):
    log_list = []
	for log in log_text.split('\n'):
		dt, username, site = log.split(';;')
		dt = datetime(*[int(x) for x in dt.split('-')])
		username = username.lower()
		site = '.'.join(site.split('/')[2].split('.')[-2:])
		log_list.append([dt, username, site])
	sessions = []
	while(log_list):
		log = log_list.pop(0)
		start_time = log[0]
		username = log[1]
		site = log[2]
		quan = 1
		duration = 1
		for l in log_list[:]:
			if l[1] == log[1] and l[2] == log[2] and (l[0] - start_time).days * 24 * 60 * 60 + (l[0] - start_time).seconds < 30 * 60:
				quan += 1
				duration += (l[0] - start_time).seconds
				start_time = l[0]
				log_list.remove(l)
		sessions.append([username, site, duration, quan])
	sessions.sort()
	for i in range(len(sessions)):
		sessions[i][2] = str(sessions[i][2]) 
		sessions[i][3] = str(sessions[i][3])
		sessions[i] = ';;'.join(sessions[i])
	return '\n'.join(sessions)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"


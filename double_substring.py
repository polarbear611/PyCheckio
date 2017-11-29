def repeat_len(text):
	

def checkio(text):
	max_len = 1
	for i in range(len(text)):
		for j in range(i + max_len, len(text), 1):
			rl = repeat_len(text[i:j])
				max_len = max(rl, max_len)

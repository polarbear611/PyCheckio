#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    stressful_words = ['help', 'asap', 'urgent']
    if subj.upper() == subj or subj.endswith('!!!'):
        return True
    subj = subj.lower()
    s = ''
    for i in range(len(subj)):
        if not subj[i] in ['-', '!', '.'] and subj[i] != subj[i - 1]:
            s += subj[i]
        
    return any([s.find(w) >= 0 for w in stressful_words])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')


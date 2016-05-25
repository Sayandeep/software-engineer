#!/usr/bin/env python
def unhash(h):
	letters ="acdegilmnoprstuw"
	a=[]
	i=0
	while(h>37):
		a.append(int(h%37))
		i=i+1
		h=h/37
	word=""
	for j in range (len(a)-1,-1,-1):
		word = word + letters[a[j]]
	return word

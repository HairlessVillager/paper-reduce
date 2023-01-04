import jieba
import jieba.posseg as pseg
import synonyms

print()
print('Welcome!')
while True :
	s = input('input:\n')
	if s == 'q' :
		break
	words = pseg.cut(s)
	replacedWords = []
	for word, flag in words:
		if word not in replacedWords and flag in ['a', 'f', 'v', 'ad', 'q', 's', 'vd'] :
			replacedWords.append(word)
			try :
				newWord = synonyms.nearby(word)[0][1]
				s = s.replace(word, newWord)
				print('replace: %s -> %s' % (word, newWord))
			except :
				print('failed to replace %s' % (word))
	print('result:\n%s' % (s))
	print()

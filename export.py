# -*- coding: utf-8 -*-
import sys,chardet,os,json
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=='__main__':
	fnames=os.listdir('./raw')

	for fname in fnames:

		print fname

		f=open('./raw/'+fname)
		s=f.readline()
		s=s.encode('utf-8')
		obj=json.loads(s)
		s=obj['serviceResult']
		s=s.encode('utf-8')
		obj=json.loads(s)['questions']
		f.close()

		f=open('./readable/'+fname,'w')
		i=1
		for item in obj:
			f.write(str(i)+'. '+item['mainTopic']+item['topic']+'\n')
			for jtem in item['choiceAnswers']:
				if jtem['correct']:
					f.write(' ->'+jtem['mark']+'. '+jtem['choiceAnswer']+'\n')
				else:
					f.write('   '+jtem['mark']+'. '+jtem['choiceAnswer']+'\n')
			if 'answerAnalyse'in item and len(item['answerAnalyse'])>2:
				f.write(u'解析：'+item['answerAnalyse']+'\n')
			f.write('\n')
			i+=1

		# print json.dumps(obj, indent=4, sort_keys=True)
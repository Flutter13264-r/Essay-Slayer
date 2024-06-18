# -*- coding: gbk -*-

# Original work Copyright 2018 The Google AI Language Team Authors.
# Modified work Copyright 2019 Rowan Zellers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
#import tensorflow as tf
import sys
import requests
import time
import random
import argparse
#from utils import *
#from token_reader import *
#from senetence_producer import *

text = "��֪�ļ���ȥɽҰ�ɣ�����ѿ������������Ƶ����룬�����۵�˶������������ɽ��ѩ����֪����������֪·Զ���ͳ����ɣ����Ƴ���Ϧ��С��߹��ӵ�ľ�ţ���֪����������֪��ѧ�����˼�ɣ�������̰��������Цŭ����������У�������ǭ�ף���֪��������峿׳���ֺ�İ����ϼ���ˣ��Ը�·�˽��²�ͣ�����ķ�Ϊ�޴ǣ��Թ���վ��ǰż����Ц��Ϊ��㣬����ܰ����뵵�����Ϊ���ݣ���һ���Ϸ򸾻������ı�ӰΪ��֣���ҡβ������С��Ϊ��ţ���������һƪ�ԡ����ġ�Ϊ��������ѻӱ�д�͡�����������ģ��������Ҹ�������ƣ���������Ȼ������ܰ��ʾ������ϣ���ĵ绰���룬��һ�������ĵĻ�������ѩ��д����¥�Ρ�������˵����д�Լ����ڸ����ͥ�������ţ�һ������Ĵ��꽽�������н����������ư�С�����������ڣ�����ɪ���м������ȣ����Ǿƻ������ɾ���ģ����������ģ�������õ��زģ��������Ľ�ӡ��׺���˴��԰�����˵ı�������ֽ�ϵ����վ�ǳ����֪����Ҫ���С�����������õ���ʦ�������еĵ�λ�ۣ��ճ�����׳���ĺ�������ϲ�����ģ������������д������ģ�Ҳ����ĸ��һ����ů�Ĺػ���Ҳ����·��һ���Ѻõ����ѣ�Ҳ�����ݽ��߻򼤰�����������Ҳ����������Ա��Ĭ�����Ķ��ӣ�Ҳ��ֻ�Ǽ����֣������Դ�����е�ԴȪ��Ŀ������֮������������֮�£����Ǻ����¡������ǳ��������Ƕ��еĸ�·�ˣ���ë˵��������û����Ϣ�ĵط��������ﶼ�������ˡ������ı��������������Ϣ�أ����ǽ���ƽ�м����Ļ�������Ӻ�ݵĻ��������ĵ��½��ϣ����ǽ������������Ļ�������Х������׺�����ĵĶ������ǽ��������ᵽ�Ļ�ܰ����������Ϣ���������ĵķ����ϣ�������������Ϥ��װ��������ı�ͤͤ���������Ľ�����Ʒζ������������ѧϰ���ġ����������ѽѧ����Ժ��ִ��д�֣����������¿�������������һ�����ɳ�������������չʾ�����ĸ�����������޷��������Ҫ�ԣ���ͬ��һ̳�ʴ����Ͼƣ�Խ��Խ���ˣ���������Ѭ���£������鲻�Խ�����Ҫ�ٴ�һƷ��������ʫ�ƣ�������Ϯ��֪��ů����������������кγ���������أ�Ψ������������ʵ��������������֮������ʢ�š���������������������ע�ء��޴��ţ����׷����ϼӺã����׺��ӡ��޴���ţ������ʹӭͷ���ϡ��Դ����ߣ����ڿ��̣����ڲ��ߣ����ڿ��ݡ�ʵ���ϣ����ߣ�����Ҫ���ݡ������ƣ�������ǧ�Ǳ���һʧ������ǧ�Ǳ���һ�á������������������������ѧ��������ϵ���ǽ�����ƽ���������Ļ�������֮һ�����ڸ�����ԣ���ϵ������ǰ;����;���ڵ�λ����֯���ԣ���ϵȺ������淢չ�����ڹ��Ҷ��ԣ��غ�������˥��������й���������ΰ������롣����Ҫ������ӿ�ֳ�һ�������ڵ������ڴ���ġ��ܳ����͡��ɽ�����֧�š���ҵ��չ�������ߡ�����չ�Ĵ����ߣ������������й�������ᷢչ�ġ���ţ�����������ǣ�Ӧ�ø�����ӿ�ѧ������ۺͼ������Լ����ʹ���ȫ��ᡢ�����������ˣ����¸��¡����´��죬���й����������뺽�С����ڻ���һЩ��Ҫ������ҵ�͵�λ��ӹ�١����٣��ر�����Ҫ�����ˣ���������������Ϊ�����������γɵ�ӹ���������������Һ���������Σ�����Թ������������˷�ָ������һЩ��Ϊ���й��Ĺ�Ա������ָ����˭�������Լ���������Ծ��Ժ�������������������ţ��������ţ��������ţ���������ܽ�����ΪһЩ�����ı���ɼ�������������ۣ���Ӧ�ÿ��ɼ�����ı��ʺͻ�������ʵ���ۣ��ϼӴ��á������й���ᷢչ���ĸ￪��30�����������ó������ٷ�չ������������������������������ȫ��Χ����Ȼ������Խϸ����ٷ�չ�����ʹ���һЩ���۾���˿�˥�й����ã����й����費�͹۵����ۡ����й��������Ρ���Ȩ����������������ҵ���Ͻ����У����ʹ���һЩ���۶Դ��Ӷ��������������ţ�������һЩǷ������Һ͵�������������Ȩ�ȷ�����ƣ�����ȴ���������������Ҳ��һ�ֲ���ѧ����֪����Ϊ�쵼�ߣ������ǡ��޴��ţ��ʱ����Ӧ�ù�ע����ġ���ţ�����ʵ���ʱ��ҲӦ�ó����;��Ϊ���۵Ĺ�ע�ߣ������Ǵӡ�����������ͷ�����������ߵ�ʱ��Ӧ�ðѸ����Ŀ��۽��ں������������Ҫ����;��Ϊ����һ���ӣ�������ѧ���ÿ��ݵ����������ɡ���ţ��֮�����������Ǿ͸���������á���ţ���䡰�족����ˣ����ҽ������á�����Ϊ"
result = []
text1 = "�������۾������ˡ������磬ȴ�޷�ֱ�ӿ����������Լ������ԣ����������ó��У�������ҪѰ�Ҹ��֡����ӡ������ϻ��ơ��Ի������������ң����Իش������������ˡ�������������������������Щʲô�����������ø������塱����Ҫ�����⡣���ܸ����ң�������������ģ�����Ҫʲô�����ܸ����ң�����ʧȥʲô������Ҫʲô���������Ľ����У��ҵ�һ���Ի�����Ϊ��Ҫ�����ܰ��������ڱ�Ҫ��ʱ��ش���������⡣��ô��Ҫ��һ���������Ի����أ����ȣ�ȷ��һ���˵�����������������ǽ�����Ҫ���۵ġ�һ����Ҫ��ο����Լ���Ҫ��ζԴ��Լ���������Լ���ǰ�����ţ������ִ������ٵ�һ�����������⡣��ο����Լ����ִ���ͨ���������Լ�����Ϊĳ���ط����������һ�����࣬�ɴ˶�ȷ�����Լ���һЩ�����ԡ���ʵ�����������Ǽ�ֵ����ͬ��������Ŀ϶�������Ϊ��֤�����Ǿ�������ļ�ֵ�ͼ̳еı�֤�������ǽ����ո����׵Ļ����κβ��ǿ��Լ����ǻ۾������������磬���ǿ�����������Լ����ǻۡ����ǣ�����֮�������˸��������ں������ǵ�����������۹��������Լ�����������õ������п�����ʵ���Լ����������ң������Ի�������������·�ϵ�ʵ�����������˵��ǻ������Լ���ͨ������������Ĺ�ͨ��ϵ���Լ������������ǻ۵Ŀ��⡣��������Ѱ���Լ������Լ�������Ĺ�ͨ��ϵ�л����Ի�������������·�ϵĶԻ������磬��ס���ⷿ�����������������������˵���������ܡ����磬���Ǵ�ɽ��������Ҫ�㣬��Ϊû���㣬��û���˴�ɽ�����磬���ǲ��䣬������Ҫ�㣬��Ϊû���㣬��û���˲��䡣�㲻��˵�����ס�ڷ����ȴ������鼰����ɳĮ������Ϊû�п���ɭ�֣���ķ�������û��ɭ���ˡ���ʱ����ͻῴ������ɭ�֡�ÿһ���˶������Լ����Ļ�����д���Լ������֡���Ҳ����������۹⿴�Լ����ǻ۵�������һ�����Ի������������췱�����������ԡ�ͬʱ�������Ի�����Ҫ���ӡ�����������ǵı���д���Լ������֣����������Լ������ֵ������ǩ�����������𻭾������Լ��Ļ���ǰ���ͳ�Ϊ��������ˡ���Ȼ���������С�����ͻῴ�������������ׯ�ϣ����ϳ����˽����ӣ����ϵĲ������Ƹ�������Ҳ�ῴ�����������ĺӣ���ĸ�׵��ָ������Լ������գ�Ϫˮ���ݺύ����֦ͷ���������������Ӥ�����ͻῴ����������㷭�Ű�ɫ����������ӵĶ԰������ߡ�����������������ߵ�С��һ�����ſ��۾���������˯����ʱ����ͻῴ��һ�ж���г��������ˮ�ľ�ֹ��ɽ����ΰ��"
text2 = ""

parser = argparse.ArgumentParser(description='Contextual generation (aka given some metadata we will generate articles')

parser.add_argument(
	'-org_text',
	dest='org_text',
	type=str,
	help='Model_generated article'
)

class AutoFormatter(object):
	'''���Ϸ������ݲ�ʵ����'''
	def __init__(self):
		self.para_limit = total
		self.result = "  "
		self.paras
		pass 

	def auto_formatting(self, text):
		seg = self.para_limit
		processed = text.split('��')
		print("split sentence slice: ", processed)
		lens = len(processed)
		if(lens >= 10):
			paras.append(int(0.2 * lens))
			paras.append(int(para1 + 0.5 * lens))
			paras.append(int(para2 + 0.3 * lens))
		else:
			paras.append(3)
			paras.append(lens - 5)
			paras.append(lens - 3)
		for pos in paras:
			# ���ո߿�����Ҫ��Ϊÿһ�����׼ӿո�
			result = result +  "    " + processed[para1]
			result += '��\n'
		print("formatted paragraph: ", result)

def coarse_formatter(text):
	'''��һ���Ű���'''
	paras = []
	final = ""
	text_list = text.split("��")
	# text_list = text_list[:15]
	if text_list[-1] != '':
		text_list = text_list[:-1]
	# print("ȥ��β����Ϊ��", text_list)
	# �ֶ��䣬��ͷ3��Ϊ���ף��м�5��Ϊ���У����5��Ϊ��β
	# print("split sentence slice lens: ", len(text_list))
	count = 3
	lens =  len(text_list)
	paras.append(text_list[:3])
	if(lens >= 10):
		while count < lens - 5:
			#print("para: ", para ," | final: ", lens - 8)
			paras.append(text_list[count:count+5])
			count += 5
		# print("�������Ӷ�β��", text_list[para:-1])
		if count == lens - 1:
			pass
		else:
			paras.append(text_list[count:-1])
	else:
		paras.append(text_list[:3])
		paras.append(text_list[3:lens - 5])
		paras.append(text_list[lens - 5:lens])
	# print("���ն���Ϊ��", paras)
	for para in paras:
		# print("paras: ", para)
		if len(para) == 1:
			final += "    " + para[0] + "��\n"
		else:
			count = 0
			for p in para:
				#print("p: ", p)
				if(count == 0):
					final +=  "    " + p + "��"
				elif(count != len(para)-1):
					final += p + "��"
				else:
					final += "\n"
				count += 1
	print("\n")
		
	# print("�����ı�Ϊ��\n", final)
	return final


def immediate_print(msg, text):
    print(msg)
    for i in text:
        print(i, end="")
        sys.stdout.flush()
        time.sleep(random.random()/20)

if __name__ == "__main__":
	#try:
	step = 125
	args = parser.parse_args()
	print("the lens: ", int(len(text)/step))
	with open(args.org_text, 'r',encoding='UTF-8') as f:
		text = f.read()

	final_output = coarse_formatter(text)
	immediate_print('�Ű�������������...', final_output)
	text_list = text.split("��")
	# print("sequence list: ", text_list)
	#for seq in text_list:
		# print("start: ", pre ," end : ",pre + step)
		# if(pre + step) >= len(text):
		# seg = get_value(access_token, seq)
		#print("seg: ", seg)
		#scores = float(seg.split(":")[-1].strip('}'))
		#result.append(scores)
	#except:
		#print("scoring api has failed...")
	# dicts = result[0].split(":")
	# plexity = result.get['ppl']
	# print("the final ppl score is: \n")
	#print(sum(result))

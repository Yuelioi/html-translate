from bs4 import BeautifulSoup
from google.cloud import translate_v3beta1 as translate
import os

#1 使用BeautifulSoup（以下简称BS）把原始数据切割为列表
soup = BeautifulSoup(open('.html',encoding='utf-8'), features='html.parser') 
list_source = soup.prettify().split('\n')

#2 分割原始文档列表：需要翻译的部分与不需要翻译的部分（用的是for，有其他方法可以留言），类似[['1','hi'],[['2'],['hello']]的有序叠加列表
tran_list = [] #要翻译的列表
noTran_list = [] #不要翻译的列表
all_list = [] #所有内容组成的列表
index_src = 0
for content_src in list_source:
    if content_src.strip().startswith('<'):
        noTran_list.append([index_src, content_src])
    else:
        tran_list.append([index_src, content_src.strip()])
    index_src += 1

#3 需要翻译的进行翻译（我用的谷歌翻译api，这里可以换成其他免费/收费翻译代码）
text_tran = list(dict(tran_list).values())  # text_tran为要翻译的列表，类似['hello','how are you','yes']

client = translate.TranslationServiceClient()
def tran_google(text1):
    if len(text1) > 300:
        final_translate_str = ""
        text2 = [text1[i:i + 30] for i in range(len(text1)) if i % 30 == 0]
        text2_len = len(text2)
        for i in range(0, text2_len):
            text = '\n'.join('%s' % id for id in text2[i])
            project_id = 'Your google project id'
            contents = [text]
            parent = client.location_path(project_id, "global")
            response = client.translate_text(
                parent=parent,
                contents=contents,
                mime_type='text/plain',  # mime types: text/plain, text/html
                source_language_code='en',
                target_language_code='zh')
            for translation in response.translations:
                final_translate_str = final_translate_str + translation.translated_text + '\n'
    else:
        text = '\n'.join(text1)
        # print(text)
        project_id = 'Your google project id'
        contents = [text]
        parent = client.location_path(project_id, "global")
        response = client.translate_text(
            parent=parent,
            contents=contents,
            mime_type='text/plain',  # mime types: text/plain, text/html
            source_language_code='en',
            target_language_code='zh')
        for translation in response.translations:
            final_translate_str = translation.translated_text

    tran_res = final_translate_str.split('\n')
    return tran_res
  
final_list = tran_google(text_tran) # final_list为翻译后的列表，诸如['你好','你多大了','好的']

#4 翻译后的内容加入源文件（可以用其他方法处理翻译后以及原始内容）
final_list_res = []
for i in range(len(tran_list)):
    final_list_res.append([tran_list[i][0], tran_list[i][1] + '  |  ' + final_list[i]])
print(final_list_res)

#5 翻译 + 不用翻译的进行合并，且根据序号进行顺序排列（见#2 排序方法）
def takeSecond(elem):
    return elem[0]

  all_list = noTran_list + final_list_res
res_list = sorted(all_list, key=takeSecond) #按序号排序所有内容
res = ''
for i in res_list:
    res = res + i[1] + '\n'

# 写入
with open(r"111.html","w", encoding='utf-8') as f:
    f.write(res)

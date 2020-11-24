from bs4 import BeautifulSoup
# from google.cloud import translate_v3beta1 as translate
import os

data = '''<!DOCTYPE html>
<!--[if IE 8]><html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->
<head>
  <meta charset="utf-8">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>After Effects Expression Reference 0.0.3 documentation</title>








  <script type="text/javascript" src="_static/js/modernizr.min.js"></script>


      <script type="text/javascript" id="documentation_options" data-url_root="./" src="_static/documentation_options.js"></script>
        <script type="text/javascript" src="_static/jquery.js"></script>
        <script type="text/javascript" src="_static/underscore.js"></script>
        <script type="text/javascript" src="_static/doctools.js"></script>
        <script type="text/javascript" src="_static/language_data.js"></script>

    <script type="text/javascript" src="_static/js/theme.js"></script>




  <link rel="stylesheet" href="_static/css/theme.css" type="text/css" />
  <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
  <link rel="stylesheet" href="_static/_static/css/theme.css" type="text/css" />
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" /> 
</head>

<body class="wy-body-for-nav">


  <div class="wy-grid-for-nav">

    <nav data-toggle="wy-nav-shift" class="wy-nav-side">
      <div class="wy-side-scroll">
        <div class="wy-side-nav-search" >



            <a href="index.html#document-index" class="icon icon-home"> After Effects Expression Reference



          </a>





              <div class="version">
                latest
              </div>




<div role="search">
  <form id="rtd-search-form" class="wy-form" action="search.html" method="get">
    <input type="text" name="q" placeholder="Search docs" />
    <input type="hidden" name="check_keywords" value="yes" />
    <input type="hidden" name="area" value="default" />
  </form>
</div>


        </div>

        <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="main navigation">




              <!-- Local TOC -->
              <div class="local-toc"><p class="caption"><span class="caption-text">Introduction</span></p>
<ul>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-introduction">Introduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-resources">Resources</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-examples">Examples</a><ul>
<li class="toctree-l2"><a class="reference internal" href="index.html#get-this-project-s-aep-name-ae-15-1-only">Get this project’s AEP name (AE 15.1+ only)</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#make-a-layer-revolve-in-a-circle">Make a layer revolve in a circle</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#rotate-the-hands-of-a-clock">Rotate the hands of a clock</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#position-one-layer-between-two-others">Position one layer between two others</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#create-a-trail-of-images">Create a trail of images</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#create-a-bulge-between-two-layers">Create a bulge between two layers</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#fade-opacity-of-a-3d-layer-based-on-distance-from-camera">Fade opacity of a 3D layer based on distance from camera</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#make-a-3d-layer-invisible-if-facing-away-from-camera">Make a 3D layer invisible if facing away from camera</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#flip-layer-horizontally-if-facing-away-from-camera">Flip layer horizontally if facing away from camera</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#animate-scale-at-each-layer-marker">Animate scale at each layer marker</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#start-or-stop-wiggle-at-specific-time">Start or stop wiggle at specific time</a></li>
<li class="toctree-l2"><a class="reference internal" href="index.html#match-camera-focal-plane-to-another-layer">Match camera focal plane to another layer</a></li>
</ul>
</li>
</ul>
<p class="caption"><span class="caption-text">General</span></p>
<ul>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-global">Global</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-time-conversion">Time conversion</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-vector-math">Vector Math</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-random-numbers">Random Numbers</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-interpolation">Interpolation</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-color-conversion">Color Conversion</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-other-math">Other Math</a></li>
</ul>
<p class="caption"><span class="caption-text">Objects</span></p>
<ul>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-project">Project</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-comp">Comp</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-footage">Footage</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-camera">Camera</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-light">Light</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-effect">Effect</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-mask">Mask</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-property">Property</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-path-property">Path Property</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-key">Key</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-markerkey">MarkerKey</a></li>
</ul>
<p class="caption"><span class="caption-text">Layer</span></p>
<ul>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-layer-sub">Layer Sub-objects</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-layer-general">Layer General</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-layer-properties">Layer Properties</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-layer-space">Layer Space Transforms</a></li>
<li class="toctree-l1"><a class="reference internal" href="index.html#document-layer-threed">Layer 3D</a></li>
</ul>
</div>


        </div>
      </div>
    </nav>

    <section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">


      <nav class="wy-nav-top" aria-label="top navigation">

          <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
          <a href="index.html#document-index">After Effects Expression Reference</a>

      </nav>


      <div class="wy-nav-content">

        <div class="rst-content">'
'''
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'G:\back\pyfile\google-key\google-key.json'

soup = BeautifulSoup(
    open(r'C:\Users\qmtv\Downloads\after-effects-expressions-guide-latest\index.html',
         encoding='utf-8'), features='html.parser')
# soup=BeautifulSoup(data,features='html.parser')

list_source = soup.prettify().split('\n')

# 分割原始文档列表：需要翻译、不需要翻译
print('开始分割源数据')
tran_list = []
noTran_list = []
all_list = []
index_src = 0
for content_src in list_source:
    if content_src.strip().startswith('<'):
        noTran_list.append([index_src, content_src])
    else:
        tran_list.append([index_src, content_src.strip()])
    index_src += 1

# 需要翻译的进行双语翻译
print('开始翻译')
# client = translate.TranslationServiceClient()
text_tran = list(dict(tran_list).values())

'''
def tran_google(text1):
    if len(text1) > 300:
        final_translate_str = ""
        text2 = [text1[i:i + 30] for i in range(len(text1)) if i % 30 == 0]
        text2_len = len(text2)
        for i in range(0, text2_len):
            text = '\n'.join('%s' % id for id in text2[i])
            project_id = '470576158197'
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
        project_id = '470576158197'
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
'''

# final_list = tran_google(text_tran)
final_list = ['After Effects表达式参考0.0.3文档', 'After Effects表达式参考', '最新', '介绍', '介绍', '资源资源', '例子', '获取此项目的AEP名称（仅限AE 15.1+）', '使图层旋转一圈', '旋转钟针', '将一层放置在其他两层之间', '创建图像轨迹', '在两层之间创建凸起', '根据与相机的距离确定3D图层的淡入度不透明度', '如果远离相机，则使3D图层不可见', '如果背对镜头，请水平翻转图层', '在每个图层标记处设置动画比例', '在特定时间开始或停止摆动', '将相机焦平面匹配到另一层', '一般', '全球', '时间转换', '向量数学', '随机数', '插补', '颜色转换', '其他数学', '对象', '项目', '补偿', '画面', '相机', '光', '影响', '面具', '属性', '路径属性', '键', '标记键', '层', '图层子对象', '图层一般', '图层属性', '图层空间变换', '3D层', 'After Effects表达式参考', "'"]
final_list_res = []
# 翻译后的内容加入

for i in range(len(tran_list)):
    final_list_res.append([tran_list[i][0], tran_list[i][1] + '  |  ' + final_list[i]])
print(final_list_res)

# 翻译 + 不用翻译的进行合并
print('开始合并源数据')


def takeSecond(elem):
    return elem[0]


all_list = noTran_list + final_list_res
res_list = sorted(all_list, key=takeSecond)
print(res_list)
res = ''
for i in res_list:
    res = res + i[1] + '\n'
# print(res)

# 写入
with open(r"G:\study\5.脚本编写\ae-expressions-docsforadobe-dev-en-latest\after-effects-expressions-guide-latest\911.html",
          "w", encoding='utf-8') as f:
    f.write(res)
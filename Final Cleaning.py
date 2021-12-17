# -*- coding: utf-8 -*-
"""Cleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1my8aHV7LX2bZqKHqlaLhcKtMf7fR8skr
"""

import numpy as np
import pandas as pd
import re

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('output.csv',encoding='utf-8')
df.head()

df.columns = pd.Series(df.columns).apply(lambda x: x.lower())

#clean_publisher_column
for i in df.index:
    df['publisher'][i] = re.sub('[/(){}\[\]\|!,;.]', ' ', df['publisher'][i])
    df['publisher'][i] = re.sub('دار النشر:| دار النشر: ', '', df['publisher'][i])

# Publisher eye balling

suffixs_and_prefixs = [
        'للنشر',
        'للنشر والإعلان',
        'للنشر والطباعة',
        'للنشر والتوزيع',
        'للنشر والترجمة',
        'للنشر الإلكتروني',
        'للنشر والإنتاج الإعلامي',
        'للنشر والتوزيع والترجمة',
        'للنشر والطباعة والتوزيع',
        'للطباعة',
        'للطباعة والنشر',
        'للطباعة و النشر',
        'للطبع والنشر',
        'للطباعة والنشر والتوزيع',
        'للطبع والنشر والتوزيع',
        'للتعليم والثقافة',
        'للدراسات والأبحاث',
        'للدراسات و الأبحاث',
        'للدراسات',
        'للأبحاث والدراسات',
        'للابحاث والنشر',
        'للترجمة',
        'للترجمة والنشر',
        'للترجمه والنشر',
        'للترجمة و النشر',
        'للإعلام',
        'للإعلام والنشر',
        'للإنتاج الإعلامي والتوزيع',
        'للبحوث',
        'للثقافة',
        'للثقافة والنشر',
        'للثقافة والعلوم',
        'للثقافة والسياحة',
        'للتوزيع والنشر',
        'التوزيع والنشر',
        'للصحافة والنشر',
        'للصحافة والطباعة والنشر',
        'للصحافه والطباعه والنشر والتوزيع',
        'للتأليف والترجمة',
        'للتراث',
        'للتدريب والنشر',
        'للتربية والثقافة والعلوم',
        'للتدعيم والتطوير',
        'سي آي سي',
        'دار',
        'الدار',
        'ودار',
        'المؤسسة',
        'مؤسسة',
        'موسسة',
        'مجمع',
        'المجمع',
        'مكتبة',
        'مكتبه',
        'المكتبة',
        'مكتبو',
        'ومكتبة',
        'المكتب',
        'مطبعة',
        'مطابع',
        'المركز',
        'مركز',
        'للكتب',
        'للكتاب',
        'للكتب والمعارف',
        'للكتب والنشر',
        'شركة',
        'الشركة',
        'منتدي',
        'مجلة',
        'ومطبعتها',
        'دار النشر',
        'الهيئة',
        'منشأة',
        'منشورات',
        'منشور',
        'مطبوعات',
        'مجموعة',
        'المشروع',
        'ش م م',
        'غير محدده',
        'غير معروف',
        'عير معروف'
]

for i in df.index:
  for sp in suffixs_and_prefixs:
    df['publisher'][i] = re.sub(sp, '', df['publisher'][i])

# Publisher eye balling

'Free Press' -----> 'جرير'
'كتاب التربية الروحية في الإسلام PDF' -----> 'بهانج دار المعمور'
'القران الكريم' -----> 'الله عز وجل'
'منزل من الله' -----> 'الله عز وجل'
'قران كريم' -----> 'الله عز وجل'

# Book Category eye balling
'تعليم برمجة' -> 'برمجة'
'التاريخ  التاريخ الإسلامي' -> 'التاريخ الإسلامي'
'الأدب العالمي المترجم  القصص القصيرة المترجمة' -> 'الأدب العالمي و القصص القصيرة'
'الأدب العالمي المترجم الروايات العالمية المترجمة' -> 'الأدب العالمي و الروايات العالمية'
'التاريخ  التاريخ الحديث' -> 'التاريخ الحديث'

# Book Category eye balling

'برمجة'
'اسلامية'
'التنمية الذاتية'
'إدارة الأعمال'
'انجليزية'
'الثقافة العامة'
'التاريخ الإسلامي'
'الأدب العالمي و القصص القصيرة'
'الأدب العالمي و الروايات العالمية'
'اللغة العربية'
'التاريخ الحديث'
'التاريخ القديم'
'التاريخ'
'أدب الرحلات'
'روايات عربية'
'العقيدة'
'أعلام وشخصيات'
'الأدب'

#clean_book_category_column
for i in df.index:
    df['book_category'][i] = re.sub('\n|:\n', '', df['book_category'][i])
    df['book_category'][i] = re.sub('[/(){}\[\]\|!,;.]', '', df['book_category'][i])
    df['book_category'][i] = re.sub(' قسم الكتاب:|تحميل|كتب|قسم الكتاب:', '', df['book_category'][i])
    df['book_language'][i] = re.sub('لغة الكتاب: ', '', df['book_language'][i])
    df['book_language'][i] = re.sub('عربية|العربية|عربي|العربية|اللغة العربية|العربيىة|اللعة العربية|اللغه العربية|اللغه العربيه|العريبية|عربية|الللغة العربية', 'Arabic', df['book_language'][i])
    df['book_language'][i] = re.sub('الانجليزية|English|إنجليزي|الإنجليزية', 'English', df['book_language'][i])
    df['book_language'][i] = re.sub('المانية|الألمانية', 'German', df['book_language'][i])
    df['book_language'][i] = re.sub('الArabicه|العرببة', 'Arabic', df['book_language'][i])

#clean_author_column
for i in df.index:
    df['author'][i] = re.sub('[a-zA-Z]', '', df['author'][i])
    df['author'][i] = re.sub('[/(){}\[\]\|!,;.]', '', df['author'][i])
    df['author'][i] = re.sub('\n|:\n', '', df['author'][i])
    df['author'][i] = re.sub('مؤلف الكتاب|كتب|الكاتب', '', df['author'][i])
    df['book_name'][i] = re.sub('\n|:\n', '', df['book_name'][i])
    df['book_name'][i] = re.sub('[/(){}\[\]\|!,;.]', '', df['book_name'][i])
    df['book_name'][i] = re.sub('كتاب|PDF|pdf|The book of|PDf| للكاتب أحمد خالد توفيق|ملخص وتحميل|لاحمد خالد توفيق| أحمد خالد توفيق|رواية |للكاتب إريك فروم|لإحسان عبدالقدوس|للكاتب أبو حامد الغزالي|للشيخ كشك|للشيخ عبد الحميد كشك|للشيخ يوسف القرضاوي|للكاتب أدهم الشرقاوي|ابراهيم الفقى|فهرس عام لل|للحافظ ابن كثير|مقدمة ال|لابن كثير|لأدهم شرقاوي||لإلياس أبو شبكة|للكاتب باولو كويلو|تشارلز دويج|لتوفيق الحكيم|للكاتب ثروت أباظة|جاري تشابمان|للكاتب جبران خليل جبران|جورج كلاسون|جوزيف ميرفي|للكاتب جوش كاوفمان|جون غراى|لديل كارنيجي|ديل كارنيجي|ديوك روبنسون|روبير هوفمان|ستيفن ار كوفي|للكاتب سيد قطب|عادل عصمت|لعادل مصطفي|– عباس العقاد|فرانتس كافكا|للمؤلف فرج جبران|لفهد عامر الاحمدي|فهد عامر الأحمدي| كارل ألبريخت|لكامل الكيلاني|لكريم الشاذلي|لمحمد الغزالي|لمحمود سالم|لنجيب محفوظ|لنعوم تشومسكي|هارف إيكر|مجلة|ليوسف زيدان|لـ جينيفر تي روبرتس|لاليف شافاق|لابن سالم باهشام|للكاتب محمد حسين هيكل|محمد حسين هيكل|للكاتب دليل بيرنز|للكاتب روديارد|لزكي نجيب|للدكتور سهيل بن محمد القاسم|للكاتب سيغموند فرويد|لعبد الحليم محمود|لفؤاد زكريا|للإمام البوصيري|للكاتب مصطفى محمود|لمصطفى محمود|لدكتور مصطفى محمود|مصطفى محمود|للألباني|لدكتور محمد طه|لمارون عبود|للدكتور محمد بن إبراهيم بن سليمان الرومي|للشيخ محمد رشيد رضا|لمحمد رياض|للكاتب يوسف إدريس|ليوسف ادريس', '', df['book_name'][i])

#clean_book_extention_column
for i in df.index:
    df['book_extention'][i] = re.sub('[^a-zA-Z]', '', df['book_extention'][i])
    df['book_extention'][i] = df['book_extention'][i].lower()

#clean_book_size_column
for i in df.index:
    #df['book_size'][i] = re.sub('حجم الكتاب: |ميغابايت|كيلوبايت |ميجا بايت|كيلو بايت |ذ|ميجا |ميجابت ', '', df['book_size'][i])
    #df['book_size'][i] = re.sub('[/(){}\[\]\|!,;>-]', '', df['book_size'][i])
    df['book_size'][i] = re.sub('[^0-9.]', '', df['book_size'][i])
    df['number_of_pages'][i] = re.sub('[^0-9]', '', df['number_of_pages'][i])


df[df['book_size']=='']=0
df['book_size'].astype('float')
df[df['number_of_pages']=='']=0
df['number_of_pages'].astype('int64')

df.dropna(inplace=True)
df.drop(['dummy'], axis = 1, inplace=True)
df.drop(['book_extention'], axis = 1, inplace=True)

df.to_csv('final.csv',encoding='utf-8')

df.head()

df.drop(['author'], axis = 1, inplace=True)
df.drop(['book_link'], axis = 1, inplace=True)

df.head()

len(df)

for i in df.index:
  if df['publisher'][i] == "0":
    df.drop(['author_name'][i], axis = 0, inplace=True)

df = df[df.publisher != '  ']

len(df)

df.head()

df = df[df.number_of_pages != 0]

len(df)

df.head()

len(df)

df.to_csv('out.csv',encoding='utf-8')

df = df[df.book_language != '']

len(df)

df = df[df.book_language != '  ']

len(df)

df.head()

for i in df.index:
    df['publisher'][i] = re.sub('-', '', df['publisher'][i])
    df['publisher'][i] = re.sub('[(0-9)+]', '', df['publisher'][i])

df = df[df.publisher != '']

len(df)

df

df.drop([df.index[1]], inplace=True)

df.drop([df.index[1] , df.index[2], df.index[2], df.index[6]], inplace=True)

df.drop([df.index[1] , df.index[6]], inplace=True)

df['author_name'][1] = re.sub('David Graeber', '', df['publisher'][i])

len(df)

df = df[df.author_name != '']

len(df)

df

df.reset_index(drop=True, inplace=True)

df

x = df.book_category.unique()

type(x)

unique_words = []
for i in x:
  lis = i.split(sep=' ')
  for v in lis:
    unique_words.append(v)

unique_words = set(unique_words)

len(unique_words)

for i in unique_words:
  print(i)

df

df.to_csv('Final Output.csv',encoding='utf-8')

len(df.book_category.unique())


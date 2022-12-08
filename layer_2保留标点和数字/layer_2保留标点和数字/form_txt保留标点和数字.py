import pandas as pd


def cate2label(cate_file, cate_name):
    #从给定的存储在外部的分类文件，获取某一列表形式的分类的label
    cate_df = pd.read_excel(cate_file)
    for i in range(len(cate_file)):
        if cate_df.at[i, 'cate'] != cate_name:
            continue
        else:
            return cate_df.at[i, 'name']


def form_title_et_abs(csv_file_name ,abs_weight = 1, title_weight = 0):
    # 可以调整两个参数生成按照需要组合的摘要和标题的复合文档需要的
    id_file = open(f'ab{abs_weight}_title_{title_weight}_id.txt', 'w', encoding='utf-8')  # 这是id_file，留个记录总会有用，顺序和后面生成的txtlabel一致，以备不时之需
    id_file.write('id,lebel\n')
    df = pd.read_csv(csv_file_name, index_col='id', delimiter='\t')
    df.fillna('')
    #print(df)
    txt_file = open(f'ab{abs_weight}_title_{title_weight}_data.txt', 'w', encoding='utf-8')
    for i in range(len(df)):
        cate = df.at[i, 'cate']
        label = cate2label('Layer_2_cate.xlsx', cate)  # 这里的cate_file 依赖于外界，而且为了避免函数有过多参数，所以我就默认都是这个文件吧
        id_file.write(f'{i},{label}\n')
        txt_file.write(f'{label} ')
        txt_file.write(df.at[i, 'abstract'] * abs_weight + ' ' + df.at[i, 'title'] * title_weight + '\n')
    id_file.close()
    txt_file.close()

def form_keywords(csv_file_name):
    id_file = open(f'keywords_id.txt', 'w', encoding='utf-8')  # 这是id_file，留个记录总会有用，顺序和后面生成的txtlabel一致，以备不时之需
    id_file.write('id,lebel\n')
    df = pd.read_csv(csv_file_name, index_col='id', delimiter='\t')
    df.fillna('empty')
    #print(df)
    txt_file = open(f'keywords_data.txt', 'w', encoding='utf-8')
    for i in range(len(df)):
        cate = df.at[i, 'cate']
        label = cate2label('Layer_2_cate.xlsx', cate)  # 这里的cate_file 依赖于外界，而且为了避免函数有过多参数，所以我就默认都是这个文件吧
        id_file.write(f'{i},{label}\n')
        txt_file.write(f'{label} ')
        txt_file.write(str(df.at[i, 'key_words']) + '\n')
    id_file.close()
    txt_file.close()




def main():
    csv = 'washed_data保留数字标点.csv'
    form_title_et_abs(csv)
    form_keywords(csv)

def test():
    c = ['元分析',
'协同技术',
'实体经济',
'市场治理',
'平台项目',
'技术治理',
'核心技术',
'法律治理',
'虚拟经济']
    for item in c:
        print(cate2label('Layer_2_cate.xlsx', item))

main()


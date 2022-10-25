import pandas as pd

df =pd.read_csv("kana_romaji.csv")

def has_mise_at_the_end(name,romaji):

    trim = name.strip()
    trim2 = romaji.strip()
    
    print(trim2[-4:])
    if trim[-1] =='店' and trim2[-4:] == 'mise' :
        return str(trim2[:-4]+"ten")

    return romaji


temp = []
for i,r in df.iterrows():

    print(r)
    # name = has_mise_at_the_end(r["title"],r["merchant_name_kana"])
    name = has_mise_at_the_end("店","mise")
    name = has_mise_at_the_end("","mise")

    temp.append(name)


df["ten_change"] = temp


def cnt(words):
    count={}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return dict(sorted(count.items(), key=lambda x: x[1]))

para=input("Enter a paragraph: ")
words=para.split()
print(cnt(words))
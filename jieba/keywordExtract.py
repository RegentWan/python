import jieba
import jieba.analyse

topK = 10
str= "奋斗创造历史，实干成就未来。我们要更加紧密地团结在以习近平同志为核心的党中央周围，高举中国特色社会主义伟大旗帜，以习近平新时代中国特色社会主义思想为指导，迎难而上，开拓进取，以经济社会发展的优异成绩迎接中华人民共和国成立70周年，为决胜全面建成小康社会、夺取新时代中国特色社会主义伟大胜利，为把我国建设成为富强民主文明和谐美丽的社会主义现代化强国、实现中华民族伟大复兴的中国梦不懈奋斗！"
tf_tags = jieba.analyse.extract_tags(str, topK=topK)
print("TF-IDF:","/".join(tf_tags))

rank_tags=jieba.analyse.textrank(str)
print("TF-IDF:","/".join(rank_tags))

print("返回词频:",end='')
for x, w in jieba.analyse.textrank(str, withWeight=True):
    print('%s %s' % (x, w))
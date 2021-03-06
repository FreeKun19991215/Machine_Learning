from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return:
    """
    news = fetch_20newsgroups(subset="all")  # 20种新闻数据集

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集进行特征重要性抽取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)  # 已训练集当中的列表进行每篇文章的重要性统计
    print(tf.get_feature_names())
    x_test = tf.transform(x_test)  # 使用训练集训练的词的重要性列表的数据提取测试集对应的词的重要性

    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    print(x_train.toarray())
    mlt.fit(x_train, y_train)

    # 预测
    y_predict = mlt.predict(x_test)
    print("预测的文章类别为：", y_predict)

    # 得出准确率
    print("准确率为：", mlt.score(x_test, y_test))
    
    # 精确率、召回率和f1-score
    print("精确率、召回率和f1-score：")
    print(classification_report(y_test, y_predict, target_names=news.target_names))


if __name__ == '__main__':
    naviebayes()

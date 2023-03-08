from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

txt = open(r"C:\Users\Gopal\PycharmProjects\3D_Matplotlib.Plots\Text.txt", "r").read()
words = STOPWORDS
print(words)

pic = WordCloud(background_color='white', stopwords=words,height=590,width=480)
pic.generate(txt)
pic.to_file("WordCloudPic3.png",)


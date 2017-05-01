from flask import Flask,render_template
from sklearn.cluster import KMeans
from numpy import genfromtxt

app = Flask(__name__)


@app.route('/')
def hello_world():
    my_data = genfromtxt("C:/Users/Ankush/PycharmProjects/azure/data.csv", delimiter=',')
    kmeans = KMeans(n_clusters=2, random_state=0).fit(my_data)
    return render_template("home.html",results = kmeans.cluster_centers_)


if __name__ == '__main__':
    app.run()

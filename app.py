from flask import *
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie

app = Flask(__name__)

##########################################


@app.route("/")
def show_charts():
    try:
        from DrawPicture import draw_picture
        chart_options = draw_picture()

        return render_template('show_charts.html',
                               chart_options=chart_options)
    except TypeError:
        pass

if __name__ == "__main__":
    app.run(debug=True)

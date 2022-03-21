from flask import *

app = Flask(__name__)
app.config.from_object('configs')
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
    app.run()

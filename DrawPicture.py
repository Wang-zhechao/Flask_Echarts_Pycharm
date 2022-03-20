from pyecharts import options as opts
from pyecharts.charts import Bar, Pie


def draw_picture():
    chart_options = []
    bar = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 10, 20])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="AB数据对比"))
    )
    chart_options.append(bar.dump_options())

    pie = (
        Pie()
        .add("", [("商家A", 100), ("商家B", 88), ("商家C", 166)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    chart_options.append(pie.dump_options())

    return chart_options

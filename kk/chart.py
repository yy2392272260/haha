#!usr/bin/python
# -*- coding: utf-8 -*-
#author:ly
from pyecharts import options as opts
from pyecharts.charts import Radar


v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]


def radar_base() -> Radar:
    c = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="销售", max_=6500),
                opts.RadarIndicatorItem(name="管理", max_=16000),
                opts.RadarIndicatorItem(name="信息技术", max_=30000),
                opts.RadarIndicatorItem(name="客服", max_=38000),
                opts.RadarIndicatorItem(name="研发", max_=52000),
                opts.RadarIndicatorItem(name="市场", max_=25000),
            ]
        )
        .add("预算分配", v1)
        .add("实际开销", v2)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Radar-基本示例"))
    )
    return c
c = radar_base()
c.render()
import plotly.express as px
import plotly.graph_objects as go


def bar_normalize_plot(csv, variable, normalizador, title, xaxis, yaxis):

    # Calculate and add the ratios Visited Count / base as a new column
    plot = go.Figure()

    aux = csv.groupby([variable, "id"])
    ans = aux["fitness"].agg(["min", "max", "mean"]).reset_index()
    base_values = ans[ans[variable] == normalizador].groupby("id")["mean"].max()
    ans["Ratio"] = ans.apply(lambda row: row["mean"] / base_values.get(row["id"], 1), axis=1)
    heuristics = csv.drop_duplicates(subset=[variable])

    for replace_type in heuristics[variable]:
        data = ans[ans[variable] == replace_type]
        plot.add_trace(go.Bar(name=replace_type, x=data["id"], y=data["Ratio"]))
    plot.update_layout(title=title,
                       xaxis=dict(title=xaxis),
                       yaxis=dict(title=yaxis))
    plot.show()

    return ans


def line_plot(csv, title):

    fig = px.line(csv, x="A", y="fitness", title=title)
    fig.show()

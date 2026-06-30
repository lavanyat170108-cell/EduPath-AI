import plotly.express as px

def create_risk_chart(high, medium, low):

    fig = px.pie(
        names=["High", "Medium", "Low"],
        values=[high, medium, low],
        title="Student Risk Distribution"
    )

    return fig.to_html(full_html=False)
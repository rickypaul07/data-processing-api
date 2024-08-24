import matplotlib.pyplot as plt
import uuid

def generate_visualization(df, chart_type, columns):
    fig, ax = plt.subplots()
    if chart_type == "histogram":
        df[columns].hist(ax=ax)
    elif chart_type == "scatter" and len(columns) == 2:
        df.plot.scatter(x=columns[0], y=columns[1], ax=ax)
    img_path = f"./uploads/{str(uuid.uuid4())}.png"
    fig.savefig(img_path)
    plt.close(fig)
    return img_path

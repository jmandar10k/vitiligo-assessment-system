import matplotlib.pyplot as plt
from typing import Dict


def create_pie_chart(section_scores: Dict[str, int]) -> str:

    # Remove zero scores
    filtered_scores = {k: v for k, v in section_scores.items() if v > 0}

    if not filtered_scores:
        return None

    labels = [label.capitalize() for label in filtered_scores.keys()]
    sizes = list(filtered_scores.values())

    # Modern soft color palette
    colors = [
        "#4C72B0",  # blue
        "#DD8452",  # orange
        "#55A868",  # green
        "#C44E52",  # red
        "#8172B2"   # purple
    ]

    # Explode slightly for visual separation
    explode = [0.03] * len(sizes)

    plt.figure(figsize=(7, 7))

    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        colors=colors[:len(sizes)],
        autopct="%1.1f%%",
        startangle=140,
        explode=explode,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
        shadow=False
    )

    # Style percentage text
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_weight("bold")
        autotext.set_color("black")

    # Style label text
    for text in texts:
        text.set_fontsize(11)

    plt.title(
        "Section-wise Score Distribution",
        fontsize=12,
        weight="bold"
    )

    plt.axis("equal")

    chart_path = "section_score_pie.png"
    plt.savefig(chart_path, bbox_inches="tight", dpi=300)
    plt.close()

    return chart_path
"""Matplotlib chart generation for the PDF report."""
import os
import matplotlib.pyplot as plt

CHART_PATH = "/tmp/report_chart.png"


def generate_chart(data: list[dict]) -> str:
    totals = {}
    for row in data:
        cat = row["category"]
        totals[cat] = totals.get(cat, 0) + row["amount"]

    categories = list(totals.keys())
    amounts = [totals[c] for c in categories]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(categories, amounts, color="#4C72B0")
    ax.set_title("Spending by Category")
    ax.set_ylabel("Amount ($)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_PATH)
    plt.close()

    return CHART_PATH

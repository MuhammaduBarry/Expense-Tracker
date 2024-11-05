import datetime

import typer
from typing_extensions import Annotated, Optional
from rich.console import Console
from rich.table import Table
from rich import print

from handle_os import increment_number, load_json, dump_json, json_file_path,get_month

app = typer.Typer()
console = Console()

@app.command()
def add(
    description: Annotated[str, typer.Option(..., help="Description for expense tracker")],
    amount: Annotated[float, typer.Option(..., help="Amount for expense tracker")]
):
    """Create a new expense tracker"""
    current_time = datetime.datetime.now().strftime("%m-%d %H:%M:%S") # Regular time format

    # Template for new task
    new_task = {
        "id": increment_number(),
        "date": current_time,
        "description": description,
        "amount": amount,
        "month": get_month()
    }

    data = load_json(json_file_path)
    data["list_of_expenses"].append(new_task)
    dump_json(data, json_file_path)

@app.command()
def list():
    """List current expenses"""
    data = load_json(json_file_path)
    if data["list_of_expenses"] == [] and data["amount_of_expenses"] == 0:
        print("[bold red]No data available to list currently, please use the[/bold red] [green]'add'[/green] [bold red]command[/bold red]")
        raise typer.Exit()

    table = Table("ID", "DATE", "DESCRIPTION", "AMOUNT")
    for expenses in data["list_of_expenses"]:
        table.add_row(f"{expenses["id"]}", expenses["date"], expenses["description"], f"${expenses['amount']:.2f}")
    console.print(table)

@app.command()
def summary(month: int = None):
    """Give a summary for entire expense or specific month"""
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    data = load_json(json_file_path)

    total_month_sum = 0
    total_sum = 0

    if month is not None:
        for expenses in data["list_of_expenses"]:
            if expenses["month"] == month:
                total_month_sum += expenses["amount"]
        print(f"[blue]Total expenses for {month_dict[month]}:[/blue] [green]${total_month_sum:.2f}[/green]")
    elif month is None:
        for expenses in data["list_of_expenses"]:
            total_sum += expenses["amount"]
        print(f"[blue]Total expenses for all months:[/blue] [green]${total_sum:.2f}[/green]")


if __name__ == "__main__":
    app()

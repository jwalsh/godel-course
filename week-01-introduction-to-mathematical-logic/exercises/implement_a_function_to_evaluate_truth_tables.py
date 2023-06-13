import click

def evaluate_truth_table(expression: str) -> None:
    """
    Evaluate the truth table of a given logical expression.

    Args:
        expression (str): The logical expression to evaluate.
    """
    click.echo(f"Truth table for '{expression}':")
    for p in [True, False]:
        for q in [True, False]:
            click.echo(f"P = {p}, Q = {q}, Expression Value = {eval(expression)}")

@click.command()
@click.option('--expression', type=str, default='p and q', help='Logical expression to evaluate.')
def cli(expression: str):
    evaluate_truth_table(expression)

if __name__ == "__main__":
    cli()

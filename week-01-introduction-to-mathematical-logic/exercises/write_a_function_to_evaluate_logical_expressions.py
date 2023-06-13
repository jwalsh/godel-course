import click

def evaluate_logical_expression(expression: str, p: bool, q: bool) -> bool:
    """
    Evaluate a logical expression for given values of propositions.

    Args:
        expression (str): The logical expression to evaluate.
        p (bool): Proposition P.
        q (bool): Proposition Q.

    Returns:
        bool: The value of the expression after evaluation.
    """
    result = eval(expression)
    click.echo(f"Expression '{expression}' with P = {p}, Q = {q} evaluates to {result}")
    return result

@click.command()
@click.option('--expression', type=str, default='p and q', help='Logical expression to evaluate.')
@click.option('--p', type=bool, default=True, help='Proposition P.')
@click.option('--q', type=bool, default=True, help='Proposition Q.')
def cli(expression: str, p: bool, q: bool):
    evaluate_logical_expression(expression, p, q)

if __name__ == "__main__":
    cli()

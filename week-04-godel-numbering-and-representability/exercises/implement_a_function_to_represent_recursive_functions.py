import click

@click.command()
@click.argument('n', type=int)
def recursive_factorial(n: int) -> int:
    """
    Calculate and return the factorial of n using a recursive function.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of n.
    """
    # A basic implementation of a recursive function to calculate the factorial of n.
    if n == 0:
        return 1
    factorial_result = n * recursive_factorial(n - 1)
    return factorial_result

@click.command()
@click.argument('n', type=int)
def cli(n: int):
    """
    CLI wrapper for the recursive_factorial function.

    Args:
        n (int): The number for which to calculate the factorial.
    """
    factorial_result = recursive_factorial(n)
    click.echo(f"Factorial of {n}: {factorial_result}")

if __name__ == "__main__":
    cli()

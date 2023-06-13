import click

def explore_logical_equivalences(p: bool, q: bool) -> None:
    """
    Explore logical equivalences between different logical expressions.

    Args:
        p (bool): Proposition P.
        q (bool): Proposition Q.
    """
    click.echo(f"Propositions: P = {p}, Q = {q}")
    click.echo(f"De Morgan's Law: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q -> {not (p and q)} ≡ {not p or not q}")
    click.echo(f"Distributive Law: P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R) -> {p or (q and False)} ≡ {(p or q) and (p or False)}")

@click.command()
@click.option('--p', type=bool, default=True, help='Proposition P.')
@click.option('--q', type=bool, default=True, help='Proposition Q.')
def cli(p: bool, q: bool):
    explore_logical_equivalences(p, q)

if __name__ == "__main__":
    cli()

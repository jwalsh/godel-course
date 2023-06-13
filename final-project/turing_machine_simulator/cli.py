import click
from turing_machine import TuringMachine


@click.command()
@click.option("--tape", type=str, help="Initial tape input for the Turing machine.")
@click.option(
    "--states", type=str, help="Comma-separated list of states for the Turing machine."
)
@click.option(
    "--transition-function",
    type=str,
    help="Transition function for the Turing machine.",
)
def simulate(tape: str, states: str, transition_function: str) -> None:
    """
    Simulate a Turing machine with the given parameters.

    :param tape: Initial tape input for the Turing machine.
    :param states: Comma-separated list of states for the Turing machine.
    :param transition_function: Transition function for the Turing machine.
    """
    tape = list(tape)
    states = states.split(",")
    transition_function = [tuple(t.split(",")) for t in transition_function.split(";")]

    tm = TuringMachine(tape, states, transition_function)
    tm.run()


def test_turing_machine():
    print("Test 1: ")
    tape = ["1", "0", "1", "1"]
    states = ["q0", "q1", "qHalt"]
    transition_function = [
        ("q0", "1", "q1", "0", "R"),
        ("q1", "0", "q1", "1", "R"),
        ("q1", "1", "qHalt", "1", "R"),
    ]
    tm = TuringMachine(tape, states, transition_function)
    print(tm)
    tm.run()
    print(tm)

    print("Test 2: ")

    tape = ["1", "0", "1", "1"]
    states = ["q0", "q1", "qHalt"]
    transition_function = [
        ("q0", "1", "q1", "0", "R"),
        ("q1", "0", "q1", "1", "R"),
        ("q1", "1", "qHalt", "1", "R"),
        ("q1", "0", "qHalt", "0", "R"),
    ]
    tm = TuringMachine(tape, states, transition_function)
    print(tm)
    tm.run()
    print(tm)

    print("Test 3: ")
    tape = ["0", "0", "0", "0"]
    states = ["q0", "q1", "qHalt"]
    transition_function = [
        ("q0", "0", "q1", "1", "R"),
        ("q1", "0", "q1", "0", "R"),
        ("q1", "1", "qHalt", "1", "R"),
    ]
    tm = TuringMachine(tape, states, transition_function)
    print(tm)
    tm.run()
    print(tm)


if __name__ == "__main__":
    print("Running tests...")
    test_turing_machine()

    print("Running Turing machine...")
    simulate()

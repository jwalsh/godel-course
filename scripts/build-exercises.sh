#!/bin/bash

# Function to create exercises for a given week
create_exercises() {
    local week_directory="$1"
    local exercise_descriptions=("${!2}")

    # Create the week directory if it doesn't exist
    if [ ! -d "${week_directory}" ]; then
        mkdir -p "${week_directory}"
    fi
    # Change to the week directory
    cd "${week_directory}"

    # Add a default slides.org file if it doesn't exist
    if [ ! -f slides.org ]; then
        echo "#+TITLE: Slides" >slides.org
    fi

    # Create :NOTER_DOCUMENT: notes.org files for each exercise
    if [ ! -f notes.org ]; then
        echo "#+TITLE: Notes" >notes.org
    fi

    # Use org-mode for lecture-notes.md
    if [ -f lecture-notes.md ]; then
	mv lecture-notes.md lecture-notes.org
    fi

    # Create the exercises directory if it doesn't exist
    mkdir -p exercises

    # Change to the exercises directory
    cd exercises

    # Loop through the array and create Python files for each exercise
    for exercise_description in "${exercise_descriptions[@]}"; do
        # Convert the description to a directory-safe filename
        exercise_filename=$(echo "${exercise_description}" | tr '[:upper:]' '[:lower:]' | tr ' ' '_').py
        echo "# ${exercise_description}" >"${exercise_filename}"
    done

    # Return to the root directory
    cd ../../
}

# Define arrays with exercise descriptions for each week
week1_exercises=(
    "Implement a function to evaluate truth tables"
    "Write a function to evaluate logical expressions"
    "Create a function to explore logical equivalences"
)

week2_exercises=(
    "Implement a simple theorem prover for propositional logic"
    "Represent first-order formulas in Python"
    "Evaluate first-order formulas using an interpretation"
)

# ... (existing content of build_exercises.sh) ...

# Define arrays with exercise descriptions for Weeks 3, 4, and 5
week3_exercises=(
    "Implement a Turing machine simulator in Python"
    "Design a Turing machine to recognize palindromes"
    "Explore examples of decidable and undecidable problems"
)

week4_exercises=(
    "Generate Gödel numbers for formulas in Python"
    "Implement a function to represent recursive functions"
    "Construct a self-referential Gödel sentence"
)

week5_exercises=(
    "Understand and implement the proof of Gödel's First Incompleteness Theorem"
    "Explore the implications and consequences of the theorem"
    "Discuss limitations of formal systems and consistency proofs"
)

# ... (existing content of build_exercises.sh) ...

# Define arrays with exercise descriptions for Weeks 6 to 12
week6_exercises=(
  "Understand and implement the proof of Gödel's Second Incompleteness Theorem"
  "Discuss the implications for formal systems and consistency proofs"
)

week7_exercises=(
  "Explore the Church-Turing Thesis and its implications"
  "Implement lambda expressions and basic evaluation rules in Python"
)

week8_exercises=(
  "Prove the undecidability of the Halting Problem"
  "Explore reductions and other examples of undecidable problems"
)

week9_exercises=(
  "Introduction to computational complexity theory"
  "Implement and analyze algorithms for NP-complete problems"
)

week10_exercises=(
  "Implement set operations and explore infinite sets in Python"
  "Understand the Continuum Hypothesis and its independence"
)

week11_exercises=(
  "Explore model theory and the concept of nonstandard models"
  "Implement structures and interpretations in Python"
)

week12_exercises=(
  "Review key concepts and themes from the course"
  "Design and implement a final project related to course topics"
)



# Create exercises for Week 1 and Week 2
create_exercises "week-01-introduction-to-mathematical-logic" "week1_exercises[@]"
create_exercises "week-02-first-order-logic-and-formal-systems" "week2_exercises[@]"
# Create exercises for Weeks 3, 4, and 5
create_exercises "week-03-computability-and-turing-machines" "week3_exercises[@]"
create_exercises "week-04-godel-numbering-and-representability" "week4_exercises[@]"
create_exercises "week-05-godels-first-incompleteness-theorem" "week5_exercises[@]"
# Create exercises for Weeks 6 to 12
create_exercises "week-06-godels-second-incompleteness-theorem" "week6_exercises[@]"
create_exercises "week-07-church-turing-thesis-and-lambda-calculus" "week7_exercises[@]"
create_exercises "week-08-halting-problem-and-undecidability" "week8_exercises[@]"
create_exercises "week-09-complexity-theory-and-p-vs-np" "week9_exercises[@]"
create_exercises "week-10-set-theory-and-continuum-hypothesis" "week10_exercises[@]"
create_exercises "week-11-model-theory-and-nonstandard-models" "week11_exercises[@]"
create_exercises "week-12-course-summary-and-final-project" "week12_exercises[@]"

Feature: Simple polynomial root solver
    Scenario Outline: Zero order polynomial
        Given a function <function>
        When asked to find roots
        Then the roots are <roots>

    Examples: Zero order
    | function | roots |
    | 0 | all |
    | 4 | undefined |

    Scenario Outline: Higher order polynomial
        Given a function <function>
        When asked to find roots for a guess <guess>
        Then the roots are <roots>

    Examples: Higher order
    | function | guess | roots |
    | -2,-1.5,0.75,0.25 | 10 | 2 |
    | -2,-1.5,0.75,0.25 | -1 | -1 |
    | -2,-1.5,0.75,0.25 | -10 | -4 |

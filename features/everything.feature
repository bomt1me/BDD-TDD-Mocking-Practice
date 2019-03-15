Feature: Simple polynomial newton solver
    Scenario Outline: Zero order polynomial
        Given a zero order function <function>
        When asked to find roots
        Then the roots are <roots>

    Examples: Zero order
    | function | roots |
    | [0] | ["all"] |
    | [4] | ["undefined"] |

    Scenario Outline: First order polynomial
        Given a first order function <function>
        When asked to find roots
        Then the roots are <roots>

    Examples: First order
    | function | roots         |
    | [0, 0]   | ["all"]       |
    | [4, 0]   | ["undefined"] |
    | [0, 1]   | [0]           |
    | [2, 4]   | [-0.5]        |
    | [-3, 12] | [1/4]         |

    Scenario Outline: Second order and above
        Given a greater than first order function <function>
        When asked to find roots
        Then the roots are <roots>

    Examples: Greater than first order
    | function             | roots       |
    | [1, 2, 3, 4]         | [-0.60583]  |
    | [5, -2, 0, -4]       | [0.92371]   |
    | [-2, -3/2, 3/4, 1/4] | [-4, -1, 2] |

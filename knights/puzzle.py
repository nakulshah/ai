from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
ATrue = Symbol("A is telling the truth")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
BTrue = Symbol("B is telling the truth")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# # Puzzle 0
# # A says "I am both a knight and a knave."
# knowledge0 = And(
#     general_knowledge,
#     Implication(AKnight, And(AKnight, AKnave)),
#     Implication(AKnave, Not(And(AKnight, AKnave)))
# )

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)

P = Symbol("It is a Tuesday.")
Q = Symbol("It is raining.")
R = Symbol("Harry will go for a run.")

knowledgeTest = And(
    Implication((And(P, Not(Q))), R),
    And(P),
    And(Not(Q))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]

    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol} is true")


    # print(R.name + " is " + str(model_check(knowledgeTest, R)))
if __name__ == "__main__":
    main()

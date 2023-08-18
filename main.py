# -*- coding: utf-8 -*-
"""
  " Manages the running of all Eular Problems
  """
import importlib


def separator():
    print('_' * 80)


SOLVED = ("eular_001",
          # "eular_002",, # TODO: Fix bug
          "eular_003",
          "eular_004",
          "eular_005",  # Takes too long
          "eular_006",
          "eular_007",
          "eular_008",
          "eular_009",
          "eular_010",
          "eular_011",
          # "eular_012",  # Takes too long
          "eular_013",
          "eular_014",
          "eular_015",
          "eular_016",
          "eular_017",
          "eular_018",
          "eular_019",
          "eular_020",
          "eular_021",
          "eular_022",
          "eular_023",
          "eular_024",
          "eular_025",

          # "eular_030", # TODO: Fix bug
          )


class EularProblem(object):
    def __init__(self, pname):
        self.num = pname
        self.module = 'src.' + pname

        self.mod = importlib.import_module(self.module)

        self.desc = self.mod.DESC
        self.question = self.mod.__doc__
        self.solution = self.mod.SOLUTION

        self.attempt = 'Unsolved.'
        self.time = 'Unsolved.'

    def solve(self):
        self.attempt, self.time = self.mod.solve()


def main():
    print("Programming Challenges")
    print("Author: Erik Lunna")
    print('\n')

    fields = ('Problem', 'Description', 'Time(sec)', 'Solution', 'Passed')
    fmt_str1 = '{:10} {:30} {:12} {:20} {:5}'
    print(fmt_str1.format(*fields))

    fmt_str2 = '{:<10} {:<30} {:<12.5f} {:<20} {:<5}'
    for pname in SOLVED:
        problem = EularProblem(pname)
        problem.solve()
        passed = problem.solution == problem.attempt
        print(fmt_str2.format(
            problem.num,
            problem.desc,
            problem.time,
            problem.solution,
            str(passed)
        ))


if __name__ == "__main__":
    main()

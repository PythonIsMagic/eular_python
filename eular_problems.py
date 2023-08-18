# -*- coding: utf-8 -*-
"""
  " Manages the running of all Eular Problems
  """
import importlib


def separator():
    print('_'*80)


SOLVED = (1,
          #2, # TODO: Fix bug
          3, 4,
          5, #Takes too long
          6, 7, 8, 9, 10,
          11,
          12, #Takes too long
          13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, #30
          )



class EularProblem(object):
    def __init__(self, num):
        self.num = num
        self.module = 'problems.problem' + str(num)

        self.mod = importlib.import_module(self.module)

        self.desc = self.mod.DESC
        self.question = self.mod.__doc__
        self.solution = self.mod.SOLUTION

        self.attempt = 'Unsolved.'
        self.time = 'Unsolved.'

    def solve(self):
        self.attempt, self.time = self.mod.solve()


def main():
    print("Eular Problems!")
    print('\n')

    fields = ('#', 'Description', 'Time(sec)', 'Solution', 'Passed')
    fmt_str1 = '{:4} {:30} {:15} {:20} {:5}'
    print(fmt_str1.format(*fields))

    fmt_str2 = '{:<4} {:<30} {:<15.10f} {:<20} {:<5}'
    for f in SOLVED:
        problem = EularProblem(f)
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

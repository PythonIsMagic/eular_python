import random
import logging

BIRTHDAY = 1
PEOPLE = 25
PARTYS = 100000
SAME_BIRTHDAYS = 0

LOG_FILENAME = 'test.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG)

if __name__ == "__main__":
    print('~~~~~~~~~~~~~~~~~~~~~\n')
    for i in range(PARTYS):
        birthdays = [random.randint(1, 365) for i in range(PEOPLE)]
        same = birthdays.count(BIRTHDAY)

        # if BIRTHDAY in birthdays:
        #	SAME_BIRTHDAYS += 1
        if same >= 2:
            SAME_BIRTHDAYS += 1

print('Ran {} parties with {} people'.format(PARTYS, PEOPLE + 1))
print('At {} parties, there was someone with the same birthday.'.format(SAME_BIRTHDAYS))

percent = (SAME_BIRTHDAYS / PARTYS) * 100

print('{}% of parties had someone with the same birthday!'.format(percent))

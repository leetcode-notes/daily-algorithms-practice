from typing import List
from collections import Counter, defaultdict
all_people = [{'name': 'Reuven', 'age': 48, 'hobbies': ['Python', 'cooking', 'reading']},
              {'name': 'Atara', 'age': 17, 'hobbies': [
                  'horses', 'cooking', 'art', 'reading']},
              {'name': 'Shikma', 'age': 15, 'hobbies': [
                  'Python', 'piano', 'cooking', 'reading']},
              {'name': 'Amotz', 'age': 13, 'hobbies': ['biking', 'cooking']}]


class Person:
    def __init__(self, name, hobbies: List[str], age: int) -> None:
        self.name = name
        self.hobbies = hobbies
        self.age = age


def parse_data(data) -> List[Person]:
    people = []
    for entry in data:
        person = Person(entry['name'], entry['hobbies'], entry['age'])
        people.append(person)
    return people


class solution:

    def __init__(self) -> None:
        pass

    @staticmethod
    def average_age_under(people_data, max_age=None) -> float:
        people = parse_data(people_data)
        age_sum = 0
        n = len(people)
        if n == 0:
            return 0
        if max_age is None:
            for person in people:
                age_sum += person.age
            return age_sum
        else:
            n = 0
            for person in people:
                if person.age < max_age:
                    n += 1
                    age_sum += person.age
            return age_sum / n if n > 0 else 0

    @staticmethod
    def all_hobbies(people_data) -> set:
        people = parse_data(people_data)
        hobby_set = set()
        for person in people:
            for hobby in person.hobbies:
                hobby_set.add(hobby)
        return hobby_set

    @staticmethod
    def hobby_counter(people_data) -> Counter:
        people = parse_data(people_data)
        hobby_counts = Counter()
        for person in people:
            for hobby in person.hobbies:
                hobby_counts[hobby] += 1
        return hobby_counts

    @staticmethod
    def n_most_common(people_data, n):
        hobby_counts = solution.hobby_counter(people_data)
        counts_hobbies = defaultdict(set)
        max_count = 0
        for hobby, count in hobby_counts.items():
            max_count = max(max_count, count)
            counts_hobbies[count].add(hobby)
        res = []

        while n > 0 and max_count > 0:
            if max_count in counts_hobbies:
                for hobby in counts_hobbies[max_count]:
                    n -= 1
                    res.append(hobby)
                    if n == 0:
                        break
                max_count -= 1
            else:
                max_count -= 1
        return res


'''
Return a set of the different hobbies enjoyed by people in our database.

Return a Counter object indicating how many people have each hobby - - that is , how many people are interested in Python, how many enjoy cooking, and so forth.  (I know, in an ideal world, everyone would love Python.  But hey, they're my children, so I'll forgive them.  For now.)
Return the n most common hobbies, as a list of strings.

Hint: Nested list comprehensions and the Counter class will make this much easier!
'''

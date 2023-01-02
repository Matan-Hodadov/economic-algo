# task 9, Matan Hodadov
from typing import *


def conditioned_utilitarian_budget(total: float, subjects: List[str], preferences: List[List[str]]):
    # At first, I solved this question using only subjects like char ('a', 'b', etc.)
    # So when I noticed it, I decided to save a copy of the original names (will be used later)
    # Here i changed the subjects and preferences lists names to 'a', 'b' etc respectively (easier to use)
    subjects_origin = subjects.copy()  # save a copy of the list with the original names
    # change names in subjects
    for i in range(len(subjects)):
        subjects[i] = chr(i+97)
        # change names in preferences
    for person in preferences:
        for preference in person:
            person[person.index(preference)] = chr(subjects_origin.index(preference) + 97)

    # we "changed" the subjects names to "a", "b" etc
    # thats why we can use ord(names) - 97 to get the correct index. we will se that a lot later

    # initiate variables
    total_subject_support = [0] * len(subjects)  # count total supports for each subject
    money_per_person = total / len(preferences)  # money for each person
    total_money_pool = [0] * len(subjects)  # how much money for each subject in total

    # add the supporters to each subject
    for person in preferences:
        for preference in person:
            total_subject_support[ord(preference) - 97] += 1  # using the change of names to get the index

    for person in preferences:  # for each person calc the budget for each subject
        max_other_supports = 0  # look for the max amount of supports
        max_other_supports_subjects = []  # the subject with the max amount of supports
        for preference in person:
            # if support is bigger the current max support
            if total_subject_support[ord(preference) - 97] - 1 > max_other_supports:
                # change max support amount
                max_other_supports = total_subject_support[ord(preference) - 97] - 1
                # change max support subject to current subject
                max_other_supports_subjects = [preference]
            # else if the amount of supports is equals
            elif total_subject_support[ord(preference) - 97] - 1 == max_other_supports:
                max_other_supports_subjects += preference  # add current subject to support subject list
        for add_money_to in max_other_supports_subjects:  # for each subject in the support subject list
            # use the changed name for the index
            # add to this index the money divided by the number of subjects in the support list
            total_money_pool[ord(add_money_to)-97] += money_per_person/len(max_other_supports_subjects)
            print("Citizen", preferences.index(person), "gives", money_per_person / len(max_other_supports_subjects),
                  "to", subjects_origin[ord(add_money_to)-97])  # use subjects_origin to get the origin name
    print("subjects:", subjects_origin)
    print("budget:", total_money_pool)

# example 1
total = 500
subjects = ["security", "basketball", "education", "companies"]
preferences = [['basketball', 'companies'], ['security', 'education'], ['security', 'companies'], ['basketball', 'education'], ['security']]
conditioned_utilitarian_budget(total, subjects, preferences)

print("\n-------------------------------\n")

# example 2
total = 500
subjects = ["security", "basketball", "education", "companies"]
preferences = [['security', 'basketball'], ['security', 'education'], ['security', 'companies'], ['basketball', 'education'], ['security']]
conditioned_utilitarian_budget(total, subjects, preferences)

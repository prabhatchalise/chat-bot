import re
import topic
import databaseOperation


def add_to_faq(question, answer):

    databaseOperation.insert_answer(question, answer)

    noOfRows = databaseOperation.no_of_rows

    subj, root, obj = topic.topic(question)

    databaseOperation.insert_subject(subj, noOfRows + 1)
    databaseOperation.insert_subject(root, noOfRows + 1)
    databaseOperation.insert_subject(obj, noOfRows + 1)


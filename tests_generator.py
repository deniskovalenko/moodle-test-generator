import random
import time 
"""
Generates test case in Moodle-compatible format, like:
Питання:
{
=Правильна відповідь
~Відповідь
~Відповідь
~Відповідь
}

Correct answer is in random place
"""
def generate_test_case(question, answer, other_options):
    options_with_symbol = ["~" + option for option in other_options]
    answer_with_symbol_of_correct_answer = "=" + answer
    options_with_symbol.append(answer_with_symbol_of_correct_answer)
    random.shuffle(options_with_symbol)
    rendered_answers = "\n".join(options_with_symbol)
    template = f'''{question}:\n{{\n{rendered_answers}\n}}

'''
    return template


expected = """Мой вопрос: кто лучше, Денис или Васz?:
{
=Денис конечно
~Вася
~Терешкова
~Путин
}

"""
random.seed(1)
actual = generate_test_case("Мой вопрос: кто лучше, Денис или Васz?", "Денис конечно", ["Вася", "Путин", "Терешкова"])
#print(actual)
#print(expected)
assert actual == expected


def parse_tsv_record(tsv_string):
    tokens = tsv_string.split("\t")
    question = tokens[0]
    answer = tokens[1]
    options = tokens[2:]
    return question, answer, options


t = 1000 * time.time()
#to cancel out fixed random seed
random.seed(int(t) % 2**32) 

filename = "tests_jessie.tsv"
#read the file
#for each test case, generate moodle-compatible string
#append test_case to output file:

with open(filename, "r") as tsv:
  tsv_lines = [line.strip() for line in tsv.readlines()]
  questions_without_header = tsv_lines[1:]
  print(questions_without_header)
  result_string = ""
  for test_case in questions_without_header:
      question, answer, options = parse_tsv_record(test_case)
      new_line = generate_test_case(question=question, answer=answer, other_options=options)
      result_string += new_line

  print(result_string)
  
  with open("output.txt", "w") as outfile:
    outfile.write(result_string)



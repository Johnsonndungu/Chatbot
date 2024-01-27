#Imports the function get from difflib.The function is used to get close match in a word.
from difflib import get_close_matches 
#Imports py in built module json which provides json encoding of data.
import json

#load_knowledge_base takes a file path as input and returns dictionary.
def load_knowledge_base(file_path : str) -> dict:
# This opens the specific file in read mode and ensures the file is closed after open.
 with open(file_path, 'r') as file:
    data: dict = json.load(file)
 return data

def save_knowlwdge_base(file_path : str, data: dict):
# opens json file in write mode
  with open(file_path, 'w') as file:
# json.dump writes content of dictionary data to the file in json format
    json.dump(data, file, indent=2)

def file_best_match(user_question : str, questions:list[str]) -> str | None:
  matches: list = get_close_matches(user_question, questions, n=1,cutoff=0.6)
  return matches [0] if matches else None

def get_answer_for_question(question:str ,knowledge_base: dict) -> str | None:
  for q in knowledge_base ['questions']:
    if q['question']== question:
      return q['answer']
    

def chat_box():
  knowledge_base: dict = load_knowledge_base('knowledge_base.json')

  while True:
    user_input: str = input('You: ')

    if user_input.lower() == 'quit':
      break

    best_match: str | None = file_best_match(user_input,[q['question'] for q in knowledge_base['questions']])
    if best_match:
      answer: str = get_answer_for_question(best_match, knowledge_base)
      print(f'Bot:{answer}')
    else:
      print('Bot:I dont know the answer,can you teach me?')
      new_answer: str = input('You; Type the answer or "skip" to skip: ')

      if new_answer.lower() != 'skip':
        knowledge_base['questions']. append({'question': user_input, 'answer': new_answer})
        save_knowlwdge_base('knowledge_base.json', knowledge_base)
        print('Bot: Thank you!')

if __name__ == '__main__':
  chat_box() 
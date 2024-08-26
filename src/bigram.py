import string, random

DATASET_PATH = "./datasets/shakespeare.txt"

def main() -> None:
  lines = []

  with open(DATASET_PATH, "r") as f:
    lines = f.readlines()

  successor_map = {}
  window = []

  for line in lines:
    for word in line.split():
      clean_word = word.strip(string.punctuation).lower()
      window.append(clean_word)
      
      if len(window) == 2:
        key = window[0]
        value = window[1]
        if key in successor_map:
          successor_map[key].append(value)
        else:
          successor_map[key] = [value]
        window.pop(0)

  word = "the"
  print(word, end=' ')

  for _ in range(15):
    successors = successor_map[word]
    word = random.choice(successors)
    print(word, end=' ')

  print("")


if __name__ == "__main__":
  main()

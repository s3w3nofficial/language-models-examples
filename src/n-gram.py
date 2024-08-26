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
      
      if len(window) == 3:
        key = (window[0], window[1])
        value = window[2]
        if key in successor_map:
          successor_map[key].append(value)
        else:
          successor_map[key] = [value]
        window.pop(0)

  word1 = "the"
  word2 = "broken"
  print(word1, end=' ')
  print(word2, end=' ')

  for _ in range(15):
    successors = successor_map[(word1, word2)]
    word3 = random.choice(successors)
    word1, word2 = word2, word3
    print(word3, end=' ')

  print("")


if __name__ == "__main__":
  main()

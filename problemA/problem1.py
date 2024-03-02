sequence = input().upper()
c = sequence.count('C')
g = sequence.count('G')
bases = c + g
number = ((bases / len(sequence)) * 100)
percent = round(number, 2)
print(f"{percent}%")
shimmy = int(input())
aerials = []
for i in range(shimmy):
    suey = input()
    aerials.append(suey)
bounce = sorted(aerials)
prisonSong = bounce[::-1]
if aerials == bounce:
    print("Ascending")
elif aerials == prisonSong:
    print("Descending")
else:
    print("Unordered")
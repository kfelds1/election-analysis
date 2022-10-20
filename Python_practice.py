counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
    print("turn on the AC.")

else:
    print("Open the windows.")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties_dict = {"Arapahoe":"432843", "Denver":"428573","Jefferson":"348395"}

x=0

while x<= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)


for county, voters in counties_dict.items():

    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


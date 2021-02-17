icc_test_wc_data={
    "England":{"id": "England", "pct": 70.2, "points": 442, "series": 6, "won": 11, "lost": 4, "drawn": 3},
    "New Zealand":{"id": "New Zealand", "pct": 70.0, "points": 420, "series": 5, "won": 7, "lost": 4, "drawn": 0},
    "Australia":{"id": "Australia", "pct": 69.2, "points": 332, "series": 4, "won": 8, "lost": 4, "drawn": 2},
    "India":{"id": "India", "pct": 68.3, "points": 430, "series": 6, "won": 9, "lost": 4, "drawn": 1},
    "Pakistan":{"id": "Pakistan", "pct": 43.3, "points": 286, "series": 5.5, "won": 4, "lost": 5, "drawn": 3},
    "West Indies":{"id": "West Indies", "pct": 33.3, "points": 160, "series": 4, "won": 3, "lost": 6, "drawn": 0},
    "South Africa": {"id": "South Africa", "pct": 30.0, "points": 144, "series": 4, "won": 3, "lost": 8, "drawn": 0},
    "Sri Lanka": {"id": "Sri Lanka", "pct": 16.7, "points": 80, "series": 4, "won": 1, "lost": 6, "drawn": 1},
    "Bangladesh": {"id": "Bangladesh", "pct": 0.0, "points": 0, "series": 2.5, "won": 0, "lost": 5, "drawn": 0},

}
for team in icc_test_wc_data:
    #print points of each team
    print(icc_test_wc_data[team]["id"]," - ",icc_test_wc_data[team]["points"])
    won=icc_test_wc_data[team]["won"]
    if(won>5):
        # print("more than 5 matches won")
        print(icc_test_wc_data[team]["id"]," ",icc_test_wc_data[team]["won"])

#print details according to input value
per=float(input("Enter percentage"))
for data in icc_test_wc_data:
    perc=float(icc_test_wc_data[data]["pct"])
    if perc >= per:
        print(icc_test_wc_data[data]["id"]," ",icc_test_wc_data[data]["pct"])
    else:
        pass
        break
#print details based on input
id=input("Enter a team name")
property=input("Enter property")
if id in icc_test_wc_data:
    if property in icc_test_wc_data[id]:
        print(icc_test_wc_data[id]["id"],icc_test_wc_data[id][property])
    else:
        print(icc_test_wc_data[id]["id"],"\n",property,"Not found")
else:
    print("Team not found")
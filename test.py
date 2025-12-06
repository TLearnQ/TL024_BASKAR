

#q27

# import json, yaml
# def process_file(inp, out):
#     if inp.endswith(".json"):
#         data = json.load(open(inp))
#     else:
#         data = yaml.safe_load(open(inp))

#     json.dump(data, open(out, "w"), indent=2)
#     print("Saved:", out)

# process_file("network.yaml", "clean.txt")



#q26




# database = {"items": []}
# def get_items():
#     return database["items"]

# def post_items(payload):
#     if not isinstance(payload, dict):
#         return {"error": "Invalid payload"}
#     database["items"].append(payload)
#     return {"status": "added"}

# def router(request, payload=None):
#     try:
#         method, path = request.split()
#     except ValueError:
#         return {"error": "Bad request format"}

#     if path != "/items":
#         return {"error": "Unknown path"}

#     if method == "GET":
#         return get_items()
#     elif method == "POST":
#         return post_items(payload)
#     else:
#         return {"error": "Invalid method"}

# print(router("GET /items"))
# print(router("POST /items", {"id": 1, "name": "Test"}))








#q28
# machines = [
#     {"id": 1, "cpu": 45, "users": 1},
#     {"id": 2, "cpu": 67, "users": 3},
#     {"id": 3, "cpu": 89, "users": 6},
#     {"id": 4, "cpu": 23, "users": 0},
#     {"id": 5, "cpu": 56, "users": 2}
# ]

# def classify_machine(machine):
#     cpu = machine["cpu"]
#     users = machine["users"]


#     if cpu < 30 and users == 0:
#         label = "Idle"
#     elif cpu < 60 and users <= 2:
#         label = "Normal"
#     elif cpu < 85 and users <= 5:
#         label = "Busy"
#     else:
#         label = "Overloaded"

#     return label


# results = []
# for m in machines:
#     label = classify_machine(m)
#     results.append({"id": m["id"], "cpu": m["cpu"], "users": m["users"], "label": label})

# for r in results:
#     print(f"Machine {r['id']}: CPU={r['cpu']}%, Users={r['users']} → {r['label']}")


# with open("lab_report.txt", "w") as f:
#     for r in results:
#         f.write(f"Machine {r['id']}: {r['label']}\n")






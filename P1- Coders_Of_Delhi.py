import pandas as pd

# --- Task 1: Identify Issues in the Data(using Only Python) ---

# data2 = {
#     "users": [
#         {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
#         {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
#         {"id": 3, "name": "", "friends": [1], "liked_pages": [101, 103]},
#         {"id": 4, "name": "Sara", "friends": [2, 2], "liked_pages": [104]},
#         {"id": 5, "name": "Amit", "friends": [], "liked_pages": []}
#     ],
#     "pages": [
#         {"id": 101, "name": "Python Developers"},
#         {"id": 102, "name": "Data Science Enthusiasts"},
#         {"id": 103, "name": "AI & ML Community"},
#         {"id": 104, "name": "Web Dev Hub"},
#         {"id": 104, "name": "Web Development"}
#     ]
# }

# df = pd.DataFrame(data2)

# def clean_data(data2):
#     data2['users'] = [user for user in data2['users'] if user['name'].strip()]

#     for user in data2['users']:
#         user['friends'] = list(set(user['friends']))

#     data2['users'] = [user for user in data2['users'] if user['name'] and user['friends']]

#     unique_pages = {}
#     for page in data2['pages']:
#         unique_pages[page['id']] = page
#     data2['pages'] = list(unique_pages.values())

#     return str(data2)

# data = clean_data(data2)
# with open('data.csv', 'w') as f:
#     data = f.write(data)


# --- Task 2: Load the User Data ---
# --- Task 2: Read and Display the Data using Python ---

df = pd.read_csv('data.csv')
print(df)
# def show_data(data):
#     print('This is a Users Data!')
#     for user in data['users']:
#         print(f"ID {user['id']} - Name {user['name']}, Friends {user['friends']}, Like Pages = {user['liked_pages']}")

#     print('\nThis is a Pages Data!')
#     for page in data['pages']:
#         print(f"ID {page['id']} - Name {page['name']}")

# show_data(data)

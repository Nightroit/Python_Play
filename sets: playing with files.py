st = set()

for i in range(3):
    with open(f'file{i+1}.txt') as file:
        st.add(file)

print(st)

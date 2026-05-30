with open('/home/itzksv/Mine/my_codes/practice/project/w/neuro-infotech.html', 'r') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'id="about"' in l or 'Who We Are' in l or 'av-row' in l:
        print(f"{i+1}: {l.strip()}")

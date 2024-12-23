data = {}

file = open('sorted_data.txt', 'r')

for line in file:
    if line.strip() == "" or line.startswith("TA"):
        continue
    
    parts = line.strip().split(', ')
    student = parts[0]
    action = parts[1]
    gate = parts[2]
    time = parts[3]
    
    if student not in data:
        data[student] = {'records': [], 'inside': False}
    
    if action == "ENTER" and not data[student]['inside']:
        data[student]['records'].append((gate, action, time))
        data[student]['inside'] = True
    elif action == "EXIT" and data[student]['inside']:
        data[student]['records'].append((gate, action, time))
        data[student]['inside'] = False
    elif action == "EXIT" and not data[student]['inside']:
        data[student]['records'].append((gate, action, time))

file.close()

def check_status(student):
    if student in data:
        print(f"Records for {student}: {data[student]['records']}")
        print(f"Currently inside: {'Yes' if data[student]['inside'] else 'No'}")
    else:
        print("No records for this student.")

def check_time_range(start, end):
    entries = []
    for student, info in data.items():
        for record in info['records']:
            if start <= record[2] <= end:
                entries.append((student, record))
    print(f"Records between {start} and {end}: {entries}")

def check_gate(gate_num):
    gate_count = {'ENTER': 0, 'EXIT': 0}
    for info in data.values():
        for record in info['records']:
            if record[0] == gate_num:
                gate_count[record[1]] += 1
    print(f"Gate {gate_num} - Entries: {gate_count['ENTER']}, Exits: {gate_count['EXIT']}")

while True:
    student_name = input("Enter student name (or press Enter to quit): ")
    if not student_name:
        break
    check_status(student_name)

    time_range = input("Enter time range (HH:MM to HH:MM): ").split(' to ')
    if len(time_range) == 2:
        check_time_range(time_range[0], time_range[1])
    else:
        print("Invalid time range format.")

    gate_num = input("Enter gate number: ")
    if gate_num:
        check_gate(gate_num)
    else:
        print("No gate number provided.")

# TEST CASES

data_test = {
    'Rishabh Oberoi': {'records': [('Gate5', 'ENTER', '14:39:14'), ('Gate5', 'EXIT', '14:42:46'), ('Gate5', 'ENTER', '14:43:15'), ('Gate5', 'EXIT', '14:43:44')], 'inside': False},
    'Gayam Shivakanth Reddy': {'records': [('Gate3', 'EXIT', '14:39:16'), ('Gate3', 'ENTER', '14:43:05')], 'inside': False},
    'Shraman Jain': {'records': [('Gate1', 'ENTER', '14:39:17')], 'inside': True},
    'Khushdev Pandit': {'records': [('Gate3', 'EXIT', '14:39:18'), ('Gate1', 'ENTER', '14:40:01'), ('Gate1', 'EXIT', '14:40:15'), ('Gate3', 'ENTER', '14:41:09'), ('Gate3', 'EXIT', '14:42:09'), ('Gate3', 'ENTER', '14:42:38'), ('Gate3', 'EXIT', '14:42:54'), ('Gate5', 'ENTER', '14:43:07'), ('Gate3', 'EXIT', '14:43:44')], 'inside': False},
    'Ujjwal Garg': {'records': [('Gate3', 'ENTER', '14:39:40'), ('Gate3', 'EXIT', '14:42:29')], 'inside': False},
    'Swati Jha': {'records': [('Gate1', 'ENTER', '14:39:44')], 'inside': True},
    'Shambhavi Sharma': {'records': [('Gate3', 'EXIT', '14:39:53')], 'inside': False},
    'Yuvraj Singh': {'records': [('Gate1', 'ENTER', '14:40:16'), ('Gate1', 'EXIT', '14:42:45')], 'inside': False},
    'Sushil Kumar': {'records': [('Gate1', 'EXIT', '14:40:37')], 'inside': False},
    'Mohammed Kaif': {'records': [('Gate5', 'ENTER', '14:40:46')], 'inside': True},
    'Thakkar Divyakumar Rameshbhai': {'records': [('Gate5', 'ENTER', '14:41:03'), ('Gate3', 'EXIT', '14:43:13')], 'inside': False},
    'Vibhor Agarwal': {'records': [('Gate1', 'ENTER', '14:41:12')], 'inside': True},
    'Snehal': {'records': [('Gate5', 'EXIT', '14:41:17'), ('Gate1', 'ENTER', '14:41:32'), ('Gate1', 'EXIT', '14:43:39'), ('Gate3', 'EXIT', '14:43:44')], 'inside': False},
    'Aditya Raj Singh': {'records': [('Gate1', 'EXIT', '14:41:46')], 'inside': False},
    'Swatantra kumar nigam': {'records': [('Gate5', 'ENTER', '14:42:04')], 'inside': True},
    'Manav Saini': {'records': [('Gate1', 'ENTER', '14:42:06')], 'inside': True},
    'Anuj Yadav': {'records': [('Gate3', 'EXIT', '14:42:13')], 'inside': False},
    'Karan Baboota': {'records': [('Gate3', 'EXIT', '14:42:36')], 'inside': False},
    'Thanmayee Matha': {'records': [('Gate5', 'EXIT', '14:43:01')], 'inside': False}
}

def test_check_status():
    check_status('Rishabh Oberoi')  # Expected: Records for Rishabh Oberoi: Currently inside: No
    check_status('Gayam Shivakanth Reddy')  # Expected: Records for Gayam Shivakanth Reddy: Currently inside: No
    check_status('Shraman Jain')  # Expected: Records for Shraman Jain: Currently inside: Yes
    check_status('Khushdev Pandit')  # Expected: Records for Khushdev Pandit: Currently inside: No
    check_status('Ujjwal Garg')  # Expected: Records for Ujjwal Garg: Currently inside: No
    check_status('Swati Jha')  # Expected: Records for Swati Jha: Currently inside: Yes
    check_status('Shambhavi Sharma')  # Expected: Records for Shambhavi Sharma: Currently inside: No
    check_status('Yuvraj Singh')  # Expected: Records for Yuvraj Singh: Currently inside: No
    check_status('Sushil Kumar')  # Expected: Records for Sushil Kumar: Currently inside: No
    check_status('Mohammed Kaif')  # Expected: Records for Mohammed Kaif: Currently inside: Yes
    check_status('Vibhor Agarwal')  # Expected: No records for this student.
    check_status('Snehal')  # Expected: Records for Snehal: Currently inside: No
    check_status('Swatantra kumar nigam')  # Expected: Records for Swatantra kumar nigam: Currently inside: Yes
    check_status('Manav Saini')  # Expected: Records for Manav Saini: Currently inside: Yes
test_check_status()

def test_check_time_range():
    print("\nTest 1: Exact match for time range")
    check_time_range('14:39:00', '14:40:00')  # Expected: Entries within this range (e.g., Rishabh Oberoi, Gayam Shivakanth Reddy)
    print("\nTest 2: Time range with no entries")
    check_time_range('14:43:00', '14:45:00')  # Expected: No records, as all entries are earlier.
    print("\nTest 3: Time range including multiple records")
    check_time_range('14:39:00', '14:42:00')  # Expected: Entries within this range (multiple students, e.g., Rishabh Oberoi, Gayam Shivakanth Reddy, Khushdev Pandit)  
    print("\nTest 4: Range with a single entry")
    check_time_range('14:41:00', '14:42:00')  # Expected: A record like Mohammed Kaif or Manav Saini (individual entries) 
    print("\nTest 5: Reverse order time range (invalid case)")
    check_time_range('14:43:00', '14:39:00')  # Expected: No records, as the time range is reversed.
test_check_time_range()

def test_check_gate():
    check_gate('Gate1')  # Expected: Entries: 7, Exits: 7
    check_gate('Gate3')  # Expected: Entries: 8, Exits: 9
    check_gate('Gate5')  # Expected: Entries: 8, Exits: 7
    check_gate('Gate2')  # Expected: Entries: 0, Exits: 0
test_check_gate()

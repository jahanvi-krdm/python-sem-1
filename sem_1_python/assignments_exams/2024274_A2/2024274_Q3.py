def count_signatures(records):
    return {student: sum(signatures.values()) for student, signatures in records.items()}

def find_min_max_students(signature_count):
    min_signatures = min(signature_count.values())
    max_signatures = max(signature_count.values())
    
    least_signed = [student for student, count in signature_count.items() if count == min_signatures]
    most_signed = [student for student, count in signature_count.items() if count == max_signatures]
    
    return least_signed, most_signed

records = {
    'student1': {'student2': 1, 'student3': 1},
    'student2': {'student1': 1, 'student3': 0},
    'student3': {'student1': 0, 'student2': 0}
}

signature_count = count_signatures(records)
least_signed, most_signed = find_min_max_students(signature_count)
print("Students with least signatures:", least_signed)
print("Students with most signatures:", most_signed)

def test():
    assert count_signatures({
        'student1': {'student2': 2, 'student3': 2},
        'student2': {'student1': 1, 'student3': 0},
        'student3': {'student1': 2, 'student2': 0}
    }) == {'student1': 4, 'student2': 1, 'student3': 2}, "Test failed for count_signatures"

    signature_data_test = {'student1': 4, 'student2': 1, 'student3': 2}
    low_signers, high_signers = find_min_max_students(signature_data_test)
    assert low_signers == ['student2'], "Test failed for low_signers"
    assert high_signers == ['student1'], "Test failed for high_signers"

test()
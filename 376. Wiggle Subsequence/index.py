def wiggle_sequence(sequence):
    print(sequence)
    def null_remote(sequence):
        new_sequence = []
        for i in sequence:
            try:
                if float(i) == 0:
                    continue
                else:
                    new_sequence.append(i)
            except ValueError:
                continue
        return new_sequence

    def differences_create(new_sequence):
        differences = []
        for i in range(len(new_sequence)):
            if i == 0:
                continue
            else:
                difference = new_sequence[i] - new_sequence[i - 1]
                differences.append(difference)
        print(differences)
        return differences

    def sign(i):
        if i > 0:
            return True
        if i < 0:
            return False

    def maximum_length_calculation(differences):
        max_count = 0
        current_count = 0
        for i in range(len(differences)):
            if i == 0:
                continue
            else:
                current_sign = sign(differences[i])
                previous_sign = sign(differences[i - 1])
                if current_sign != previous_sign:
                    current_count += 1
                    if current_count > max_count:
                        max_count = current_count
                else:
                    current_count = 0
        return max_count

    return maximum_length_calculation(differences_create(null_remote(sequence)))


test_value = [1,17,5,10,13,15,10,5,16,8]

print(wiggle_sequence(test_value))

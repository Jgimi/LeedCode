def wiggle_sequence(nums):
    print(nums)

    def null_remote(nums):
        new_sequence = []
        for i in nums:
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
            current_sign = sign(differences[i])
            try:
                next_sign = sign(differences[i + 1])
            except IndexError:
                break
            if current_sign != next_sign:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                continue
        if len(differences) == 0:
            return max_count+1
        else:
            return max_count + 2

    return maximum_length_calculation(null_remote(differences_create(nums)))


test_value = [3,3,3,2,5]

print(wiggle_sequence(test_value))

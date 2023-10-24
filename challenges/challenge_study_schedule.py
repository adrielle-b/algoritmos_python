def study_schedule(permanence_period, target_time):
    try:
        count_student = 0
        for start, end in permanence_period:
            if start <= target_time <= end:
                count_student += 1
        return count_student
    except TypeError:
        return None
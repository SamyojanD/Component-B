import sys

def analyze_cat_shelter_log(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        cat_visits = 0
        other_cats = 0
        total_time_in_house = 0
        durations = []

        for line in lines:
            if line.strip() == 'END':
                break

            data = line.strip().split(',')
            cat_name, entry_time, exit_time = data

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            duration = exit_time - entry_time

            if cat_name == 'OURS':
                cat_visits += 1
                total_time_in_house += duration
                durations.append(duration)
            elif cat_name == 'THEIRS':
                other_cats += 1

        average_duration = 0 if not durations else sum(durations) / len(durations)
        longest_duration = max(durations) if durations else 0
        shortest_duration = min(durations) if durations else 0

        print("\nLog File Analysis")
        print("==================\n")
        print("Cat Visits:", cat_visits)
        print("Other Cats:", other_cats)
        print("\nTotal Time in House: {} Hours, {} Minutes".format(
            total_time_in_house // 60, total_time_in_house % 60))
        print("\nAverage Visit Length: {} Minutes".format(int(average_duration)))
        print("Longest Visit:        {} Minutes".format(longest_duration))
        print("Shortest Visit:       {} Minutes".format(shortest_duration))

    except FileNotFoundError:
        print('Cannot open "{}"!'.format(filename))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        print("Usage: {} <filename>".format(sys.argv[0]))
        sys.exit(1)

    log_filename = sys.argv[1]

    analyze_cat_shelter_log(log_filename)

import csv

def notation_relation(notation):
    relationships = {
        'a': "AccessRelationship",
        'c': "CompositionRelationship",
        'f': "FlowRelationship",
        'g': "AggregationRelationship",
        'i': "AssignmentRelationship",
        'n': "InfluenceRelationship",
        'o': "AssociationRelationship",
        'r': "RealizationRelationship",
        's': "SpecializationRelationship",
        't': "TriggeringRelationship",
        'v': "ServingRelationship"
    }
    return relationships.get(notation, 'Unknown notation')

# Input and output file paths
input_file = 'Gbus.csv'
output_file = 'Gbus_output.csv' 

# Read from input CSV and write to output CSV
try:
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Read and write the header
        header = next(reader, None)
        writer.writerow(["Source", "Relation", "Target"])  # Write a new header

        for row in reader:
            print(f"Processing row: {row}")  # Debug line to see what row is being processed
            if len(row) == 3:
                entity1, notations, entity2 = row
                for notation in notations:
                    expanded_notation = notation_relation(notation)
                    new_row = [entity1, expanded_notation, entity2]
                    print(f"Writing new row: {new_row}")  # Debug line to see what row is being written
                    writer.writerow(new_row)
            else:
                print(f"Skipping invalid row: {row}")
except Exception as e:
    print(f"An error occurred: {e}")

print("Conversion complete. Output written to", output_file)

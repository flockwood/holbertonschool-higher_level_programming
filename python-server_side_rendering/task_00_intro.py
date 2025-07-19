import os

# Type checks
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"[ERROR] template must be a string, got {type(template)}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("[ERROR] attendees must be a list of dicts")
        return

    # Empty checks
    if template.strip() == '':
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, person in enumerate(attendees, start=1):
        # Safely get values or default to "N/A"
        name = person.get('name') or "N/A"
        title = person.get('event_title') or "N/A"
        date = person.get('event_date') or "N/A"
        location = person.get('event_location') or "N/A"

        # FIll in the template
        filled = (template
                  .replace('{name}', name)
                  .replace('{event_title}', title)
                  .replace('{event_date}', date)
                  .replace('{event_location}', location)
                  )

        # Write to output_i.txt
        out_path = f"output_{i}.txt"
        try:
            with open(out_path, 'w') as out_file:
                out_file.write(filled)
        except OSError as e:
            print(f"[ERROR] Could not write {out_path}: {e}")




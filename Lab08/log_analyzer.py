print(f"ERROR REPORT")
print(f"----------------------------------------")

error_count = 0
warning_count = 0

with open("application.log", "r") as log_file:
    for line in log_file:

        timestamp = line[:19]
        if "error" in line.lower() or "warning" in line.lower():
        
            if line.lower().find("error") != -1 or line.lower().find("warning") != -1:
                line = line.replace("error", "ERROR")
                line = line.replace("warning", "WARNING")

            fields = line.split("|")

            timestamp = fields[0].strip()
            severity = fields[1].strip()
            message = fields[2].strip()


            if severity == "ERROR":
                error_count += 1
            elif severity == "WARNING":
                warning_count += 1

            report_entry = " - ".join(fields)
            print(report_entry)

print(f"\nTotal errors and warnings: {error_count + warning_count}")

#For some reason my computer was not picking up the application.log file for a bit
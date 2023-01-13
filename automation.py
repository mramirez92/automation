import re

with open("./assets/potential_contacts.txt", "r") as f:
    text_from_file = f.read()

# pattern resources in README.md
email_pattern = r"[\w.-]+@[\w.-]+(?:\.[\w.-]+)*\.[a-z]{2,6}"
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

# set does the heavy lifting to remove duplicates
phone_data = sorted(set(re.findall(phone_pattern,re.sub(r'[^\d+]', '', text_from_file))))
email_data = sorted(set(re.findall(email_pattern, text_from_file)))

numbers_formatted = [f"{n[:3]}-{n[3:6]}-{n[6:]}" for n in phone_data]

with open("./collected/email_collected.txt", "w") as f:
    for emails in email_data:
        f.write(emails + "\n")

with open("./collected/phone_collected.txt", "w") as f:
    for numbers in numbers_formatted:
        f.write(numbers + "\n")

def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Arun", age=21, city="Chennai", course="AI")

def analyze_student(student):
    """
    Analyze a student's academic performance.
    Returns a dictionary with:
    - average
    - risk
    - recommendation
    """

    average = (
        student.math_marks +
        student.science_marks +
        student.english_marks
    ) / 3

    # Determine risk
    if student.attendance < 60 or average < 50:
        risk = "High"
        recommendation = (
            "Increase attendance, attend extra classes, "
            "and meet your faculty advisor."
        )

    elif student.attendance < 75 or average < 65:
        risk = "Medium"
        recommendation = (
            "Practice weak subjects and maintain regular attendance."
        )

    else:
        risk = "Low"
        recommendation = (
            "Keep up the good work and continue consistent study habits."
        )

    return {
        "average": round(average, 2),
        "risk": risk,
        "recommendation": recommendation
    }